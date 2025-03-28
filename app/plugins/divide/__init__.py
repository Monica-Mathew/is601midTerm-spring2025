'''Divide plugin'''
from decimal import Decimal
import logging
import sys
from app.commands import Command
from calculator import Calculator

class DivideCommand(Command):
    '''Divide command class'''
    def execute(self,a,b):
        '''being called from CommandHandler to execute the function'''
        a_decimal, b_decimal = map(Decimal, [a,b])
        try:
            logging.info("Divide command function invoked")
            print(f"The result of {a_decimal} divide {b_decimal} is equal to {Calculator.divide(a_decimal,b_decimal):.2f}")
        except ZeroDivisionError:
            print("Error :Division by zero")
        except Exception as e:# pylint: disable=broad-exception-caught 
            print(f"An error occured : {e}") 
