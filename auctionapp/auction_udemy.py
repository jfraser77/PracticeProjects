"""
Name: Joe Fraser
Date: 12/20/22
Description: Day 9 - Secret Auction Program
"""

from art import logo
import os

welcome_msg = "Welcome to the secret auction program."
name_question = "What is your name?: "
bid_question = "What's your bid?: "
more_users_check = "Are there any other bidders? Type 'yes' or 'no'.\n"


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

def main():
    print(logo)
    print(welcome_msg)

    bid_on = False
    my_dict = {}

    while not bid_on:
        name_bid = input(name_question) 
        user_bid = input(bid_question)
        convert_bid = int(user_bid.strip('$'))
        my_dict[name_bid] = convert_bid
        add_bidders = input(more_users_check)

        if add_bidders.lower() == "no":
            bid_on = True
            find_highest_bidder(my_dict)
        else:
            os.system('cls')
    
    


if __name__ == "__main__":
    main()