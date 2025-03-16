'''History plugin'''
from app.commands import Command
from calculator.calculations import Calculations

class LoadHistoryCommand(Command):
    '''Add LoadHistory command class'''
    def execute(self,a,b): 
        '''being called from CommandHandler to execute the function'''
        history = Calculations.get_history_csv()
        if history is None or history.empty: 
            print("No history available to show.")
        else:
            print("History of the calculations:")
            for index, row in history.iterrows(): # pylint: disable =unused-variable
                print(f"{row['num1']} {row['operation']} {row['num2']} = {row['result']}")
