# Project: Mad
# Author: Joe Fraser
# Date: 6/23/2022
# Description: program mad.py that asks the user to enter a phrase, and then prints out phrase.

x = "Enter a phrase. "

user_phrase = input(x)

print("Mad version of phrase: ",user_phrase.upper())

print("Confused version of phrase: ",user_phrase.replace("e", "x"))

print("Maddest version of all phrases: ", str(user_phrase.isprintable()))