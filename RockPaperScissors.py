import random


PlayerScore = 0
ComputerScore = 0
Player2Score = 0
options = ["rock","paper","scissors"]
#i have no idea why i thought 2 player local rock paper scissors made any sense but i did it anyway
TwoPlayer = input("Do you want it to be two player? Y/N").upper()


while True:
    PlayerUses = input("Rock/Paper/Scissors, Press E to exit").lower()
    Play2Uses = input("Rock/Paper/Scissors, Press E to exit").lower()
    if PlayerUses or Play2Uses  == "e":
        break
    
    if PlayerUses or Play2Uses not in options:
        print("Option is not valid, ensure what you put is correct")
        continue


    if TwoPlayer == "N":
        RandomNumber = random.randint(1,3)
        ComputerUses = options[RandomNumber]
        print(f"Computer picked {ComputerUses} You picked {PlayerUses}")

        if PlayerUses == "rock" and ComputerUses == "scissors":
             print("You win!")
             PlayerScore += 1
        
        elif PlayerUses == "paper" and ComputerUses == "rock":
             print("You win!")
             PlayerScore += 1
        
        elif PlayerUses == "scissors" and ComputerUses == "paper":
             print("You win!")
             PlayerScore += 1
        else:
             print("You lost!")
             ComputerScore += 1    
    if TwoPlayer == "Y":
        print(f"Player 2 chose {Play2Uses} You picked {PlayerUses}")

        if PlayerUses == "rock" and Play2Uses == "scissors":
             print("Player 1 wins!")
             PlayerScore += 1
        
        elif PlayerUses == "paper" and Play2Uses == "rock":
             print("Player 1 wins!")
             PlayerScore += 1
        
        elif PlayerUses == "scissors" and Play2Uses == "paper":
             print("Player 1 wins!")
             PlayerScore += 1
        else:
             print("Player 2 Won!")
             Player2Score += 1    

if TwoPlayer == "N":
    print(f"The overall score was: {PlayerScore} against {ComputerScore}")
    if PlayerScore > ComputerScore:
        print("You win!!")
    else:
        print("You lost! Better luck next time")
else:
    print(f"The overall score was player 1 with: {PlayerScore} against player 2 with: {Player2Score}")
    if PlayerScore > Player2Score:
        print("Player 1 wins!!")
    else:
        print("Player 2 wins!!")
