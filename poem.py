# Project: Poem
# Author: Joe Fraser
# Date: 6/23/2022
# Description: asks the user for 2 parts of speech as input (a plural noun and an adjective) and outputs


def main():
    phrase1 = "Fill in a plural noun: "
    phrase2 = "Fill in an adjective: "

    # User inputs
    input_plural = str(input(phrase1))
    input_adjective = str(input(phrase2))

    print(f"{input_plural.title()} are red, violets are blue Monty Python is {input_adjective.lower()}, woo hoo!")

if __name__ == '__main__':
    main()