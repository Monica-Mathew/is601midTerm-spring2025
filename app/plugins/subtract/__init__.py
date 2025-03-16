'''Subtract plugin'''
from decimal import Decimal
import logging
from app.commands import Command
from calculator import Calculator

class SubtractCommand(Command):
    '''Subtract command class'''
    def execute(self,a,b):
        '''being called from CommandHandler to execute the function'''
        a_decimal, b_decimal = map(Decimal, [a,b])
        logging.info("Subtract command function invoked")
        print(f"The result of {a_decimal} subtract {b_decimal} is equal to {Calculator.subtract(a_decimal,b_decimal)}")
