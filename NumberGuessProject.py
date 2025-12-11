
import random

RandNum = random.randint(0,100)

attempt = 0
CorrectGuess = RandNum
Flag = False
while Flag == False:
    Guess = int(input("Enter your first guess"))
    if Guess > CorrectGuess:
        print("Too high, try again!")
        attempt = attempt + 1
    elif Guess < CorrectGuess:
        print("Too low, try again!")
        attempt = attempt + 1
    else:
        print("Correct! well done")
        print("It only took you: ", attempt, " guesses!" )
        Flag == True