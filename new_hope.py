""" 
Name: Joe Fraser
Description: 
"""



def main():
    user_input = eval(input())

    if user_input == 1:
        print("A long time ago in a galaxy far away...")
    else:
        user_input = user_input - 1
        print("A long time ago in a galaxy " + "far, " * user_input + "far away..." )


if __name__ == '__main__':
    main()
    