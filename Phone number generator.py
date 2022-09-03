import random


def generator(n):
    # initialize empty list to append numbers
    numbers = []
    # initialize variable to concatinate number
    number = ""
    for i in range(n):
        # generating the starting number
        number += str(random.randint(6, 9))
        # running the loop to generate rest 9 numbers
        for j in range(9):
            num = random.randint(0, 9)
            # concatinating new number to old one
            number += str(num)
        # finally append 10 digit number to numbers array
        numbers.append(number)
        # empty number variable to add new one
        number = ""
    return numbers


if __name__ == "__main__":
    run = True
    while run:
        try:
            num = int(input("Enter how many numbers you want to generate : "))
            for i in generator(num):
                print(i)

            run = False
            input()

        except Exception as e:
            print("Invalid Input")

