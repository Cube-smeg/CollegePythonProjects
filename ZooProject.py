import json as jason

#Enter Login and password
#Email
#Create bookings, date, name, viewing add information to animals
#hold information about all animals
fileZoo = "ZooDataBase.json"

class ZooAnimals():
    animals = []
    dates = []

    def login(self):
        createNewAcc = input("Do you already have an account created? Y/N").upper()
        if createNewAcc == "N":
            newEmailAcc = input("Enter the email for your account")
            newUserAcc = input("Enter the user for your account")
            newPasswordAcc = input("Enter the password for your account")
            with open(fileZoo, "w", encoding="utf-8") as file:
                pass
            

        else:
            #Read Json
            #Store user and pass into varible
            #compare both varibles to see if they are equal
            with open(fileZoo, "r", encoding="utff-8") as file:
                pass
                
            existingUserAcc = input("Enter your username")
            existingPassAcc = input("Enter your password")
            if existingUserAcc == #Username inside json file
                if existingPassAcc == #password inside json file
                print("Access Granted")
                Access = "Granted"


