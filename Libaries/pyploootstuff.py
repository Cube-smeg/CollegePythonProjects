import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Ask the user what they want to find:
try:
    given_graph = int(input('''
    [1] - Bar Graph
    [2] - Scatter Graph
    '''))
except ValueError:
    print("Enter 1 or 2. ")

#Check if the user has their own data they want to use:
user_file = int(input("Enter 1 if you already have your own file: "))
if user_file == 1:
    user_file_name = input("Enter the exact name of the file including the filetype: ")
    y_axis = input("Enter the name of the Y axis: ")
    x_axis = input("Enter the name of the X axis: ")
    title = input("Enter the title of your graph: ")
    first_colum = input("Enter the exact name of the first colum to use: ")
    second_colum = input("Enter the exact name of the second colum: ")


else:
    cv_file = "vgsales.csv"
    dataframe = []

dataframe = pd.read_csv(user_file_name)

if given_graph == 1:
    if user_file == 1:
        dataframe = pd.read_csv(user_file_name)
        #Create bar graph:
        plt.bar(dataframe[first_colum], dataframe[second_colum])
        plt.xlabel = x_axis
        plt.ylabel = y_axis
        plt.title = title
        plt.legend
        plt.show()
elif given_graph == 2:
    if user_file == 1:
        dataframe = pd.read_csv(user_file_name)
        #Create scatter graph:
        plt.scatter(dataframe[first_colum], dataframe[second_colum])
        plt.xlabel = x_axis
        plt.ylabel = y_axis
        plt.title = title
        plt.legend 
        plt.show()

def create_scatter(x_axis, y_axis, title):
    plt.xlabel = x_axis
    plt.ylabel = y_axis
    plt.title = title
    plt