import json as jason
import datetime 

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
            elif any(newEmailAcc == info.get("email") for info in data.get("accounts", {}).values()):
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
            if existingUserAcc in data.get("accounts", {}):  # Username inside json file
                if data["accounts"][existingUserAcc] == existingPassAcc:  # password inside json file
                    print("Access Granted")
                    return "User", existingUserAcc
                elif data["adminAccounts"][existingUserAcc] == existingPassAcc:
                    print("Access granted, Admin permisions enabled.")
                    return "Admin", existingUserAcc
                else:
                    print("Password did not match username.")
            else:
                print("Username could not be found.")
        except:
            print("Please try again.")

def updateAnimals(whatToUpdate): #[4], [3]
    if whatToUpdate == "avalibility":
        pass
    elif whatToUpdate == "descriptions":
        pass
    
      

def createBooking(username): #[1]
    with open(fileZoo, "r", "utf-8") as file:
        bookings = jason.load(file)
    unavalibleDates = bookings["bookings"][*]
    while True: # finding a valid date for booking
        bookingDates = int(input("Please enter when you wish to visit [DD/MM/YYYY]: "))
        try:
            validDate = datetime.strptime(bookingDates("%d/%m/%Y"))
            if validDate in unavalibleDates:
                raise ValueError("Day has already been taken, please select another time")
            
            print("Date validated. your booking has been created for: ", validDate.strftime("%d/%m/%Y"))
            break
        except: ValueError

    finalDate = ["bookings"][username] = validDate.date().isoformat()
    with open(fileZoo, "w", "utf-8") as file:
        jason.dump(finalDate, file, indent=4 )

def viewAnimals(): #[2]
    pass

def createAdmin(): #[5]
    with open(fileZoo, "r", "utf-8") as file:
        data = jason.load(file)
    pass
    try:
        adminUsername = input("Enter the username for the new account: ")
        if adminUsername in data.get["adminAccounts"] or adminUsername in data.get["accounts"]:
            raise ValueError("Username has already been taken, please try again")
        adminPassword = input("Enter the password for the new account: ")
    except ValueError:

        accountInformation = ["adminAccounts"][adminUsername] = [adminPassword]
        
        with open(fileZoo, "w", "utf-8") as file:
            jason.dump(accountInformation, file, indent=4)



# Run the login function
Access, username = login()

while True:
    if Access == "User":
        action = int(input("""
    [                      DISPLAY                      ]
        [1] Create a booking
        [2] View avalible animals


    """))
        
    elif Access == "Admin":
        action = int(input("""
    [                      DISPLAY                      ]
        [1] Create a booking
        [2] View avalible animals
        [3] Update animal avaliblility
        [4] Update animal descriptions 
        [5] Create new admin account

    """))

    if action == 1:
        createBooking(username)
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break
    elif action == 2:
        pass
    elif action == 3:
        updateAnimals("avalibility")
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break
    elif action == 4:
        updateAnimals("description")
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break
    elif action == 5:
        createAdmin()
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