import json as jason

#Enter Login and password
#Email
#Create bookings, date, name, viewing add information to animals
#hold information about all animals
import json as jason

# File 
fileZoo = "ZooDataBase.json"

# Lists to hold animals 
with open(fileZoo, "r", encoding="utf-8") as file:
    animals = jason.load(file["animals"]["animalsSpecies"])

zooAnimals = [animals]

def login():
    createNewAcc = input("Do you already have an account created? Y/N: ").upper()
    with open(fileZoo, "r", encoding="utf-8") as file:
        data = jason.load(file)

    if createNewAcc == "N":
        try:
            newEmailAcc = input("Enter the email for your account: ")
            newUserAcc = input("Enter the user for your account: ")
            newPasswordAcc = input("Enter the password for your account: ")
            if newUserAcc in data.get("accounts", {}):
                print("Username taken, please try again.")
            elif any(newEmailAcc == info.get("email") for info in data.get("accounts", {}).values()):
                print("Email is already in use, please try again.")
        except:
            print("please try again")
        else:
            if "accounts" not in data:
                data["accounts"] = {}
            data["accounts"][newUserAcc] = newPasswordAcc
            with open(fileZoo, "w", encoding="utf-8") as file:
                jason.dump(data, file, indent=4)
                print("Account created!, Access Granted.")
                return True

    else:
        try:
            existingUserAcc = input("Enter your username: ")
            existingPassAcc = input("Enter your password: ")
            if existingUserAcc in data.get("accounts", {}):  # Username inside json file
                if data["accounts"][existingUserAcc] == existingPassAcc:  # password inside json file
                    print("Access Granted")
                    return True
                else:
                    print("Password did not match username.")
            else:
                print("Username could not be found.")
        except:
            print("Please try again.")

def updateAnimals():
    pass  # Placeholder 

# Run the login function
login()


#next:
# Maybe remove login from the class(?)
# Create a table for all animal species in zoo
# Each species will have a generalised overview of the animal aswell as dates that animal can be visitted 
# create a bookings system, check what dates are good, which are taken
