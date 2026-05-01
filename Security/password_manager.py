import json as jason
file_path = "password_holder.json"

def main_menu():
    options = int(input("""\n
    ------ Password Manager ------
    [1] - View passwords
    [2] - Add password
    [3] - Remove password 
    """))

    if options == 1:
        account_to_open = input("Enter the application you want to check your passwords Ie, google, microsoft: ").lower
        #show password
        with open(file_path, "r") as file:
            passwords = jason.load(file)
            find_password = passwords[account_to_open]
            print(find_password)
    elif options == 2:
        account_to_add = account_to_open = input("Enter the application you want to check your passwords Ie, google, microsoft: ").lower
        #get username and password to add
        new_username = input("Enter the username for the password: ")
        new_password = input("Enter the password to the account: ")
        data_dump = {}
        data_dump[new_username] = new_password
        #add info to json file
        with open(file_path, "r+") as file:
            file_data = jason.load(file)
            file_data[account_to_add].append(data_dump)
            file.seek(0)
            jason.dump(file_data, file, indent=4)
    elif options == 3:
        password_to_remove = input("enter the exact name of the password you want to remove")
        username_to_remove = input("enter the username associated with that password")
        with open(file_path, "r+") as file:
            data = jason.load(file)
            if username_to_remove in data:
                if password_to_remove in data:
                    data.pop(username_to_remove[password_to_remove])
                    file.seek(0)
                    jason.dump(data, file, indent=4)
                else:  
                     print("password could not be found")     
            else:
                print("username could not be found")

main_menu()

    