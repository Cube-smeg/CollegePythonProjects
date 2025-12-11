import pandas as pd 

data = pd.read_csv("data.csv")

subject = input("Which subject are you looking at?")
scoreRangeMin = int(input("Whats the lowest score you want to see?"))
scoreRangeMax = int(input("Whats the highest score you want to see?"))

wantedData = (data[subject] >= scoreRangeMin) & (data[subject] <= scoreRangeMax)
dataFound = data.loc[wantedData, subject]
print(dataFound)



print("-------Averages-------")
print(data["Maths"].mean())
print(data["English"].mean())
print(data["Science"].mean())
print(data["IT"].mean())
print("-------Top Scores-------")
print(data["Maths"].max())
print(data["English"].max())
print(data["Science"].max())
print(data["IT"].max())
print("-------Lowest Scores-------")
print(data["Maths"].min())
print(data["English"].min())
print(data["Science"].min())
print(data["IT"].min())

