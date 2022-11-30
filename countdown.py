"""
Name: Joe Fraser
Date: 11/15/22
Description: Countdown with recursion
"""

def countdown(num):
    if num == 0:
        print("done!")
        return
    else:
        print(num, "...")
        countdown(num-1)

def main():
    countdown(20)


if __name__ == "__main__":
    main()