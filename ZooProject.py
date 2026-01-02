import json as jason
from datetime import datetime 

#Enter Login and password
#Email
#Create bookings, date, name, viewing add information to animals
#hold information about all animals
import json as jason

# File 
fileZoo = "ZooDataBase.json"

# Lists to hold animals 
with open(fileZoo, "r", encoding="utf-8") as file:
    animals = jason.load(file)

zooAnimals = animals["animals"]["animalsSpecies"]

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
            elif newEmailAcc in data.get("accounts"):
                print("Email is already in use, please try again.")
        except ValueError:
            print("please try again")
        else:
            if "accounts" not in data:
                data["accounts"] = {}

            data["accounts"][newUserAcc] = newPasswordAcc
            with open(fileZoo, "w", encoding="utf-8") as file:
                jason.dump(data, file, indent=4)
                print("Account created!, Access Granted.")
                return True, newUserAcc

    else:
        try:
            existingUserAcc = input("Enter your username: ")
            existingPassAcc = input("Enter your password: ")
            if existingUserAcc in data.get("accounts", {}):
                if data["accounts"][existingUserAcc] == existingPassAcc:
                    print("Access Granted")
                    return "User", existingUserAcc
                else:
                     print("Password did not match username.")
            elif existingUserAcc in data.get("adminAccounts", {}):
                if data["adminAccounts"][existingUserAcc] == existingPassAcc:
                    print("Access granted, Admin permissions enabled.")
                    return "Admin", existingUserAcc
            else:
                print("Password did not match username.")
        except ValueError:
            print("please try again.")

def updateAnimals(whatToUpdate): #[4], [3]
    if whatToUpdate == "avalibility":
        with open(fileZoo, "r", encoding="utf-8") as file:
            data = jason.load(file)

        avalibleAnimals = data["animals"]["animalsAvalible"]
        unavalibleAnimals = data["animals"]["animalsUnavalible"]
        print(f"Currently avalible : {avalibleAnimals}")
        print(f"Currently unavalible : {unavalibleAnimals}")
        while True:
            animalToMove = input("Enter the name of the animal you wish to move: ").title()
            if animalToMove in avalibleAnimals:
                avalibleAnimals.remove(animalToMove)
                unavalibleAnimals.append(animalToMove)
                print(f"{animalToMove} has been placed into unavalible.")
                with open(fileZoo, "w", encoding="utf-8") as file:
                    jason.dump(data, file, indent=4)
                    break

            elif animalToMove in unavalibleAnimals:
                unavalibleAnimals.remove(animalToMove)
                avalibleAnimals.append(animalToMove)
                print(f"{animalToMove} has been placed into avalible.")
                with open(fileZoo, "w", encoding="utf-8") as file:
                    jason.dump(data, file, indent=4)
                    break
            else:
                print("Animal could not be found. please ensure you enter the name correctly.")
    elif whatToUpdate == "descriptions":

        with open(fileZoo, "r", encoding="utf-8") as file:
            data = jason.load(file)

        animalsDescriptions = data["animals"]["animalsSpecies"]
        print(f"""Currently stored are: 
{animalsDescriptions}
 """)
        while True:
            animalToUpdate = input("Which animal you like to update?: ").title()
            if animalToUpdate not in animalsDescriptions:
                print("Animal could not be found. please try again")
            else:
                specificAnimalDescription = data["animals"]["animalsSpecies"][animalToUpdate]

                print(f"You are editing {animalToUpdate}, currently their description is: {specificAnimalDescription}")
                newDescription = input("Enter the new description: ")
                data["animals"]["animalsSpecies"][animalToUpdate] = newDescription

                with open(fileZoo, "w", encoding="utf-8") as file:
                    jason.dump(data, file, indent=4)    
                print(f"{animalToUpdate}s description has been updated: {newDescription} ")
                break

