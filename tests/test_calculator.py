'''My calculator test'''
from calculator import Calculator

def test_addition():
    '''Test that additon function works'''
    assert Calculator.add(2,2) ==4

def test_subtraction():
    '''Test that subtraction function works'''
    assert Calculator.subtract(2,2) ==0

def test_multiply():
    '''Test that multiply function works'''
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that divide function works'''
    assert Calculator.divide(2,2) ==1
