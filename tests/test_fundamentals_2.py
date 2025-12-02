import importlib.util
from pathlib import Path
import builtins
import pytest
from core_python.Fundamental_2.dataTypes import decades
from core_python.Fundamental_2 import conditionalsAndImports

@pytest.fixture
def sample_list():
    return [1, 2, 3]

# a demo method how to load a module from the file
def _load_data_types_module():
    path = Path(__file__).resolve().parents[1] / "core_python" / "2.Fundamentals" / "dataTypes.py"
    spec = importlib.util.spec_from_file_location("dataTypes", str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_decades_prints_correct_message(monkeypatch, capsys):
    # Provide a birth year that yields a clear decade and remainder
    monkeypatch.setattr(builtins, "input", lambda prompt="": "1985")
    decades()
    captured = capsys.readouterr()
    assert "You were born in the 1980s and 5 years old." in captured.out


def test_rock_paper_scissors_tie(monkeypatch, capsys):
    # computer chooses rock, user chooses rock -> TIE
    monkeypatch.setattr(conditionalsAndImports.random, "choice", lambda seq: "rock")
    monkeypatch.setattr(builtins, "input", lambda prompt="": "rock")
    conditionalsAndImports.rock_paper_scissors()
    captured = capsys.readouterr()
    assert "TIE" in captured.out
    assert "Computer chose: rock" in captured.out


def test_rock_paper_scissors_user_wins(monkeypatch, capsys):
    # computer chooses scissors, user chooses rock -> YOU WIN
    monkeypatch.setattr(conditionalsAndImports.random, "choice", lambda seq: "scissors")
    monkeypatch.setattr(builtins, "input", lambda prompt="": "rock")
    conditionalsAndImports.rock_paper_scissors()
    captured = capsys.readouterr()
    assert "YOU WIN" in captured.out


def test_rock_paper_scissors_user_loses(monkeypatch, capsys):
    # computer chooses paper, user chooses rock -> YOU LOSE
    monkeypatch.setattr(conditionalsAndImports.random, "choice", lambda seq: "paper")
    monkeypatch.setattr(builtins, "input", lambda prompt="": "rock")
    conditionalsAndImports.rock_paper_scissors()
    captured = capsys.readouterr()
    assert "YOU LOSE" in captured.out

