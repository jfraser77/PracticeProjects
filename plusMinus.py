"""
Name: Joe Fraser
Date: 11/8/22
Description: Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.
"""

def plusMinus(arr):
    # Write your code here
    number_prop = len(arr)
    positive_prop = 0
    negative_prop = 0
    zero_prop = 0
    
    for number in arr:
        if number == 0:
            zero_prop += 1
        elif number < 0:
            negative_prop += 1
        elif number > 0:
            positive_prop += 1
            
    positive = positive_prop/number_prop
    negative = negative_prop/number_prop
    zero = zero_prop/number_prop

    print(f"{positive:.6f}")
    print(f"{negative:.6f}")
    print(f"{zero:.6f}")
            
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
