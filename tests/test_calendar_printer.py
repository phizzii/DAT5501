# calendar printer testing suite

import builtins
from io import StringIO
import sys
import pytest # so i can use monkeypatch instead of inputs (as it would need keyboard input to run)

def test_calendar_output_structure(monkeypatch, capsys)
