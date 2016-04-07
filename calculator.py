"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def prefix_calculator(split_line):
    """Main function. Calls all arithmetic functions 
    based on user input.
    """
    for i in range(len(split_line) - 1):
        split_line[i+1] = int(split_line[i+1])

    if split_line[0] == '+':
        print add(split_line[1], split_line[2])

    elif split_line[0] == '-':
        print subtract(split_line[1], split_line[2])

    elif split_line[0] == '*':
        print multiply(split_line[1], split_line[2])

    elif split_line[0] == '/':
        print divide(split_line[1], split_line[2])

    elif split_line[0] == 'square':
        print square(split_line[1])

    elif split_line[0] == 'cube':
        print cube(split_line[1])

    elif split_line[0] == 'pow':
        print power(split_line[1], split_line[2])

    elif split_line[0] == 'mod':
        print mod(split_line[1], split_line[2])

while True:
    user_input = raw_input("Enter prefix equation: ")
    split_line = user_input.split(' ')

    if user_input.lower() == 'q':
        break

    prefix_calculator(split_line)