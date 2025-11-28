import csv
import os
import tempfile
import pytest

from small_projects.sheet_music_collection_manager import Piece, CollectionManager

def test_piece_initialization():
    # basic test class pieces (they are so overplayed but im not gonna over complicate it)
    p = Piece("Moonlight Sonata", "Beethoven", "Romantic", "Piano", "7")
    assert p.title == "Moonlight Sonata"
    assert p.composer == "Beethoven"
    assert p.time_period == "Romantic"
    assert p.instrumentation == "Piano"
    assert p.difficulty == "7"

@pytest.fixture
def cm():
    return CollectionManager()

# basic functionality tests
def test_add_piece(cm):
    p = Piece("Test", "Composer", "Modern", "Violin", "5")
    cm.add_piece(p)
    assert len(cm.pieces) == 1
    assert cm.pieces[0].title == "Test"


def test_remove_piece(cm):
    p = Piece("Test", "Composer", "Modern", "Violin", "5")
    cm.add_piece(p)
    cm.remove_piece("Test")
    assert len(cm.pieces) == 0


def test_edit_piece_existing(cm):
    p = Piece("Test", "C1", "Baroque", "Piano", "3")
    cm.add_piece(p)

    result = cm.edit_piece("Test", composer="Mozart", difficulty="8")
    assert result is True
    assert p.composer == "Mozart"
    assert p.difficulty == "8"


def test_edit_piece_nonexistent(cm):
    result = cm.edit_piece("DoesNotExist", composer="X")
    assert result is False


# sorting tests
def test_sort_by_title(cm):
    p1 = Piece("C Title", "A", "", "", "")
    p2 = Piece("A Title", "B", "", "", "")
    p3 = Piece("B Title", "C", "", "", "")

    cm.add_piece(p1)
    cm.add_piece(p2)
    cm.add_piece(p3)

    cm.sort_by("title")
    titles = [p.title for p in cm.pieces]
    assert titles == ["A Title", "B Title", "C Title"]


def test_sort_by_composer(cm):
    p1 = Piece("X", "Zoe", "", "", "")
    p2 = Piece("X", "Aaron", "", "", "")
    p3 = Piece("X", "Milo", "", "", "")

    cm.add_piece(p1)
    cm.add_piece(p2)
    cm.add_piece(p3)

    cm.sort_by("composer")
    composers = [p.composer for p in cm.pieces]
    assert composers == ["Aaron", "Milo", "Zoe"]

# tests to make sure the csv imports properlyy
def test_import_from_csv(cm, tmp_path):
    csv_file = tmp_path / "import_test.csv"

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["title", "composer", "time_period", "instrumentation", "difficulty"],
        )
        writer.writeheader()
        writer.writerow({
            "title": "Clair de Lune",
            "composer": "Debussy",
            "time_period": "Modern",
            "instrumentation": "Piano",
            "difficulty": "6",
        })

    cm.import_from_csv(csv_file)

    assert len(cm.pieces) == 1
    assert cm.pieces[0].title == "Clair de Lune"
    assert cm.pieces[0].composer == "Debussy"


def test_import_csv_missing_title(cm, tmp_path):
    csv_file = tmp_path / "bad.csv"

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["composer"])
        writer.writeheader()
        writer.writerow({"composer": "Bach"})

    cm.import_from_csv(csv_file)

    # make sure it didn't add invalid piece o_O
    assert len(cm.pieces) == 0


# test to make sure csv export is fine
def test_export_to_csv(cm, tmp_path):
    cm.add_piece(Piece("TestPiece", "Composer", "Baroque", "Flute", "2"))

    output_file = tmp_path / "export_test.csv"
    cm.export_to_csv(output_file)

    assert output_file.exists()

    # Read back exported CSV
    with open(output_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 1
    assert rows[0]["title"] == "TestPiece"
    assert rows[0]["composer"] == "Composer"
