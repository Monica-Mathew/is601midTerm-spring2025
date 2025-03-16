'''Multiply plugin'''
from decimal import Decimal
import logging
import sys
from app.commands import Command
from calculator import Calculator


class MultiplyCommand(Command):
    '''Multiply command class'''
    def execute(self,a,b):
        '''being called from CommandHandler to execute the function'''
        a_decimal, b_decimal = map(Decimal, [a,b])
        logging.info("Multiply command function invoked")
        print(f"The result of {a_decimal} multiply {b_decimal} is equal to {Calculator.multiply(a_decimal,b_decimal)}")
