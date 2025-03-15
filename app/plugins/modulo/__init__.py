'''Modulo plugin'''
from decimal import Decimal
from app.commands import Command

class ModuloCommand(Command): # testing out dynamic plugin
    '''Modulo command class'''
    def execute(self,a,b):
        '''being called from CommandHandler to execute the function'''
        a_decimal, b_decimal = map(Decimal, [a,b])
        print(f"The result of {a_decimal} modulo {b_decimal} is equal to {a_decimal % b_decimal}")
