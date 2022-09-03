# rock papper scissor game
# date:23:02:2021
# author :Piyush Kumar

import random

# initializing score to 0
comScore = 0
userScore = 0


# function to declare winner or looser (all game logic inside it)
def game(user, com):
    global comScore, userScore
    # comparing user and com choices
    if user == com:
        print("Tie !")
    elif user == "S":
        if com == "P":
            print("You win")
            userScore += 1
        elif com == "R":
            print("You loose")
            comScore += 1
    elif user == "P":
        if com == "S":
            print("You loose")
            comScore += 1
        elif com == "R":
            print("You Win")
            userScore += 1
    elif user == "R":
        if com == "P":
            print("You loose")
            comScore += 1
        elif com == "S":
            print("You Win")
            userScore += 1

    else:
        print("Wrong Input!")

# loop variable
i = 0

# declare options for computer to choose randomly
options = ["S", "R", "P"]

# loop for running game
while i <= 10:
    # asking user for input
    user = input("Your turn : (R) for Rock (P) for Paper and (S) for Scissor: ").capitalize()
    # pick randomly one option for com
    com = options[random.randint(0, 2)]
    print("You Choose", user)
    print("Com Choose", com)

    # calling game function to declare winner
    game(user, com)
    # increamenting variable
    i += 1

# after finishing the gameloop
print("Your Score is", userScore)
print("Computer Score is", comScore)

# declaring final winner or looser
if userScore > comScore:
    print("You are the winner!🎉🎉🎉")
elif userScore < comScore:
    print("Computer Win!")
elif userScore == comScore:
    print("Match is Tie try again!")
else:
    print("Something Went Wrong")
