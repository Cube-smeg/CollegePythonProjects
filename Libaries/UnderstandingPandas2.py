import pandas as pd 

data = pd.read_csv("ECarData.csv")
#Displaying potential columns to pick from
potentialColumns = ["top_speed_kmh", "battery_capacity_kWh", "number_of_cells", "torque_nm", "efficiency_wh_per_km", "range_km", "acceleration_0_100_s"]
print(potentialColumns)
#Find What to look at
Column = input("Which column would you like to look at?: ").lower()
brand = input("Enter the car brand you would like to look at?: ")
#Finding Operation
findWhat = input("What do you want to find? Max, Min, Mean or Mode?").lower()
#Manipulating data
if findWhat == "min":
    dataFound = (data[data["brand"] == brand])
    print(dataFound[Column].min())
elif findWhat == "max":     
    dataFound = (data[data["brand"] == brand])
    print(dataFound[Column].max())
elif findWhat == "mean":
    dataFound = (data[data["brand"] == brand])
    print(dataFound[Column].mean())
elif findWhat == "mode":
    dataFound = (data[data["brand"] == brand])
    print(dataFound[Column].mode())
else:
    print("You did not print one of the valid columns, try again")


print('''      
      ╱|、
     (˚ˎ 。7
      |、˜〵
      じしˍ,)ノ''')
