'''My App test'''
import pytest
from app import App
from calculator.calculations import Calculations

def test_app_get_environment_variable():
    """Test the app environment variable"""
    app = App()
    current_env = app.get_environment_variable('ENVIRONMENT')
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"
    
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
    assert "- add" in captured.out
    assert "- divide" in captured.out
    assert "- history-clear" in captured.out
    assert "- history-delete" in captured.out
    assert "- history-load" in captured.out
    assert "- history-save" in captured.out
    assert "- history-show" in captured.out
    assert "- modulo" in captured.out
    assert "- multiply" in captured.out
    assert "- subtract" in captured.out
    assert excinfo.value.code == 1
    assert "Exiting Command line" in captured.out

@pytest.fixture(autouse=True)
def clear_history():
    '''clearing history'''
    Calculations.clear_history()

@pytest.mark.parametrize("inputs, expected_output", [
    (['5 3 add', 'exit'], "The result of 5 add 3 is equal to 8\nExiting Command line"),
    (['10 2 subtract', 'exit'], "The result of 10 subtract 2 is equal to 8\nExiting Command line"),
    (['4 5 multiply', 'exit'], "The result of 4 multiply 5 is equal to 20\nExiting Command line"),
    (['20 4 divide', 'exit'], "The result of 20 divide 4 is equal to 5.00\nExiting Command line"),
    (['2 2 modulo', 'exit'], "The result of 2 modulo 2 is equal to 0\nExiting Command line"),
    (['1 0 divide', 'exit'], "An error occured : Cannot divide by zero - Exception\nExiting Command line"),
    (['9 3 unknown', 'exit'], "No such command: unknown\nExiting Command line"),
    (['a 3 add', 'exit'], "Invalid number input: a or 3 is not a valid number.\nExiting Command line"),
    (['5 b subtract', 'exit'], "Invalid number input: 5 or b is not a valid number.\nExiting Command line"),
    (['history-show', '2 2 add', 'history-save', 'exit'], "No history available to show, start adding calculations.\nThe result of 2 add 2 is equal to 4\nAdding in memory calculation history to csv\nExiting Command line"),
    (['history-delete', 'history-load', 'exit'], "History file has been cleared.\nNo history available to show from csv file.\nExiting Command line"),
    (['history-clear', 'history-show', '5 0 add', 'history-show','history-save','history-load','exit'],
     "No history available to show, start adding calculations.\nThe result of 5 add 0 is equal to 5\nHistory of the calculations from memory:\nCalcualtion of 5 and 0 with add, Result: 5.00\nAdding in memory calculation history to csv\nHistory of the calculations loaded from csv:\n5 add 0 = 5.0\nExiting Command line")
])
def test_app_operations(inputs, expected_output, capfd, monkeypatch):
    """Test how the REPL handles various calculator operations and errors."""
    def input_side_effect(prompt):
        return inputs.pop(0)  
    monkeypatch.setattr('builtins.input', input_side_effect)
    app = App()
    with pytest.raises(SystemExit): 
        app.start()
    captured = capfd.readouterr()
    full_expected_output = f"Type 'exit' to exit, 'menu' to see list of operations\n{expected_output}"
    assert full_expected_output in captured.out  # Check if the expected output is in the captured output
