'''Operations file'''
from decimal import Decimal
import logging

def add(a: Decimal, b:Decimal) -> Decimal:
    '''Add operation'''
    return a + b
def subtract(a: Decimal,b:Decimal) -> Decimal:
    '''Subtract operation'''
    return a-b
def multiply(a: Decimal,b:Decimal) -> Decimal:
    '''Multiply operation'''
    return a*b
# def divide(a: Decimal,b:Decimal) -> Decimal: # LBYL sample
#     '''Divide operation'''
#     if b ==0:
#         logging.error("Divsion by zero")
#         raise ValueError("Cannot divide by zero - Exception")
#     return a/b
def divide(a: Decimal, b: Decimal) -> Decimal:
    '''Divide operation'''
    try:
        return a / b  # Attempting division  #EAFP
    except ZeroDivisionError:
        logging.error("Division by zero")
        raise ValueError("Cannot divide by zero - Exception")