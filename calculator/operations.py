'''Operations file'''
from decimal import Decimal

def add(a: Decimal, b:Decimal) -> Decimal:
    '''Add operation'''
    return a + b
def subtract(a: Decimal, b:Decimal) -> Decimal:
    '''subtract operation'''
    return a + b
def multiply(a: Decimal, b:Decimal) -> Decimal:
    '''multiply operation'''
    return a + b
def divide(a: Decimal,b:Decimal) -> Decimal:
    '''divide operation'''
    if b ==0:
        raise ValueError("Cannot divide by zero - Exception")
    return a/b
