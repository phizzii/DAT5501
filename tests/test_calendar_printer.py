# calendar printer testing suite
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import calender_printer_python

import builtins
from io import StringIO
import sys
import pytest # so i can use monkeypatch instead of inputs (as it would need keyboard input to run)

def test_calendar_output_structure(monkeypatch, capsys):
    # fake user input
    inputs = iter(["30", "Mon"])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))

    # import the script
    import calender_printer_python

    # 'capture' printed output
    capture = capsys.readouterr().out

    # check day headers and lines
    assert "Mon" in capture
    assert "Tue" in capture
    assert "---" in capture
    assert "30" in capture

def test_starting_day_invalid(monkeypatch):
    # test script with invalid input
    inputs = iter(["31", "Funday"])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))

    with pytest.raises(ValueError):
        import calender_printer_python
                   
