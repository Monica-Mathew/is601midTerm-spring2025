'''Calculations file'''
from decimal import Decimal
import logging
import os
import pandas as pd
from calculator.calculation import Calculation

class Calculations:
    '''Calculations class'''
    # history: List[Calculation] =[] # history object to store list of calculations.

    # @classmethod # adding as a classmethod to bind to the class itself to have it shared across all instances of clas
    # def add_calculation_to_history(cls, calculation:Calculation):
    #     '''add a new calculation to the history'''
    #     cls.history.append(calculation)

    # @classmethod
    # def get_history(cls):
    #     '''get the history of calculation'''
    #     return cls.history # we are accessing the variable through the method
    
    # @classmethod
    # def clear_history(cls):
    #     '''Clear the history of calculation'''
    #     cls.history.clear()
    
    # @classmethod
    # def get_latest(cls) -> Calculation:
    #     '''gets latest calculation'''
    #     if cls.history:
    #         return cls.history[-1]
    #     return None
    
    # @classmethod
    # def find_by_operation(cls, operation_name: str) -> Calculation:
    #     '''add a new calculation to the history'''
    #     return [calc for calc in cls.history if calc.operation.__name__ == operation_name]

    historyPd: pd.DataFrame 

    data_dir =os.getenv('DATA_DIRECTORY','./data') # adding default directory
    logging.info(f"Data directory path - {data_dir}")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    file_name =os.getenv('FILE_NAME','calculations.csv') # adding default file name
    csv_file_path = os.path.join(data_dir, file_name)

    @classmethod
    def add_calculation_to_history_csv(cls, calculation: Calculation, result:Decimal):
        '''Add a new calculation to the historyPd using Pandas'''
        new_calculation = {
            'num1': calculation.a,
            'num2': calculation.b,
            'operation': calculation.operation.__name__,
            'result': result
        }
        cls.historyPd =  pd.DataFrame([new_calculation])
        
        if os.path.exists(cls.csv_file_path):
            cls.historyPd.to_csv(cls.csv_file_path, mode='a', header=False, index=False)
        else:
            cls.historyPd.to_csv(cls.csv_file_path, mode='w', header=True, index=False)
        absolute_path = os.path.abspath(cls.csv_file_path)
        logging.info(f'the relative path  to save my file is {cls.csv_file_path}')
        logging.info(f'the absolute path  to save my file is {absolute_path}')

    @classmethod
    def get_history_csv(cls):
        '''Get the history of calculations as a DataFrame'''
        if os.path.exists(cls.csv_file_path):
            cls.historyPd = pd.read_csv(cls.csv_file_path)
            return cls.historyPd
        return pd.DataFrame(columns=['num1', 'num2', 'operation', 'result'])
    
    @classmethod
    def clear_history_csv(cls):
        '''Clears the history temporarily'''
        cls.historyPd = pd.DataFrame(columns=['num1', 'num2', 'operation', 'result'])
        if os.path.exists(cls.csv_file_path):
            cls.historyPd.to_csv(cls.csv_file_path, index=False)
            print(f"History file '{cls.csv_file_path}' has been cleared.")
        else:
            print("No history file to be cleared.")

    
    @classmethod
    def delete_history_from_csv(cls):
        '''Delete the history entirely from the CSV file'''
        cls.historyPd = pd.DataFrame(columns=['num1', 'num2', 'operation', 'result'])
        if os.path.exists(cls.csv_file_path):
            os.remove(cls.csv_file_path)  
            print(f"History file '{cls.csv_file_path}' has been deleted.")
        else:
            print(f"No history file found at '{cls.csv_file_path}' to delete.")
