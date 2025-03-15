'''Divide plugin'''
from decimal import Decimal
import sys
from app.commands import Command
from calculator import Calculator

class DivideCommand(Command):
    '''Divide command class'''
    def execute(self,a,b):
        '''being called from CommandHandler to execute the function'''
        a_decimal, b_decimal = map(Decimal, [a,b])
        try:
            print(f"The result of {a_decimal} divide {b_decimal} is equal to {Calculator.divide(a_decimal,b_decimal)}")
        except ValueError:
            print("Error :Division by zero")
        except Exception as e:# pylint: disable=broad-exception-caught
            print(f"An error occured : {e}") 
