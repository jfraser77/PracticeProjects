# Project: Day Quiz 2 
# Author: Joe Fraser
# Date: 6/23/2022
# Description: asks the user for their favorite month and day of the month as input and outputs 

import math


def main():
    # User phrases for input variables
    phrase1 = "Please enter your favorite month: "
    phrase2 = "Enter your favorite day of the month: "

    # User input variables
    month_input = input(phrase1)
    day_input = input(phrase2)

    # Printed results
    month = month_input.capitalize() 
    print(month + " " + day_input + ", 2020")
    print("Is the month alphanumeric? ", month.isalpha())
    print("How many 2's? ", day_input.count("2"))
    # Changed string day to numerical value variable
    day_value = eval(day_input)
    print(f"Factorial: ", math.factorial(day_value))
    print(f"Log base 2: ", math.log(abs(day_value), 2))


if __name__ == '__main__':
    main()