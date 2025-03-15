'''App file'''
import importlib
import sys
import pkgutil
import multiprocessing
from app.commands import CommandHandler
from app.commands import Command

class App:
    '''init def'''
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
    
    # def run_in_process(self, target, *args): 
    #     '''multiprocessing'''
    #     process = multiprocessing.Process(target=target, args=args)
    #     process.start()
    #     process.join()  

    def load_plugins(self):
        '''loading plugins dynamically'''
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        '''start of the program execution'''
        self.load_plugins()

        print("Type 'exit' to exit, 'menu' to see list of operations")
        while True:  #REPL Read, Evaluate, Print, Loop

            command_line_input = input(">>> ").strip()
            if command_line_input == 'exit':
                print("Exiting Command line")
                sys.exit(1)
            if command_line_input == 'menu':
                print("Printing Menu")
                for command in self.command_handler.commands:
                    print(f"- {command}\n")
                continue
            if(len(command_line_input.split())) != 3:
                print("Usage : <number1> <number2> <operation>")
                continue
            
            num1, num2, operation = command_line_input.split()
            self.command_handler.execute_command(operation, num1, num2)
            # self.run_in_process(self.command_handler.execute_command, operation, num1,num2)
