'''History plugin'''
import logging
from app.commands import Command
from calculator.calculations import Calculations

class ShowHistoryCommand(Command):
    '''Add ShowHistory command class'''
    def execute(self,a,b): 
        '''being called from CommandHandler to execute the function'''
        history = Calculations.get_history()
        if not history: 
            logging.info("No history available in memory")
            print("No history available to show, start adding calculations.")
        else:
            print("History of the calculations from memory:")
            logging.info("Printing calculation history from memory")
            for row in history:
                calculation, result = row
                print(f"{calculation}, Result: {result:.2f}")
