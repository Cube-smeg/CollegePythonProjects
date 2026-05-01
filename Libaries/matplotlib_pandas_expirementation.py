import matplotlib.pyplot as plt
import pandas as pd
use_dataset = int(input("Enter [1] to use a minimum wage dataset \n Enter [2] to use a finance dataset: "))
#Using minimum wage dataset:
if use_dataset == 1:
    filepath = "global_minimum_wage.csv"
    df = pd.read(filepath)
    print(f"Displaying dataset information: {df.info}")
    #Finding highest minimum wage out of all countrys:
    print(f"The highest minimum wage is: {df["Minimum_Wage_USD_Monthly"].max()} \n The lowest minimum wage is: {df["Minimum_Wage_USD_Monthly"].min()}")
    df.groupby("Minimum_Wage_USD_Monthly")

#Using finance dataset:
elif use_dataset == 2:
    filepath = ".csv"