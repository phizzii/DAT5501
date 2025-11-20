import os
import shutil
import pytest
from unittest.mock import patch

# importing my functions
from file_manager import searchFolder, searchFile, delNonEmptyDir

def test_search_folder_finds_directory(tmp_path, monkeypatch):
    # Create directory structure
    base = tmp_path / "Users"
    base.mkdir()
    (base / "target_dir").mkdir()

    # Mock os.walk to walk through tmp_path instead of /Users
    def fake_walk(_):
        for root, dirs, files in os.walk(base):
            yield root, dirs, files

    monkeypatch.setattr("os.walk", fake_walk)

    from file_manager import searchFolder
    result = searchFolder("target_dir")

    assert result is not None
    assert "target_dir" in result


def test_search_folder_not_found(monkeypatch, tmp_path):
    base = tmp_path / "Users"
    base.mkdir()

    def fake_walk(_):
        for root, dirs, files in os.walk(base):
            yield root, dirs, files

    monkeypatch.setattr("os.walk", fake_walk)

    from file_manager import searchFolder
    result = searchFolder("missing_dir")
    assert result is None

def test_search_file_finds_file(tmp_path, monkeypatch):
    base = tmp_path / "Users"
    base.mkdir()
    file = base / "data.txt"
    file.write_text("hello")

    def fake_walk(_):
        for root, dirs, files in os.walk(base):
            yield root, dirs, files

    monkeypatch.setattr("os.walk", fake_walk)

    from file_manager import searchFile
    result = searchFile("data.txt")

    assert result is not None
    assert result.endswith("data.txt")


def test_search_file_not_found(monkeypatch, tmp_path):
    base = tmp_path / "Users"
    base.mkdir()

    def fake_walk(_):
        for root, dirs, files in os.walk(base):
            yield root, dirs, files

    monkeypatch.setattr("os.walk", fake_walk)

    from file_manager import searchFile
    result = searchFile("missing.txt")
    assert result is None

def test_del_non_empty_dir(tmp_path):
    folder = tmp_path / "todelete"
    folder.mkdir()
    file = folder / "inner.txt"
    file.write_text("stuff")

    from file_manager import delNonEmptyDir
    delNonEmptyDir(str(folder))

    assert not folder.exists()