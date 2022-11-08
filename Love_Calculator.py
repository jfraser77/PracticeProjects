"""
Name: Joe Fraser
Date: 10/4/22
Description: Love Calculator 
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count1 = 0
count2 = 0

for letter in "true":
    count1 += name1.lower().count(letter)
    count1 += name2.lower().count(letter)
for letter in "love":
    count2 += name1.lower().count(letter)
    count2 += name2.lower().count(letter)

count_true = str(count1)
count_love = str(count2)

true_love = count_true + count_love

total_count = int(true_love)

if 10 > total_count or total_count > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif 40 < total_count < 50:
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}.")