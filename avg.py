#Create a program avg.py that calculates and prints the average of 10 real (i.e., decimal) numbers entered by the user. Make sure you ask (i.e., prompt) the user to enter each number (the user will hit enter after each number). 




def main():
    phrase1 = "Enter 10 Decimal numbers to return average: "
    user_numbers = 0
    for i in range(10):
        user_numbers += eval(input(phrase1))

    print("Averaged numbers: ", user_numbers/10)



if __name__ == '__main__':
    main()