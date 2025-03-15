

from decimal import Decimal
from typing import Callable
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:
    @staticmethod
    def _perform_operaration(a:Decimal, b:Decimal, operation: Callable[[Decimal, Decimal], Decimal]): # internal method to class
        calculation = Calculation.create(a,b,operation)
        Calculations.add_calculation_to_history(calculation)
        return calculation.performOperation()

    @staticmethod
    def addOperation(a:Decimal,b:Decimal) -> Decimal:
        return Calculator._perform_operaration(a,b,add)

    @staticmethod
    def subtractOpertiona(a:Decimal,b:Decimal) -> Decimal:
        return Calculator._perform_operaration(a,b,subtract)
    
    @staticmethod
    def multiplyOperation(a:Decimal,b:Decimal) -> Decimal:
        return Calculator._perform_operaration(a,b,multiply)
    
    @staticmethod
    def divideOperation(a:Decimal,b:Decimal) -> Decimal:
        return Calculator._perform_operaration(a,b,divide)