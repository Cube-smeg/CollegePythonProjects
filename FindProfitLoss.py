while True: 
    while True:
        CostPrice = float(input("Enter the cost of the product"))
        SellingPrice = float(input("Enter the selling point of the product"))
        if CostPrice < 0  or SellingPrice < 0:
            continue
        else:
            break

    if CostPrice > SellingPrice:
        Loss = CostPrice - SellingPrice
        print(f"You lost {Loss} ")
    else:
        Profit = SellingPrice - CostPrice
        print(f"You made {Profit} ")

    Retry = input("Do you want to restart - Y/N").upper()
    if Retry == "Y":
        continue
    else:
        break