

Num1 = int(input("Enter your first number"))
Num2 = int(input("Enter your second number"))

dictionary = {"Key1": "Value1", "Key2": "Value2"}

if Num1 > Num2:
    print("The first number is greater then the second number")
else:
    print("The second number is greater then the first number")                         

operation = input("Which operation would you like to perform, addition, subtraction, multiplication or division?")

if operation.lower() == "addition":
    print(Num1 + Num2)
elif operation.lower() == "subtraction":
    print(Num1 - Num2)
elif operation.lower() == "division":
    print(Num1 / Num2)
elif operation.lower() == "multiplication":
    print(Num1 * Num2)
else:
    print("Please ensure you entered a valid operation")
   


num1 = int(input("enter another number"))
num2 = int(input("Enter another number"))

match (num1, num2):
    case (num1, num2) if num1 % 2 == 0 or num2 % 2 == 0:
        print("either number 1 or number 2 is even")
    case (num1, num2) if num1 > num2:
        print("The first number is greater then the second number")
    case (num1, num2) if num1 < num2:
        print("The second number is greater then the first number")

