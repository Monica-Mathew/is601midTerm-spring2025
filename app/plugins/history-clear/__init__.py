'''Clear History plugin'''
from app.commands import Command
from calculator.calculations import Calculations

class LoadHistoryCommand(Command):
    '''Add ClearHistory command class'''
    def execute(self,a,b): 
        '''being called from CommandHandler to execute the function'''
        Calculations.clear_history_csv()
        
