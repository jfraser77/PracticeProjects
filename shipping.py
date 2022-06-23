# Project: Shipping
# Author: Joe Fraser
# Date: 6/22/2022
# Description: 

def main():
    weight = float(input("Enter weight >>>> "))

    cost = ""
    
    # Ground Shipping
    
    if weight <= 2:
        cost = weight * 1.50 + 20
    elif 2 > weight <= 6:
        cost = weight * 3.00 + 20
    elif 6 < weight <= 10:
        cost = weight * 4.00 + 20
    else: 
        cost = weight * 4.75 + 20

    premium_cost = float(cost + (125.00 - 20))

    print(f"Ground Shipping cost is taxes and small flat charge plus a rate based on the weight of your package ${cost}" )
    print(f"Ground Premium Shipping which is a higher flat charge but no charge for weight is ${premium_cost}")

    # Drone Shipping

    drone_cost = ""

    if weight <= 2:
        drone_cost = weight * 4.50
    elif 2 < weight <= 6:
        drone_cost = weight * 9
    elif 6 < weight <= 10:
        drone_cost = weight * 12
    elif 10 < weight:
        drone_cost = weight * 14.25

if __name__ == "__main__":
    main()