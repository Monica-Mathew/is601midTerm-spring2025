'''History plugin'''
from app.commands import Command
from calculator.calculations import Calculations

class ShowHistoryCommand(Command):
    '''Add ShowHistory command class'''
    def execute(self,a,b): 
        '''being called from CommandHandler to execute the function'''
        history = Calculations.get_history()
        if not history: 
            print("No history available to show.")
        else:
            print("History of the calculations:")
            for calculation in history:
                print(f"- {calculation}")
