# Project: Sum10 Module 3 Learning Exercise
# Author: Joe Fraser
# Date: 6/24/2022
# Description: Create a program sum10.py that calculates and prints the sum of 10 real (i.e., decimal) numbers entered by the user. Make sure you ask (i.e., prompt) the user to enter each number (the user will hit enter after each number). 


def main():
    phrase1 = "Enter 10 decimals to sum total: "
    sum_user = 0

    for i in range(10):
        sum_user += eval(input(phrase1))

    print("Sum total: ", sum_user)
if __name__ == "__main__":
    main()