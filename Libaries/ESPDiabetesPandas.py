import pandas as pd
file = "diabetes.csv"
data_frame = pd.read_csv(file)

give_glucose = int(input("Please give the range that the glucose needs to be higher than:"))
higher_than = data_frame[data_frame["Glucose"] > give_glucose]
print(higher_than)
