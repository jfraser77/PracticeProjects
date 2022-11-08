"""
Name: Joe Fraser
Date: 10/11/22
Description: Multiplication tables
"""



def main():
    print("\t\t\t\tMultiplication Tables\n")
    for i in range(1, 13):
        print(i, end="\t")
    print()
    print("____________________________________________________________________________________________\n")

    for j in range(1,13):
        for k in range(1,13):
            print(j * k, end="\t")
    print("\n")



if __name__ == "__main__":
    main()