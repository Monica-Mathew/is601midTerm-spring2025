'''Command line file'''
from abc import ABC, abstractmethod

class Command(ABC):
    '''Command class method '''
    @abstractmethod
    def execute(self,a,b):
        '''execute method'''
        pass # pylint: disable=unnecessary-pass

class CommandHandler:
    '''Command Handler class'''
    def __init__(self):
        '''initalizing the commands'''
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        '''registering the commands with command handler'''
        self.commands[command_name] = command

    def execute_command(self, command_name: str,num1, num2):
        '''function to execute based on the command name'''
        try:
            command = self.commands[command_name]
            command.execute(num1, num2)
        except KeyError:
            print(f"No such command: {command_name}")
