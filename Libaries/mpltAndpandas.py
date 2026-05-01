from matplotlib import pyplot as plt
import pandas as pd
filename = ""
dataframe = pd.readcsv(filename)


def Return():
    exit = int(input("Enter 1 to exit."))
    return exit

def Main():
    Action = int(input("""What would you like to do?:
                            [1] - Bar Graph
                            [2] - Pie Chart
                            [3] - Line Plot
                            [4] - Scatter Plot
                            """))

    while True:
        if Action == 0: 
            #  
            Xaxis = input("Enter the category for the X axis")
            Yaxis = input("Enter the category name for the Y axis")
            plt.xlabel = input("enter x label")
            plt.ylabel = input("enter y label")  
            plt.title = input("enter the title")  
            
            plt.bar(dataframe[Xaxis], dataframe[Yaxis], color="skyblue", color="lime")
            Return("exit")
            if exit == 1:
                 break
                 
        elif Action == 1: 
            slice_amount = int(input("How many slices(categorys): "))
            slices = []
            slices_values = []
            for x  in range(slice_amount):
                new_slice = input("Enter the name of the category you want in your pie chart: ").capitalize
                slices.append(new_slice)
                slices_values = dataframe[new_slice]
                slices_values.pop(slices_values)
            plt.title = input("Enter the title of your pie chart!")
            plt.pie(slices_values, labels=slices, autopct='%1.1f%%', colors=["Red","Green", "Blue", "Yellow", "Pink "Skyblue"])          
            Return()
            if exit == 1:
                 break
        elif Action == 3: #
            Xaxis = input("Enter the category for the X axis")
            Yaxis = input("Enter the category name for the Y axis") 
            plt.plot(dataframe["Xaxis"], dataframe[Yaxis])
            plt.xlabel(f"{Xaxis}")
            plt.ylabel(f"{Yaxis}")
            plt.title("Line graph")
            plt.show() 
            Return()
            if exit == 1: 
                 break
        
        elif Action == 4: (Scatter graph)
            Xaxis = input("Enter the category for the X axis")
            Yaxis = input("Enter the category name for the Y axis")
            plt.label = ("enter the x axis labbel")
            plt.ylabel =input 
            #2. Get values of the categories using pandas
            #3. display them using .scatter
            #4. show the graph to the user
            # 5. start diggin in yo butt twin 
            plt.scatter()
            plt.show()
        else:
            print("Please input a valid option.")

