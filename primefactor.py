"""
Name: Joe Fraser
Description: Program demonstrates how to find list of prime numbers
"""



def get_prime_factors(N):
    factors = list()
    divisor = 2

    while(divisor <= N):
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N//divisor
        else:
            divisor += 1 
    return factors

if __name__ == '__main__':
    prompt1 = "Please enter a number to return Prime Number List: "

    number_input = eval(input(prompt1))

    print(get_prime_factors(number_input))