from decimal import Decimal
import sys
from app.commands import Command
from calculator import Calculator


class MultiplyCommand(Command):

    def execute(self,a,b):
        '''being called from CommandHandler to execute the function'''
        a_decimal, b_decimal = map(Decimal, [a,b])
        print(f"The result of {a_decimal} multiply {b_decimal} is equal to {Calculator.multiply(a_decimal,b_decimal)}")
