

from decimal import Decimal
from typing import Callable


class Calculation: # Calculation class is used to create a instance of the calculation, which can be later stored
    def __init__(self,a,b,operation):
        self.a = a
        self.b=b
        self.operation=operation

    def performOperation(self) -> Decimal:
        return self.operation(self.a,self.b)
    
    @staticmethod
    def create(a:Decimal, b:Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(a, b, operation)
    
    def __repr__(self):
        return f"Calcualtion of {self.a} and {self.b} with {self.operation.__name__}"
