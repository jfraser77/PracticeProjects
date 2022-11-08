""" 
Name: Joe fraser 
Description: Incantation program demonstrates string concactenation
"""

def spook(num):
    s = 'o' * num


    return "sp" + s + "ky"

def main():
    s = eval(input("Enter an integer for incantation level!...\n"))

    print(spook(s))

if __name__ == '__main__':
    main()