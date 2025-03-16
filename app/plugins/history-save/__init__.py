'''History plugin'''
import logging
from app.commands import Command
from calculator.calculations import Calculations

class SaveHistoryCommand(Command):
    '''Add SaveHistory command class'''
    def execute(self,a,b): 
        '''being called from CommandHandler to execute the function'''
        logging.info('Adding calculation history to csv')
        Calculations.add_calculation_to_history_csv()
