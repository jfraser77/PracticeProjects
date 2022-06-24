# Project: Madfun
# Author: Joe Fraser
# Date: 6/23/2022
# Description: takes a decimal number as input from the user and prints out 

import math
from math import sqrt

def main():
    phrase1 = "Please enter a number: "

    user_input = eval(input(phrase1))

    # Print out to terminal Absolute, Rounded Number, and Square Root of rounded number Absolute value.
    print(f"Absolute value of number inputed: {abs(user_input)}")
    print(f"Round number to 0 decimal places: {round(user_input, 0)}")
    print(f"Square root of rounded number: {sqrt(abs(round(user_input)))}")


if __name__ == '__main__':
    main()