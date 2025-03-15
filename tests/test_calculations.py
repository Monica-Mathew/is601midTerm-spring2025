'''My calculations test'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
    '''clearing and setting history'''
    Calculations.clear_history()
    Calculations.add_calculation_to_history(Calculation(Decimal('10'), Decimal('5'),add))
    Calculations.add_calculation_to_history(Calculation(Decimal('20'), Decimal('3'),subtract))

def test_add_calculation_to_history(setup_calculations): #passing the fixture for each test
    '''test adding a calcualtion to the history'''
    calc =  Calculation.create(Decimal('2'),Decimal('2'),add)
    Calculations.add_calculation_to_history(calc)
    assert Calculations.get_latest() == calc, "Failed to add calc to the history"

def test_get_history(setup_calculations):
    '''test retreving history'''
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain expected number of calculations"

def test_clear_history(setup_calculations):
    '''test clearing history'''
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    '''test getting the latest calculation from history'''
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the latest calculation added"

def test_get_latest_with_empty_history():
    '''test getting None from latest when histiory is empty'''
    Calculations.clear_history()
    latest = Calculations.get_latest()
    assert latest is None, "Expected None for latest calcualtion with empty history"


def test_find_by_operation(setup_calculations):
    '''test finding operation by the operation type'''
    add_operation = Calculations.find_by_operation("add")
    assert len(add_operation) ==1, "Failed to find add operation from history"
    subtract_operation = Calculations.find_by_operation("subtract")
    assert len(subtract_operation) ==1, "Failed to find subtract operation from history"
