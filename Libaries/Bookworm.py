import json as jason

LibaryFile = "Libary.json"

def Login():
    #Check if they have an account
    createNewAcc = input("Do you already have an account created? Y/N: ").upper()
    with open(LibaryFile, "r", encoding="utf-8") as file:
        data = jason.load(file)

    if createNewAcc == "N":
        try: # create the account
            newEmailAcc = input("Enter the email for your account: ")
            newUserAcc = input("Enter the user for your account: ")
            newPasswordAcc = input("Enter the password for your account: ")
            if newUserAcc in data.get("accounts", {}):
                print("Username taken, please try again.")
            elif newEmailAcc in data.get("accounts"):
                print("Email is already in use, please try again.")
        except ValueError:
            print("please try again")
        else:
            if "accounts" not in data:
                data["accounts"] = {}

            data["accounts"][newUserAcc] = newPasswordAcc
            with open(LibaryFile, "w", encoding="utf-8") as file:
                jason.dump(data, file, indent=4)
                print("Account created!, Access Granted.")
                return "User", newUserAcc

    else:
        try:
            existingUserAcc = input("Enter your username: ")
            existingPassAcc = input("Enter your password: ")
            if existingUserAcc in data.get("accounts", {}):
                if data["accounts"][existingUserAcc] == existingPassAcc:
                    print("Access Granted")
                    return "User", existingUserAcc
                else:
                     print("Password did not match username.")
            elif existingUserAcc in data.get("adminAccounts", {}):
                if data["adminAccounts"][existingUserAcc] == existingPassAcc:
                    print("Access granted, Admin permissions enabled.")
                    return "Admin", existingUserAcc
            else:
                print("Password did not match username.")
        except ValueError:
            print("please try again.")     



def AddBooks(BookName, Author, ReleaseDate):
    data = [BookName], [Author][ReleaseDate]
    with open(LibaryFile, "w", encoding= "utf-8") as file:
            jason.dump(data)
    print("Book has been succesfully added.")

def BorrowBook(BookName, username):
    with open(LibaryFile, "r", encoding="utf-8") as file:
        data = jason.load(file)
    if BookName in data:
        print("Book Found:")
        del data[BookName]
        print(f"Book has been taken by {username}")

def ReturnBook(BookName, Author, ReleaseDate, username):
    with open(LibaryFile, "r", encoding="utf-8") as file:
        data = jason.load(file)
    if BookName in data:
        print("Book is already in the libary!")
        return
    else:
        data = [BookName], [Author][ReleaseDate]
        with open(LibaryFile, "w", encoding="utf-8") as file:
            jason.dump(data, file, indent=4)        
        print(f"Book: {BookName} Author: {Author} Release Date: {ReleaseDate}... Book has been successfully returned. thank you, {username}")

def FindBook(BookName):
    with open(LibaryFile, "r", encoding="utf-8") as file:
        data = jason.load(file)
    if BookName in data:
        print("Book Found!:")
        author = data[BookName]["Author"]
        releaseDate = data[BookName]["Releasedate"]
        print(f"The was authored by: {author} and released in {releaseDate}")
        print("-"*60)
    else:
        print("Book could not be found!, either we do not have this or you entered the name incorrectly.")


def Return():
     exit = int(input("Enter 1 to exit."))
     return exit

def Main():
    Access, username = Login()
    if Access == "Admin":
        Action = int(input("""What would you like to do?:
                            [1] = Borrow book
                            [2] = Return Book
                            [3] Find book
                            [4] - Add new book"""))
    elif Access == "Member":
         Action = int(input("""What would you like to do?:
                            [1] = Borrow book
                            [2] = Return Book
                            [3] Find book"""))
    while True:
        if Action == 1:
            bookName = input("Enter the books name: ")
            BorrowBook(bookName, username)
            Return(bookName, username)
            if exit == 1:
                 break
        elif Action == 2:
            bookName = input("Enter the books name: ")
            author = input("Enter the authors name: ")
            releaseDate = input("Enter the release date : DD/MM/YYYY: ")
            ReturnBook(bookName, author, releaseDate, username)
            Return()
            if exit == 1:
                 break
        elif Action == 3:
            bookName = input("Enter the books name that you wish to find (MUST BE EXACT.)")
            FindBook(bookName)
            Return()
            if exit == 1:
                 break
        elif Action == 4 and Access == "Admin":
            bookName = input("Enter the books name").capitalize()
            author = input("Enter the Authors name")
            releaseDate = input("Enter the release date: DD/MM/YYYY")
            AddBooks(bookName, author, releaseDate)
            Return()
            if exit == 1:
                 break
        else:
            print("Please input a valid option.")

Main()
