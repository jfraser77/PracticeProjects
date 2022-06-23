# Project: Maths
# Author: Joe Fraser
# Date: 6/23/2022
# Description: takes a number as input from the user and prints out function result.

import math

x = "Enter number: "

user_number = float(input(x))

print("Absolute value of your number: ", abs(user_number))

print("Floor of number: ", math.floor(user_number))

print("Round number to 2 decimal places: ", round(user_number, 2))