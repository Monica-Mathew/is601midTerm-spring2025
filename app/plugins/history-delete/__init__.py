'''Delete History plugin'''
from app.commands import Command
from calculator.calculations import Calculations

class LoadHistoryCommand(Command):
    '''Add Deleteistory command class'''
    def execute(self,a,b): 
        '''being called from CommandHandler to execute the function'''
        Calculations.delete_history_from_csv()
        