'''Clear History plugin'''
import logging
from app.commands import Command
from calculator.calculations import Calculations

class ClearHistoryCommand(Command):
    '''Add ClearHistory command class'''
    def execute(self,a,b): 
        logging.info("Clearing calculation history in memory")
        '''being called from CommandHandler to execute the function'''
        Calculations.clear_history()
        
