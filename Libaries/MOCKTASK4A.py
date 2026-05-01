import pandas as pd
import matplotlib.pyplot as plt

#The menu() function generates the UI the accepts and validates user choice

def conversion_menu():

    flag = True

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Australian Dollars (AUD)")
        print("4. Australian Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("-"*60)
        print("7. Compare GBP to other currencies. ")
        print("8. Chart the increase or decrease in value of a specified currency. ")
        print("######################################################")

        
        menu_choice = int(input("Please enter the number of your choice (1-8): "))

        if menu_choice == 7:
            compare_gbp_to_currency()
            continue
        elif menu_choice == 8:
            show_currency_performance()
            continue
        else:

            try:
                int(menu_choice)
            except:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                if int(menu_choice) < 1 or int(menu_choice) > 8:
                    print("Sorry, you did not enter a valid choice")
                    flag = True
                else:
                    return menu_choice  


#Gets the short version of the conversion information based on user menu choice
def get_currency ():
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GBP - JPY',
       '6': 'JPY - GBP'}
   
    currency = currencies.get(menu_choice)
    
    return currency





#The get_conversion_rate function uses pandas to get the latest conversion rate
#Imports a csv file in to a data frame
#Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate():
    df = pd.read_csv("Task4a_RBSX_data.csv")
    
    conversion_rate = round(df[currency].iloc[-1],2)


    return conversion_rate




#Accepts and validates user input for the amount they want to convert
def get_amount_to_convert():
    print("You are converting: ",currency)
    
    flag = True
    
    while flag:
        conversion_amount = input("please enter the amount you wish to convert")
    
        try:
            float(conversion_amount)
        except:
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return conversion_amount  




def compare_gbp_to_currency():
    print("entered")
    while True:
        df = pd.read_csv("Task4a_RBSX_data.csv")

        df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")


        start_date = pd.to_datetime(get_start_date(), format="%d/%m/%Y")
        end_date = pd.to_datetime(get_end_date(), format="%d/%m/%Y")

        # Filter dataframe
        filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

        if filtered_df.empty:
            print("No data found for that date range.")
            continue

        # Group by date and take mean
        grouped = filtered_df.groupby("Date").mean(numeric_only=True)

        # print options
        print("1 GBP - EUR")
        print("2 GBP - AUD")
        print("3 GBP - JPY")
        print("4 GBP - USD")
        print("5. exit ")

        user_choice = int(input("Enter 1 - 5 to select."))

        if user_choice == 1:
            print(grouped["GBP - EUR"])
        elif user_choice == 2:
            print(grouped["GBP - AUD"])
        elif user_choice == 3:
            print(grouped["GBP - JPY"])
        elif user_choice == 4:
            print(grouped["GBP - USD"])
        elif user_choice == 5:
            break
        else:
            print("Ensure you entered a valid option [1-5]")
def get_start_date():
    

    
    while True:
        start_date = input('Possible date ranges from [04/03/2024] To [28/05/2024] \n Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            continue
        else:
            break
    
    return start_date

def get_end_date():
    
    while True:
        end_date = input('Possible date ranges from [04/03/2024] To [28/05/2024] \n Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            continue
        else:
            break
    
    return end_date

def show_currency_performance():
    
    print("Which conversion would you like to make today?")
    print("1. Pound Sterling (GBP) to Euros (EUR)")
    print("2. Euros (EUR) to Pound Sterling(GBP)")
    print("3. Pound (GBP) to Australian Dollars (AUD)")
    print("4. Australian Dollars (AUD) to Pound Sterling (GBP)")
    print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
    print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
    choice = (input("Enter from 1-6"))
                 
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GBP - JPY',
       '6': 'JPY - GBP'}
   
    currency = currencies.get(choice)
    #stupid freaking groupby - Finds data within given date ranges
    df = pd.read_csv("Task4a_RBSX_data.csv")

    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

    start_date = pd.to_datetime(get_start_date(), dayfirst=True)
    end_date = pd.to_datetime(get_end_date(), dayfirst=True)

    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    print(filtered_df[['Date', currency]])
    
    #Create final graph
    plt.figure(figsize=(10,5))
    plt.plot(filtered_df['Date'], filtered_df[currency], marker='o')
    plt.title(f"{currency} Exchange Rate Over Time")
    plt.xlabel("Date")
    plt.ylabel("Exchange Rate")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    

#Performs the conversion and outputs the final values
def perfom_conversion():
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]) )
    print('You will receive {} in {}'.format(amount_recieved, currency[6:9]))
    
menu_choice = conversion_menu()
currency = get_currency()
conversion_rate = get_conversion_rate()
conversion_amount = float(get_amount_to_convert())
perfom_conversion()
