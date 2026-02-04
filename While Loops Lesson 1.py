CorrectInput = True

while CorrectInput == False:
    ChosenNumber = int(input("enter a number from 1 - 100"))
    if ChosenNumber > 100 or ChosenNumber <1:
        print("Retry, ensure your input if between 1 and 100")
    else:
        CorrectInput = True
print(ChosenNumber)


MusicListDict = [
    {"Genre1": "Musician1", "Groups": "Groups"}
    {"Genre2": "Muscician2", "Groups2" "Groups2"}
]
