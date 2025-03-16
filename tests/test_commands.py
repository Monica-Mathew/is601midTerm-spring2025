'''My Command test'''
import pytest
from app import App
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand

def test_add_command(capfd):
    '''Testing add command'''
    command = AddCommand()
    command.execute(2,2)
    out = capfd.readouterr().out
    assert out == "The result of 2 add 2 is equal to 4\n"

def test_subtract_command(capfd):
    '''Testing subtract command'''
    command = SubtractCommand()
    command.execute(2,2)
    out = capfd.readouterr().out
    assert out == "The result of 2 subtract 2 is equal to 0\n"

def test_divide_command(capfd):
    '''testing divide command'''
    command = MultiplyCommand()
    command.execute(2,2)
    out = capfd.readouterr().out
    assert out == "The result of 2 multiply 2 is equal to 4\n"

def test_multiply_command(capfd):
    '''testing multiply command'''
    command = DivideCommand()
    command.execute(2,2)
    out = capfd.readouterr().out
    assert out == "The result of 2 divide 2 is equal to 1.00\n"

def test_app_subtract_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['2 2 subtract', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert "Exiting Command line" in captured.out
    assert str(e.value) == '1'
