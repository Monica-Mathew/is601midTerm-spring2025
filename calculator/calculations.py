'''Calculations file'''
import logging
import os
from typing import List
import pandas as pd
from app import App 
from calculator.calculation import Calculation
import atexit

class Calculations:
    '''Calculations class'''
    history: List[Calculation] =[] # history object to store list of calculations in memory.

    @classmethod # adding as a classmethod to bind to the class itself to have it shared across all instances of clas
    def add_calculation_to_history(cls, calculation:Calculation,result):
        '''add a new calculation to the history'''
        cls.history.append((calculation,result))

    @classmethod
    def get_history(cls):
        '''get the history of calculation'''
        return cls.history # we are accessing the variable through the method
    
    @classmethod
    def clear_history(cls):
        '''Clears the history of calculation from memory'''
        cls.history.clear()
    
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

    historyPd: pd.DataFrame  # history dataframe to store list of calculations in csv file.

    app_instance = App() #  Singleton pattern, the __new__ method is overridden in App class to check if an instance of the class already exists, and returns it
    data_dir = app_instance.get_environment_variable('DATA_DIRECTORY') # grabbing DATA_DIRECTORY from env
    logging.info(f"Data directory path - {data_dir}")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    file_name= app_instance.get_environment_variable('FILE_NAME') # grabbing FILE_NAME from env
    csv_file_path = os.path.join(data_dir, file_name)
    
    @classmethod
    def save_history_on_exit(cls):
        '''Save all history when the program exits'''
        for handler in logging.getLogger().handlers:
            handler.flush()
        logging.info("Saving calculation history to CSV")
        absolute_path = os.path.abspath(cls.csv_file_path)
        logging.info(f'the relative path  to save my file is {cls.csv_file_path}')
        logging.info(f'the absolute path  to save my file is {absolute_path}')
        cls.add_calculation_to_history_csv()
        logging.info("History saved to csv file successfully upon exit.")
        logging.info("Shutting down application.")
       
    @classmethod
    def add_calculation_to_history_csv(cls):
        '''Add a new calculation to the historyPd using Pandas'''
        all_calculations = []
        for calc, result in cls.history:
            new_calculation = {
                'num1': calc.a,
                'num2': calc.b,
                'operation': calc.operation.__name__,
                'result': result
            }
            all_calculations.append(new_calculation)
        cls.historyPd =  pd.DataFrame(all_calculations)
        
        if os.path.exists(cls.csv_file_path):
            cls.historyPd.to_csv(cls.csv_file_path, mode='a', header=False, index=False)
        else:
            cls.historyPd.to_csv(cls.csv_file_path, mode='w', header=True, index=False)
        cls.clear_history()
        logging.info('Clearing the current in memory history since its saved to disk')
        

    @classmethod
    def get_history_csv(cls):
        '''Get the history of calculations as a DataFrame'''
        if os.path.exists(cls.csv_file_path):
            cls.historyPd = pd.read_csv(cls.csv_file_path)
            return cls.historyPd
        logging.info("Printing out the saved history")
        return pd.DataFrame(columns=['num1', 'num2', 'operation', 'result'])
    
    @classmethod
    def delete_history_from_csv(cls):
        '''Delete the history entirely from the CSV file'''
        cls.historyPd = pd.DataFrame(columns=['num1', 'num2', 'operation', 'result'])
        try:
            cls.historyPd.to_csv(cls.csv_file_path, index=False)
            logging.info(f"History file '{cls.csv_file_path}' has been cleared.")
            print(f"History file has been cleared.")
        except:
            logging.info(f"No history file found at '{cls.csv_file_path}' to be cleared.")
            print(f"No history file to be cleared.")
atexit.register(Calculations.save_history_on_exit)

