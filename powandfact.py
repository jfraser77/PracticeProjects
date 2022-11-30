"""
Name: Joe Fraser
Date: 11/15/22
Description: Recursion on power and factorial
"""
import calendar

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def g(n):
    print(f"{n}...")
    if n == 0:
        return
    else:
        g(n-1)

def h(n):
    if n == 0:
        return
    else:
        h(n - 1)
    print(f"{n}...")

def f(n):
    if n <= 1:
        return 1
    else:
        return n ** f(n - 1)

def c(s):
    x = 0
    if len(s) == 0:
        return x
    elif s[0] == '8':
        x = 1
    return x + c(s[1:len(s)])

def reverse(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse(s[:-1])

def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)

def multiply(n):
    if n == 1:
        return 1
    return n * multiply(n - 1)

def main():
#    print(g(10))
#    print(h(10))
#    print(f(3))
#    print(c('34876818'))
#    print(reverse("Happy Friday!"))
#    print(sum(9))
    print(multiply(4))

if __name__ == "__main__":
    main()



    """     print("{} to the power of {} is {}". format(5, 3, power(5,3)))
    print("{} to the power of {} is {}". format(1, 5, power(1,5)))
    print("{}! is {}".format(4, factorial(4)))
    print("{}! is {}".format(0, factorial(0)))

    print()
    print()


    cal = calendar.month(2019, 7)
    print(cal) """