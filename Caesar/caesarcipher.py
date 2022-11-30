"""
Name: Joe Fraser
Date: 11/9/22
Description: Ceasar cipher to code and decode string
"""
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encrypt_phrase = "The encoded text is {pass}"

decrypt_phrase = "The decrypted text is {pass}"

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"The {cipher_direction}d text is {end_text}")
           


def main():
    should_continue = True
    while should_continue:
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") 
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        continue_program = input("Do you want to restart ciphar program?\n Type 'yes' to go again. Otherwise type 'no'\n")
        if continue_program.lower() == 'no':
            should_continue = False
            print("Goodbye")
        


if __name__ == "__main__":
    main()