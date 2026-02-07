#Learning uses of Iloc and groupby to create graphs with matplotlib
import pandas as pd
import pyplot from matplotlib

#Single row selecting:
df.iloc[0]
df.iloc[1]

#Colum Slicing
df.iloc[:, 1:4] # the Colon: shows its selecting all, then the 1:4 shows it selects all rows from colum 1 to 4

#Complex Selection
df.iloc[2:5, [0,3]]  # Selects rows 2 - 4 and colums 0 - 3

#These examples show the iloc sequence goes [Rows,]