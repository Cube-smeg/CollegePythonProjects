import pandas as pd
import json as jason
#Importantish varibles
fileName = "PersonalBudgetTrackerHelper.json"
balance = pd.read_json("PersonalBudgetTrackerHelper.json")
userExpenses = 0
purchaseCatagories =[
"Transport",
"Food" ,
"Entertainment"  ,
"Misc" ,
"CustomCatagory2"   
]

#VERY IMPORTANT FUNCTION TO UPDATE VALUES IN PERSONALBUDGETTRACKERHELPER.JSON (Used so values are saved and the program is somewhat useful)
def ChangeValue(fileName, key, newValue):
    try: #error handling (???)

        #opening the jason file in read mode to yk read it
        with open(fileName, "r", encoding="utf-8") as file:
            data = jason.load(fileName)

        #Editing the key value thing in jason file
        data[key] = newValue

        with open(fileName, "w", encoding="utf-8") as file: # i have no idea what the encoding does to be real
            jason.dump(data, file, indent=4)
    
        print(f"Updated:  {key} to: {newValue} in your budget tracker!!")
    #random error checks just incase! (also makes me look smart)
    except FileNotFoundError:
        print("Error has occured: Ensure the file name is correct and in a valid location")
    except jason.JSONDecodeError:
        print("Error has occured: JSON file format was invalid")
    except Exception as e:
        print(f"Error has occured: {e}")

#give ur balance a value 
if balance["CurrentBalance"] == "0": #only allows you to change your balance if it is not already given a value (i.e your first time running the program)
    currentBalance = int(input("How much money do you have in your balance?"))
    ChangeValue(fileName, "CurrentBalance", currentBalance) #actually changes the balance in the jason file 
else:
    currentBalance = balance["CurrentBalance"]

#give ur expenses a value
if balance["UserIncome"] == "0": #only allows you to change your balance if it is not already given a value (i.e your first time running the program)
    userIncome = int(input("What is your usual income?"))
    ChangeValue(fileName, "UserIncome", userIncome) #actually changes the balance in the jason file 
else:
    userIncome = balance["UserIncome"]

#PROGRAM ACTUALLY STARTS HERE KINDA
while True: 
    print(f"Your current balance is: {currentBalance}")
    whatToDo = int(input("What would you like to do?: Add purchase [1] | Edit Income [2] | Update Balance [3] ] | View Catagory [4] | View Balance [5]"))
    if whatToDo == 1:
        print(purchaseCatagories)
        purchaseCatagory = (input("What catagory do you want your purchase to come under?")).capitalize()
        purchaseCost = float(input("How much did the purchase cost?"))
        newValue = purchaseCatagory + balance[purchaseCatagory]
        ChangeValue(fileName, purchaseCatagory, purchaseCost)
        currentBalance = currentBalance - purchaseCost
        ChangeValue(fileName, "CurrentBalance", currentBalance)
        print(f"Updated tracker, your balance has been subtracted by: {purchaseCost} and your purchase has been logged in the appropiate catagory.")
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break
    elif whatToDo == 2:
        newIncome = float(f"Currently your income is: {userIncome}, what would you like to change it to?")
        userIncome = newIncome
        ChangeValue(fileName, "UserIncome", userIncome)
        print(f"Your new income is {userIncome}")
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":    
            break
    elif whatToDo == 3:
        operation = (input(f"Your current balance is: {currentBalance} What would you like to do?: Add | Subtract | Rewrite")).capitalize()
        if operation == "Rewrite":
            currentBalance = int(input("What do you want to change your balance to?"))
            ChangeValue(fileName, "CurrentBalance", currentBalance)
            print(f"Your new balance is: {currentBalance}")

        elif operation == "Add":
            addingBalance = int(input("How much would you like to add to your balance?"))
            currentBalance = currentBalance + addingBalance
            ChangeValue(fileName, "CurrentBalance", currentBalance)
        elif operation == "Subtract": 
            subtractingBalance = int(input("How much would you like to remove from your balance?"))
            currentBalance = currentBalance - subtractingBalance
            ChangeValue(fileName, "CurrentBalance", currentBalance)
        else:
            print("You entered an invalid action")

        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break
    elif whatToDo == 4:
        checkThis = input("Which catagory would you like to look at?: Transport, Food Entertainment or one of your own catagories?").capitalize()
        print(purchaseCatagories[checkThis])
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break

    elif whatToDo == 5:
        print(f"Your current balance is: {currentBalance}")
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break

    else:
        print("Ensure you enter a valid number for an action")
        UserLeave = input("Press E to exit, if not enter Y to carry out a new action").upper()
        if UserLeave == "E":
            break
