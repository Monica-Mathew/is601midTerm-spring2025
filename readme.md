# Project Overview
This project implements a command line interface mode for Calculator with dynamic plugin support, history management in both memory and on disk, logging, and Pandas library for data handling. The CLI interface is based on REPL (Read Eval Print Loop), and supports operations like add, subtract, multiply, divide.

# Project Install Instructions

## Install

1. git clone https://github.com/Monica-Mathew/is601midTerm-spring2025.git

## Activate virtual environment

1. source venv/bin/activate
2. pip3 install -r requirements.txt
3. pip3 freeze > requirements.txt 

## Set up environment variables
1. Create a `.env` file in the root directory of the project and add the following variables:
DATA_DIRECTORY=./data FILE_NAME=calculations.csv LOGGING_CONF_PATH=logging.conf ENVIRONMENT=DEVELOPMENT

2. Otherwise, variables can be directly exported in  terminal using below commands:
    ```bash
    export DATA_DIRECTORY=./data
    export FILE_NAME=calculations.csv
    export LOGGING_CONF_PATH=logging.conf
    export ENVIRONMENT=DEVELOPMENT

# Run the file

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
 ```2025-03-16 19:45:20,412 - root - INFO - Add command function invoked The result of 3 add 5 is equal to 8```

# Design Patterns Used
### Facade Pattern
### Command Pattern
### Factory Method Pattern
### Singleton Pattern

# Testing
1. pytest
2. pytest --pylint 
3. pytest --pylint --cov
4. pytest --num_records=100
5. pytest --cov=. --cov-report=html (To see the coverage report line by line)