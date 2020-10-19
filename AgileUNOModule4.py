#Your Name
#Module 4 Assignment

from sys import exit
from random import randint

myData = {}
guesses = 0
wins = 0

with open("questions.txt", "r") as infile:
    questions = infile.readlines()
    for question in questions:
        if "first" in question:
            myData["first_name"] = input(question)
        elif "last" in question:
            myData["last_name"] = input(question)
        else: print("bad question in input")
        exit()

for play in range(10)
    number = randint(0, 100)
    solved = False
    while not solved:
        guess = int(input(f"Guess a number from o to 100 :"))
        guesses += 1
        if guess == number:
            print(f"Great Job {myData["first_name"], your guess of {guess} is correct!!!")
            wins += 1
            solved = True
            break
        if guess != number:
            print(f"Your guess of {guess} is incorrect!")

        if guess > number:
            print(f"Sorry, you guessed too high!!")
        elif guess < number:
            print(f"Sorry, you guessed too low!!")
        else:
            pass

        if solved:
            print(f"Lets play agin, you have complicated {wins} out of 10 plays.")
            continue

    print(f"{myData["first_name]} {myData["last_name]} guessed the correct number {wins} out of 10 plays.")
    print(f"It took {myData["first_name]} {myData["last_name]}{guesses} guesses to do this!")
    exit()