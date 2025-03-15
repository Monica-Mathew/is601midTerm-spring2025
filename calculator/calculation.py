'''Calculation file'''
from decimal import Decimal
from typing import Callable

class Calculation: # Calculation class is used to create a instance of the calculation, which can be later stored
    '''Calculation class'''
    def __init__(self,a,b,operation):
        self.a = a
        self.b=b
        self.operation=operation

    def performOperation(self) -> Decimal:
        '''perform the stored calculation and return the result'''
        return self.operation(self.a,self.b)
    
    @staticmethod
    def create(a:Decimal, b:Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        '''static method to create, not using factory method to create instance of the class'''
        return Calculation(a, b, operation)
    
    def __repr__(self):
        '''return simplified representaion of calculation'''
        return f"Calcualtion of {self.a} and {self.b} with {self.operation.__name__}"
