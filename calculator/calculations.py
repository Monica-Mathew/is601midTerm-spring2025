from typing import List
from calculator.calculation import Calculation

class Calcualtions:
    history: List[Calculation] =[] # history object to store list of calculations.

    @classmethod # adding as a classmethod to bind to the class itself to have it shared across all instances of clas
    def add_calculation_to_history(cls, calculation:Calculation):
        '''add a new calculation to the history'''
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        '''get the history of calculation'''
        return cls.history # we are accessing the variable through the method
    
    @classmethod
    def clear_history(cls):
        '''Clear the history of calculation'''
        cls.history.clear()
    
    @classmethod
    def get_latest(cls) -> Calculation:
        '''gets latest calculation'''
        if cls.history:
            return cls.history[-1];
        return None
    
    @classmethod
    def find_by_operation(cls, operation_name: str) -> Calculation:
        '''add a new calculation to the history'''
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]