def createBooking(username, action): #[1] #NEEDS TO ADD A WAY TO REMOVE A BOOKING
    if action == 1:
        with open(fileZoo, "r", encoding="utf-8") as file:
            bookings = jason.load(file)
        unavalibleDates = bookings["bookings"]
        while True: # finding a valid date for booking
            bookingDates = int(input("Please enter when you wish to visit [DD/MM/YYYY]: "))
            try:
                validDate = datetime.strptime(bookingDates("%d/%m/%Y"))
                if validDate in unavalibleDates:
                    raise ValueError("Day has already been taken, please select another time")
                
                print("Date validated. your booking has been created for: ", validDate.strftime("%d/%m/%Y"))
                break
            except ValueError:
                print("value error or smth")
                

        finalDate = ["bookings"][username] = validDate.date().isoformat()
        with open(fileZoo, "w", encoding="utf-8") as file:
            jason.dump(finalDate, file, indent=4 )
    else:
        #REMOVE BOOKING OPTION 
        with open(fileZoo, "w", encoding="utf-8") as file:
            data = jason.load(file)
        while True:
            bookingToRemove = input("Enter the username of the booking to remove.")
            if bookingToRemove in data["bookings"]:
                dateToBooking = input("Enter the date to confirm.")
                if data["bookings"][bookingToRemove] == dateToBooking:
                    del data[bookingToRemove]
                    print(f"Remove booking: {bookingToRemove} with the date {dateToBooking}.")
                    with open(fileZoo, "w", encoding="utf-8") as file:
                        jason.dump(data, file, indent=4)
                    break
                else:
                    print("The date was incorrect. please try again")
            else:
                print("Booking couldnt be found. please try again")

def viewAnimals(): #[2]
    with open(fileZoo, "r", encoding="utf-8") as file:
        data = jason.load(file)
    avalibleAnimals = data["animals"]["animalsAvalible"]
    print(f"Currently the avalible animals are: {avalibleAnimals}.")
    checkUnavalible = int(input("If you wish to see what animals are currently unavalible press 1: "))
    if checkUnavalible == 1:
        unavalibleAnimals = data["animals"]["animalsUnavalible"]
        if len(unavalibleAnimals) == 1:
            print("Currently there are no animals unavalible!")
        else:
            print(f"Currently unavalible animals are {unavalibleAnimals}")

def createAdmin(remove): #[5]
    if remove == False:
        with open(fileZoo, "r", encoding="utf-8") as file:
            data = jason.load(file)
        pass
        try:
            adminUsername = input("Enter the username for the new account: ")
            if adminUsername in data.get("adminAccounts", {}) or adminUsername in data.get("accounts", {}):
                raise ValueError("Username has already been taken, please try again")
            adminPassword = input("Enter the password for the new account: ")
            data["adminAccounts"][adminUsername] = adminPassword
            with open(fileZoo, "w", encoding="utf-8") as file:
                jason.dump(data, file, indent=4)
            print("account should have been created.")
        except ValueError as e:
            print(e)
    else:
        with open(fileZoo, "r", encoding="utf-8") as file:
            data = jason.load(file)
        while True:
            accountToRemove = input("Enter the username of the account to remove.")
            if accountToRemove in data["adminAccounts"]:
                passwordToAccount = input("Enter the password to confirm.")
                if data["adminAccounts"][accountToRemove] == passwordToAccount:
                    del data[accountToRemove]
                    print(f"Remove username: {accountToRemove} with the password {passwordToAccount}.")
                    with open(fileZoo, "w", encoding="utf-8") as file:
                        jason.dump(data, file, indent=4)
                    break
                else:
                    print("Password was incorrect. please try again")
            else:
                print("Username could not be found. please try again")
            


# Run the login function
Access, username = login()

while True:
    if Access == "User":
        action = int(input("""
[                      DISPLAY                      ]
        [1] Create or remove a booking
        [2] View currently avalible animals
        

    """))
        
    elif Access == "Admin":
        action = int(input("""
[                      DISPLAY                      ]
        [1] Create a or remove a booking
        [2] View currently avalible animals
        [3] Update animal avaliblility
        [4] Update animal descriptions 
        [5] Create or remove admin account

    """))

    if action == 1:
        remove = int(input("[ Press 1 to create booking, press 2 to remove a booking.]"))
        if remove == 1:
            createBooking(username, remove) # create
        elif remove == 2:
            createBooking(username, remove) # remove
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break
    elif action == 2:
        viewAnimals()
    elif action == 3:
        updateAnimals("avalibility")
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break
    elif action == 4:
        updateAnimals("descriptions")
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break
    elif action == 5:
        remove = int(input("[ Press 1 to create booking, press 2 to remove a booking.]"))
        if remove == 1:
            createAdmin(remove=True) #remove
        elif remove == 2:
            createAdmin(remove=False) #create
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break
    else:
        print("ensure you enter a valid option.")


     


#next:
# Maybe remove login from the class(?)
# Create a table for all animal species in zoo
# Each species will have a generalised overview of the animal aswell as dates that animal can be visitted 
# create a bookings system, check what dates are good, which are taken

#Working:
#create admin acc
#view avalible animals
#create booking
#view unavalible animals
#remove account 
#remove booking
#animals function [3 and 4]

#not working:


