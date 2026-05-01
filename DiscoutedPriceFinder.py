#Find original price:
ori_price = float(input("Enter the original price of the item: "))
cust_loyalty = input("Check the customers loyalty tier: Standard or Premium: ").capitalize

if cust_loyalty == "Standard":
    discount = .95 #5% off
elif cust_loyalty =="Premium":
    discount = .80 #20% off
else:
    discount = 1 # no discount

#apply discount:
final_price = ori_price * discount

#check for shipping if price is under 10:
if final_price < 10:
    shipping_price = 2
    final_price = final_price + shipping_price

print(f"your final price is: {final_price:.3f}")
