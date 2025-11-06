import builtins
import os
import shutil
import pytest
import sys

# append parent directory to import your script
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import project_manager

# ---- Fixtures ----
@pytest.fixture
def temp_dir(tmp_path):
    # create a temporary directory for testing filesystem operations
    return tmp_path

# ---- Test searchFolder ----
def test_searchFolder_found(monkeypatch, temp_dir):
    folder_name = "TestFolder"
    test_path = temp_dir / folder_name
    test_path.mkdir()
    
    # monkeypatch os.walk to search in tmp_path
    monkeypatch.setattr(os, "walk", lambda _: [(str(temp_dir), [folder_name], [])])
    
    result = project_manager.searchFolder(folder_name)
    assert folder_name in result

def test_searchFolder_not_found(monkeypatch, temp_dir):
    monkeypatch.setattr(os, "walk", lambda _: [(str(temp_dir), [], [])])
    result = project_manager.searchFolder("MissingFolder")
    assert result is None

# ---- Test searchFile ----
def test_searchFile_found(monkeypatch, temp_dir):
    file_name = "file.txt"
    (temp_dir / file_name).write_text("test")
    monkeypatch.setattr(os, "walk", lambda _: [(str(temp_dir), [], [file_name])])
    
    result = project_manager.searchFile(file_name)
    assert file_name in result

def test_searchFile_not_found(monkeypatch, temp_dir):
    monkeypatch.setattr(os, "walk", lambda _: [(str(temp_dir), [], [])])
    result = project_manager.searchFile("nofile.txt")
    assert result is None

# ---- Test delNonEmptyDir ----
def test_delNonEmptyDir(temp_dir):
    folder_path = temp_dir / "DeleteMe"
    folder_path.mkdir()
    (folder_path / "file.txt").write_text("data")
    
    project_manager.delNonEmptyDir(str(folder_path))
    assert not folder_path.exists()

# ---- Test createDir via main menu ----
def test_createDir_main(monkeypatch, tmp_path):
    # Prepare inputs for main() menu:
    # 1 -> choose "Create Directory"
    # tmp_path / "NewDir" -> directory name
    # n -> exit after
    inputs = iter([
        "1",                     # menu choice for Create Directory
        str(tmp_path / "NewDir"),# directory name input
        "n"                      # exit after creation
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    
    # Monkeypatch os.chdir to stay in tmp_path
    monkeypatch.setattr(os, "chdir", lambda x: None)
    
    # Run the script via main
    project_manager.main()
    
    # Assert the new directory exists
    assert (tmp_path / "NewDir").exists()