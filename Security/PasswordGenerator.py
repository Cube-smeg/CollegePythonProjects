import random
import string 

def createpassword(minlength, numbers=True, specialchars=True):
    letters = string.ascii_letters
    digits = string.digits
    specialcharacters = string.punctuation

    possiblecharacters = letters
    if numbers:
        possiblecharacters += digits
    if specialchars:
       possiblecharacters =+ specialchars
    
    password = " "
    meets_criteria = False
    has_special = False
    has_number = False


    while not meets_criteria or len(password) < minlength:
        NewChar = random.choice(possiblecharacters)
        password =+ NewChar
        if NewChar in digits:
            has_number = True
        elif NewChar in specialcharacters:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        elif specialchars:
            meets_criteria = meets_criteria and has_number
    return password

minlength = input("What is the minimum length of the password?: ")
numbers = input("Should it include numbers? Y/N: ").upper() == "Y"
specialchar = input("Should it include special characters? Y/N").upper() == "Y"

password = createpassword(minlength, numbers, specialchar)
print("Password Generated: ", password)