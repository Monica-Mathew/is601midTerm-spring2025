'''My calculation test'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, divide


def test_calculation_operations(a, b, operation, expected):
    '''test calculation operation with various scenarions'''
    calc = Calculation(a, b, operation) # creating an instance with given parameters.
    assert calc.performOperation() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr(): # we have conftest defined for repr and divisioin
    '''test representation of the calcualtion'''
    calc = Calculation(Decimal('10'), Decimal('5'),add)
    expected_repr = "Calcualtion of 10 and 5 with add"
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string"

def test_divide_by_zero():
    '''Check Value error thrown for division by zero'''
    calc = Calculation(Decimal('10'), Decimal('0'),divide)
    with pytest.raises(ValueError, match='Cannot divide by zero - Exception'):
        calc.performOperation()
