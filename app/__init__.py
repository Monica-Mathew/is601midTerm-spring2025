'''App file'''
import importlib
import logging
import os
import sys
import pkgutil
import logging.config
from app.commands import CommandHandler
from app.commands import Command
from dotenv import load_dotenv

class App:
    '''App class'''
    _instance = None  # Class level variable for singleton instance
    def __new__(cls):
        if cls._instance is None:  
            cls._instance = super(App, cls).__new__(cls)
        return cls._instance #return the same instance
    
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        load_dotenv() #loads from .env file contents
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'TESTING') # sets default only if it is missing, right now in .env I have it as DEVELOPMENT
        self.configure_logging()
        self.command_handler = CommandHandler()
    
    def configure_logging(self):
        logging_conf_path = self.get_environment_variable('LOGGING_CONF_PATH')
        try:
           logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        except Exception as e:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
            logging.error(f"Logging configuration failed: {e}, falling back to basicConfig.")
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings
    
    def get_environment_variable(self, envVar: str ='ENVIRONMENT'):
        logging.info("Fetching environment variable")
        return self.settings[envVar]

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
        logging.info("Application started. Type 'exit' to exit.")
        print("Type 'exit' to exit, 'menu' to see list of operations")
        while True:  #REPL Read, Evaluate, Print, Loop

            command_line_input = input(">>> ").strip()
            if command_line_input == 'exit':
                logging.info("Application exited using 'exit' command")
                print("Exiting Command line")
                sys.exit(1)
            if command_line_input == 'menu':
                logging.info("Menu Command used")
                print("Printing Menu")
                for command in self.command_handler.commands:
                    print(f"- {command}\n")
                continue 
            if(len(command_line_input.split()) == 1 and command_line_input.split()[0].startswith("history")):
                logging.info(f"History opertaion invoked, executing - {command_line_input.split()[0]}")
                self.command_handler.execute_command(command_line_input.split()[0])
                continue
            if(len(command_line_input.split())) != 3:
                logging.warning("Application usage incorrect")
                print("Usage : <number1> <number2> <operation>")
                continue
            
            num1, num2, operation = command_line_input.split()
            self.command_handler.execute_command(operation, num1, num2)
