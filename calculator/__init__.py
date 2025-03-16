'''Init file for caclulator package'''
from decimal import Decimal
from typing import Callable

from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add,subtract,multiply,divide


class Calculator:
    '''Calculator init '''
    @staticmethod
    def _perform_operaration(a:Decimal, b:Decimal, operation: Callable[[Decimal, Decimal], Decimal]): # internal method to class
        '''create and perform a calcualtion, then return result'''
        calculation = Calculation.create(a,b,operation)
        # Calculations.add_calculation_to_history(calculation)
        # Calculations.add_calculation_to_history_csv(calculation)
        # return calculation.performOperation()
        result = calculation.performOperation()
        Calculations.add_calculation_to_history_csv(calculation,result)
        return result

    @staticmethod
    def add(a:Decimal,b:Decimal) -> Decimal:
        '''Method to invoke add operation'''
        return Calculator._perform_operaration(a,b,add)

    @staticmethod
    def subtract(a:Decimal,b:Decimal) -> Decimal:
        '''Method to invoke subtract operation'''
        return Calculator._perform_operaration(a,b,subtract)

    @staticmethod
    def multiply(a:Decimal,b:Decimal) -> Decimal:
        '''Method to invoke multiply operation'''
        return Calculator._perform_operaration(a,b,multiply)

    @staticmethod
    def divide(a:Decimal,b:Decimal) -> Decimal:
        '''Method to invoke divide operation'''
        return Calculator._perform_operaration(a,b,divide)
