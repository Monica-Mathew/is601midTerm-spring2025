'''My Operations test'''
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation(a,b,operation,expected):
    '''testing various operations'''
    calculation =  create_Calculation_Instance(a,b,operation)
    assert calculation.performOperation() == expected, f"{operation.__name__} operation failed"

def create_Calculation_Instance(a,b,operation):
    '''adding a helper funcation to instaniate using create static method'''
    calculation = Calculation.create(Decimal(a),Decimal(b),operation)
    return calculation

def test_operation_add():
    '''Testing the adding operation'''
    test_operation(10,5,add,15)

def test_operation_subtract():
    '''Testing the subtract operation'''
    test_operation(10,5,subtract,5)

def test_operation_multiply():
    '''Testing the multiply operation'''
    test_operation(10,5,multiply,50)

def test_operation_divide():
    '''Testing the divison operation'''
    test_operation(10,5,divide,2)
