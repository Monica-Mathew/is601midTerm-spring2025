'''My App test'''
import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['2 2 unknown_command', '2 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
    assert "Usage : <number1> <number2> <operation>" in captured.out
    assert excinfo.value.code == 1
    assert "Exiting Command line" in captured.out

def test_app_menu_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    captured = capfd.readouterr()
    assert "Printing Menu" in captured.out
    assert "- add" in captured.out
    assert "- divide" in captured.out
    assert "- multiply" in captured.out
    assert "- subtract" in captured.out
    assert excinfo.value.code == 1
    assert "Exiting Command line" in captured.out
