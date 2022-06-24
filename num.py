# Project: Num Quiz 2 Self-Assessment
# Author: Joe Fraser
# Date: 6/23/2022
# Description: asks the user for their name and their favorite number as input and outputs

import math


def main():
    # Phrases for user input variables
    name_phrase = "Please enter your name: "
    number_phrase = "Please enter your favorite number:  "

    # User inputs for Name and favorite number
    name_input = input(name_phrase)
    number_input = input(number_phrase)
    
    # Convert string number variable into number value
    number_value = eval(number_input)

    # Prints Name, Decimal, Count 1's, Factorial, Log base 5
    name = name_input.capitalize() + "'s Number"
    print(name.center(80))
    print(f"Is decimal?", number_input.isdecimal())
    print("How many 1's?", number_input.count("1"))
    print("Factorial: ", math.factorial(round(abs(number_value), 0)))
    print("Log base 5: ", math.log(abs(number_value), 5))




if __name__ == '__main__':
    main()