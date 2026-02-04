import pandas as pd
file = "Pandas_lesson1.csv"
df = pd.read_csv(file)

#Starter
print(df.head(10))#prints first 10 lines
print("-"*60) #used to seperate 
print(df.tail(10)) #print last 10
#Extension
print("-"*60)#improves readability
full_data = df.head(10) + df.tail(10) # concatenates both dataframes into 1
print(full_data) #prints both in the same line 
print("-"*60)#improves readability

#################################

print(df.head())#prints first 5 rows
print(df.info())#shows info about data set

df["Age"] = df["Age"].fillna(df["Age"].mean(neumeric_only = True)) #replaces missng values in column with average age
df = df.dropna(df) # remove any nil values?

print('''      
      ╱|、
     (˚ˎ 。7
      |、˜〵
      じしˍ,)ノ''')
