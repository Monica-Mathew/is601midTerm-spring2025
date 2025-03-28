'''Add plugin'''
from decimal import Decimal
import logging
import sys
from app.commands import Command
from calculator import Calculator


class AddCommand(Command):
    '''Add command class'''
    def execute(self,a,b): 
        '''being called from CommandHandler to execute the function'''
        a_decimal, b_decimal = map(Decimal, [a,b])
        logging.info("Add command function invoked")
        print(f"The result of {a_decimal} add {b_decimal} is equal to {Calculator.add(a_decimal,b_decimal)}")
