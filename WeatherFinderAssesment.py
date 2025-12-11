import requests
import pandas as pd
import json as jason


#Find API - OpenWeatherMap Y
#Ask for a city Y
#Save API Response to a JSON file - USE GET METHOD Y
#Read specific JSON file parameters given by the user
#Display the statistics to the user in a understandable format
#Show main statistics - current.temp, current.humidity, current.wind_speed, current.weather.description (print these from the api response json file) Y
#Error handling on inputs (sticking to length checks and type validation) Y
#Multiple Use in 1 run (functions)
#Display future statistics


ApiKey = "ca52f33f0c6862b9e1c84aac584ae49e"
FileName = "ApiResponse.json"
PotentialResponses = {
    1: "current.temp",
    2: "current.humidity",
    3: "current.wind_speed",
    4: "current.weather.description"
}



#Finding city - Mainly for reuseability E 
def FindCity():
    while True:
        CityName = input("Enter the name of the city you want to check").capitalize() # Autoconvert to a correct format 
        if len(CityName) < 3 : 
            print("Ensure the name is correct.")
        else:
            return CityName


#Create the APIs response 
def CreateResponse(CityName):
    Response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={CityName}&appid={ApiKey}&units=metric"
    )

    Data = Response.json()
    print("Request placed into Response")

    #Save response into json file
    try:
        with open(FileName, "w", encoding="utf-8") as file:
            jason.dump(Data, file, indent=4)


    except FileNotFoundError:
        print("File Not Found")
    except jason.JSONDecodeError:
        print("File is formatted incorrectly ")
    except Exception as e:
        print(f"An unknown error has occured {e} ")
    return Data

#Ask what the user wishes to see
def FindWhat():
    Targets = []

# Instead of using If statements because there so long, I use the for loop to cycle through the targets allow the user to
# chose the target they want and actively update it using the response to WhatToFind

    for x in range(3):
        try:

            WhatToFind = int(input(f"What would you like to look at?: {PotentialResponses}"))
            if WhatToFind in PotentialResponses:
                Targets.append(WhatToFind)
            else:
                print("Select between 1-4")
        except ValueError:
            print("Enter a number between 1-4")
    return Targets

def DisplayResults(Targets, City, Data):
    #Read the Json File and use it to display the relavent data
    print(f"--- Current Weather for {City} ---")

    for x in Targets:
        Key = PotentialResponses[x]   # like "current.temp"
        Parts = Key.split(".")        # ["current","temp"]

        # Drill into nested dictionary
        value = Data
        for p in Parts:
            value = value[p]

        print(f"{Key}: {value}")

    print("-------------------------------")

    #Going to sleep its 5am - ToDo: Print all 3 Displays in a formatted mannor, Finish the end While Loop, Correct the target options to match those in the Json File maybe change it to a dictionary and use for what to pick and value for the exact param name(only hard part left)
    
#Display Results and initiate program
while True:
    print("-------Weather App-------")
    City = FindCity()
    Data = CreateResponse(City)
    Targets = FindWhat()
    DisplayResults(Targets, City, Data)
   
    UserExit = input("Press E to exit, if not enter Y to carry out a new action").upper()
    if UserExit == "E":
        break
