import pandas as pd

#Outputs the main menu and checks the user input

def main_menu():
    while True:
        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("\n--------------------- Main Menu --------------------- ")
        print("1. Total sales by product")

        choice = input('Enter your number selection here: ')

        if choice == "1":
            return 1
        else:
            print("Invalid selection. Please enter 1.")



#Generates submenu of available product codes and allows user to select a product to view
def get_product_id ():

    df = pd.read_csv("Task4a_RetailX_data.csv")

    product_codes = df["Product ID"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a product code:")
        for i in range(len(product_codes)):
            print(i+1, " ", product_codes[i])

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        
        product_ID = product_codes[selection -1]
   
    print("You have selected product id:",product_ID)
    return product_ID

#gets and converts user input from string to date format
def get_date(start_end):
    
    flag = True
    
    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))

        try:
           pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return date

#extracts data based on product ID within a user specified date range.
def get_data_by_ID_and_date(product_id, start_date, end_date):
    all_data = pd.read_csv("Task4a_RetailX_data.csv")
    product_data = all_data.loc[all_data["Product ID"] == product_id].copy()

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]



    return extracted_data

#generates a total of the number of items sold for the extracted data
def calculate_total_sale (date_ID, product_id, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    print('The total number of sales for product {}, between {} and {} was: {}'.format(product_id, start_date, end_date, total_sales))

#uses product id to find sales,cost and multiplys them to find the profit/loss
def get_profit_loss(product_id): 
    all_data = pd.read_cs("Task4a_RetailX_data.csv") #Get all data
    product_data = all_data.loc[all_data["Product ID"] == product_id].copy() # find data for specific id
    product_sales = product_data["QTY Sold"] # find sales amount
    product_sales_price = product_data["Sales Price"] # find revenue for each sale
    product_cost_price = product_data["Cost Price"] # find cost for each sale
    product_revenue = product_sales * product_sales_price # find true revenue
    product_profit = product_revenue - (product_cost_price * product_sales) # find true profit
    
    #if profit is below 0 it shows a loss rather then profit
    if product_profit > 0:
        print(f"product {product_id} profit was {product_profit}.")
    else:
        print(f"product {product_id} lost {product_profit}")
    #FINISHED

# gets the least sales in the category
def least_sales(catagory): 
    #TO DO LIST DONT DELETE
    #1: find all data (look in the getprofitloss function)
    #2: find all products inside that category: eg. products_inside_category = all_data.loc[all_data["Category"]]
    #3 find the bottom performers inside said category (im going to be so honest this is 100% the hardest thing to do about this)
    #4: compare with other categories(maybe not needed js an idea)
    #5: print data and show the user all the stuff 
    # got it i
    #OKOK PLAN MADE
    # all_data = pd.read_cs("Task4a_RetailX_data.csv")
    # products_inside_category = all_data.loc[all_data[category]]
    # while True:
        # if catagory = sales:
        #    lowest_sales = min(all_data[QTY sold])
            #print (data)
            # break
        # elif catagory = (whatever catagory)
        #    x = min(all_data(catagory))
        #    print (x, data)
        #MAKE SURE YOU SAVE THIS BTW
    #want a loop?ooo that could work actually
    # hol on
    all_data = pd.read_cs("Task4a_RetailX_data.csv")
    
    products_inside_category = all_data.loc[all_data[catagory]]
    #if it was "sales" it would look like Lowest_Sales = min(all_data["Sales"]) or
   


    lowest_sales = min(all_data["QTY Sold"]) # qty sold is the exactname of the catagory in the csv file)
    lowest_performers = lowest_sales 
    


    lowest_performers = min(products_inside_category)
    all_data = pd.read_cs("Task4a_RetailX_data.csv")
    if len(lowest_performers) > 1:
        print(f"The lowest performers are {lowest_performers}")
    else:
        print(f"The lowest performer is {lowest_performers}")

    

main_menu_choice = main_menu()

if main_menu_choice == 1: 
    product_id = get_product_id()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
    calculate_total_sale (date_ID, product_id, start_date, end_date)
    
elif main_menu_choice == 2: # Finding profit / loss
    product_id = get_product_id()
    #pass the product id into the find profit function
elif main_menu_choice == 3: # find product with least sales in catagory
    product_category = input("Enter the category you want to look at")
    least_sales(product_category)
    #1: give input to find which catagory the user wants to look at
    #2: pass the catagory to teh least_sales function

#Menu2
#Find Profit/loss on specific product ids
#Find products with least sales in catagories
#Find xxxx





