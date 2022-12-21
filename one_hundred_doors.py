"""
Name: Joe Fraser
Date: 11/30/22
Description: Imagine you  have 100 doors in a row that are all initially closed. you going to make 100 passes by each of these doors. And on the first pass, you going to visit each door in sequence and toggle it state. So that means if it's closed, it becomes open. If it's open, it becomes closed. Since all the doors are initially closed, this will result in all the doors being open after the first pass. For the second pass, you visit every second door and toggle it state. For the third pass, you visit every third door, and so on and so forth, until you only visit the 100th on the 100th pass. And the question is which doors are open at the end of this process.
"""

# Represents a list of 100 doors
doors = [False] * 101


def main():
    for i in range(1, 11, 2):
        print(i)


"""     print(doors)

    for i in range(1, 101):
        doors[i] = not doors[i]

    print(doors)

    for i in range(1, 6):
        for j in range(1, 4):
            print("i:", i, "j:", j)
 """


if __name__ == "__main__":
    main()