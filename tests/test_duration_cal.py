import builtins
import numpy as np
import pytest

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import Week5.duration_calculator_python as duration_calculator_python


def test_days_difference_correct(monkeypatch, capsys):
    # put fake date
    inputs = iter(["2000-01-01"])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))

    duration_calculator_python.main()
    
    capture = capsys.readouterr().out

    assert "2000-01-01" in capture
    assert "today" not in capture
    assert "9463" in capture # THIS NEEDS TO BE CONSISTENTLY CHANGED ALIGNING WITH THE CURRENT DATE

def test_invalid_date_input(monkeypatch):
    inputs = iter(["not-a-date"])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))

    with pytest.raises(ValueError):
        duration_calculator_python.main()