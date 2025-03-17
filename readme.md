# Project Overview
This project implements a command line interface mode for Calculator with dynamic plugin support, history management in both memory and on disk, logging, and Pandas library for data handling. The CLI interface is based on REPL (Read Eval Print Loop), and supports operations like add, subtract, multiply, divide.

# Project Install Instructions

## Install

1. ```git clone https://github.com/Monica-Mathew/is601midTerm-spring2025.git```

## Activate virtual environment

1. source venv/bin/activate
2. pip3 install -r requirements.txt
3. pip3 freeze > requirements.txt 

## Set up environment variables
1. Create a `.env` file in the root directory of the project and add the following variables:
DATA_DIRECTORY=./data 
FILE_NAME=calculations.csv 
LOGGING_CONF_PATH=logging.conf 
ENVIRONMENT=DEVELOPMENT

2. Otherwise, variables can be directly exported in bash terminal using below commands:
    ```bash
    export DATA_DIRECTORY=./data
    export FILE_NAME=calculations.csv
    export LOGGING_CONF_PATH=logging.conf
    export ENVIRONMENT=DEVELOPMENT

# Run the program

1. python main.py
On the prompt, user can enter menu to see list of operations

## Available Operations

- **add**: Addition of numbers
- **divide**: Division of numbers
- **history-clear**: Clearing the in-memory history of calculations
- **history-delete**: Deleting the history of calculations from file
- **history-load**: Loading the history of calculations from file
- **history-save**: Saving the history of calculations to the file
- **history-show**: Showing the in-memory history of calculations
- **modulo**: Modulo of two numbers
- **multiply**: Multiplication of two numbers
- **subtract**: Subtraction of two numbers

## Example Usage
 ```3 5 add```
 ### Output:
 ```2025-03-16 19:45:20,412 - root - INFO - Add command function invoked```
    ```The result of 3 add 5 is equal to 8```


# Design Patterns Used

### Facade Pattern
Each plugin Implementation the user interaction is a facade class  -  which invokes appropiate methods from Calculations class.
Calculations class simplified the interface to interact with Pandas calculation history and data file handlling.
The `Calculation` class and its methods manage the history of calculations (e.g., `add_calculation_to_history()`, `save_history_on_exit()`, `get_history_csv()`) without having to worry about saving/loading them to/from a CSV file. 
[calculations.py file on GitHub](https://github.com/Monica-Mathew/is601midTerm-spring2025/blob/main/calculator/calculations.py)

### Command Pattern
The Command class acts as an abstract base for all  commands, and CommandHandler registers and executes the commands. In the REPL (Read-Eval-Print Loop), the user provides input that corresponds to specific commands. The CommandHandler captures provided input, and invokes and executes the respective command accordingly.
[commands __init__.py file on GitHub](https://github.com/Monica-Mathew/is601midTerm-spring2025/blob/main/app/commands/__init__.py)

### Factory Method Pattern
The create() in Calculation class is  a Factory Method because it allows  to create Calculation objects without directly instantiating the class using the constructor. This fucntion offers future flexibility to adjust how Calculation objects are created.
 [calculation.py file on GitHub](https://github.com/Monica-Mathew/is601midTerm-spring2025/blob/main/calculator/calculation.py#L17)

### Singleton Pattern
The Singleton pattern ensures that only one instance of the app class exists throughout the program. This __new__ method is called before __init__, which is used for initializing the instance and check if an instance of the class already exists. If instance is present, we return the existing instance, hence mainiting one global instance of App class.
By having only one instance, the Singleton pattern ensures consistent behavior across the application, as all parts of the program are working with the same app instance ,and dont have multiple initialization of app object
[app __init__.py file on GitHub](https://github.com/Monica-Mathew/is601midTerm-spring2025/blob/main/app/__init__.py#L15)
[Singleton pattern app instance in Calculations.py file on GitHub](https://github.com/Monica-Mathew/is601midTerm-spring2025/blob/main/calculator/calculations.py#L43)

# Environment Variables Usage
In application, environment variables are used to manage configuration in a secure way. The values are retreived during run time rather than hard coded in the code.
eg: the ```DATA_DIRECTORY``` path holds the location for adding the csv file which holds the calculation history.
This is fetched by ```get_environment_variable``` function from the app file.
[environment variable DATA_DIRECTORY ](https://github.com/Monica-Mathew/is601midTerm-spring2025/blob/main/calculator/calculations.py#L44)
In github, to run the tests, I have added these variables to GitHub secrets and variables section, so during the github action workflow, these values would be picked.
[Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)

# Logging 
Application has comprehensive logging system to record the detailed application operations, data manipulations, errors, and informational messages. Logging config file is present to configure the logging system, and it is stored in logs folder.
Informational logs - [logging.info code example](https://github.com/Monica-Mathew/is601midTerm-spring2025/blob/main/calculator/calculations.py#L59)
Warning logs - [logging.warning code example](https://github.com/Monica-Mathew/is601midTerm-spring2025/blob/main/app/__init__.py#L84)
Error logs - [logging.error code example](https://github.com/Monica-Mathew/is601midTerm-spring2025/blob/main/calculator/operations.py#L25)

# Error Handling and Exceptions
Application uses both LBYL and EAFP approach for error handling and to avoid potential errors
LBYL (Look Before You Leap): We avoid errors by checking conditions beforehand (no need for try/catch), mainly by using conditional logic
eg: [LBYL if condtiion code example](https://github.com/Monica-Mathew/is601midTerm-spring2025/blob/main/calculator/calculations.py#L79). Here we check if file exists before we write to it in append mode, otherwise new file would be created in else logic, avoiding any unwanted overwriting or unexpected behavior.
EAFP (Easier to Ask for Forgiveness than Permission): This approach asumes that operations will succeed and errors are handled on the fly if it occurs.
eg: [EAFP try except code example](https://github.com/Monica-Mathew/is601midTerm-spring2025/blob/main/app/commands/__init__.py#L28). Here we first tries to execute the command operation, and if the command specified is not present, except block catches this error gracefully and prints user-friendly message to user.


# Testing
1. pytest
2. pytest --pylint 
3. pytest --pylint --cov
4. pytest --num_records=100
5. pytest --cov=. --cov-report=html (To see the coverage report line by line)