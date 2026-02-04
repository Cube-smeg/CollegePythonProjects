#Miler + Smeg + gappy2trappy
#Fitness tracker: 22/01/26
import json as jason
file = "FitnessTracker.json"
def create_tracker():
    first_name = input("what is your first name: ")
    last_name = input ("what is your last name: ")
    full_name = first_name, " ", last_name
    #storing name to use later
    with open(file, "w", encoding="utf-8") as file:
        jason.dump(full_name)

    #find information about the user
    while True:
        try:
            weight = float(input("What is your weight (kg): "))
            height = float(input("What is your height (m): "))
        except ValueError:
            print("Invalid input")
            continue
        if height < 0.5:
            print("invalid height")
        else:
            break
    return height, weight

  
  
MIN_HEIGHT = 0.5


#set the users goals
def create_goals(username): #takes username so it can save it properly
    shortterm_goals = []
    longterm_goals = []
    #disgustingly confusing while loop - blame mitler
    while True:
        new_goal = input("Enter your short term goal")
        new_long = input("Enter your long term goal ")
        shortterm_goals.append(new_goal)
        longterm_goals.append(new_long)
        exit = input("do you want to enter any more goals? Y/N").upper()
        if exit == "N":
            print("Cool, bye bye!!")
            break
        elif exit == "Y":
            continue
        else:
            print("Sorry, not a valid input")
            while True:
                exit = input("do you want to enter any more goals? Y/N").upper()
                if exit == "N":
                    print("Cool!")
                    break
                elif exit == "Y":
                    break
                else:
                    print("Didn't you hear me the first time? INVALID INPUT!!!")
    save_data(username, shortterm_goals, longterm_goals)

def save_data(arg1, arg2, arg3): #using ambiguous varible names due to it saving multiple different things
    #arg1: username always
    # moving all args into a df
    data = [arg1], [arg2][arg3]
    # saving the data
    with open(file, "r") as file:
        if arg1 in file:
            data = data[arg1]
            with open(file, "w") as file:
               jason.dump(data)
        else:
            with open(file, "w") as file:
                jason.dump(data)
    
#perform BMI calculation          
def find_BMI(user_weight, user_height):
    if user_weight < MIN_HEIGHT:
            print("Calculation can not be complete, height is too low.")
    else:
        user_BMI = user_weight / (user_height ** 2)
        user_BMI = "%.2f", user_BMI 
        return user_BMI

# find user, find their information, perform BMI calculation            
def search_user(): 
    find_user = input("Enter the username of who you want to find: ")
    with open(file, "r", encoding="utf-8") as file:
        if find_user in file:
            user_information = file[find_user]
        else: 
            print("username could not be found, ensure its correct")
    user_weight = user_information["weight"]
    user_height = user_information["height"]
    user_BMI = find_BMI(user_weight, user_height)
    print(f"{find_user} Weight is {user_weight}, their height is {user_height}. Their BMI is: {user_BMI}")



print('''      
      ╱|、
     (˚ˎ 。7
      |、˜〵
      じしˍ,)ノ''')

def main():
    new_user = input("Do you already have an account?: Y/N ").upper()
    while True:
        if new_user == "Y":
            create_tracker()
            break
        elif new_user != "N" or "Y":
            print("Enter either Y or N")
            continue
    action = int(input("""What would you like to do:
                       [1] - Search user information
                       [2] - Create your own goals
                       [3] - Create a new tracker"""))
#functions:
#save_data - saves data given to the json file
#serch_user - finds information about a specified user
#create_goals - allows users to create fitness goals both short and long term as well as saving it using save_data()
#create_tracker - allows new users to create an account 