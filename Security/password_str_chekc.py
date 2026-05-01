#Checklist for what is needed in a password
upper_case = False
lower_case = False
symbol = False
password_length = 0
common_weak_passwords = []
password_strength = "weak"
feedback = []
password_score = 0
valid_special_characters = [".",",","!","@","#","%","&"]
#create str checker function:
def strength_check(password):
    if len(password) > 8:
        password_length = True
        score =+ 1
    else:
        feedback.append("Ensure the password is over 8 characters")

    if password.lower() in common_weak_passwords:
        feedback.append("Password has been found in a database of common passwords, it is recomended that you change it.")
        score =-2
    
    if symbol == False:
        for x in valid_special_characters:
            if x in password:
                symbol = True
                score =+ 1
            else:
                feedback.append("Ensure you incorperate a special character inside your password.")
    
    if any(x.isdigit() for x in password):
        score =+1
    else:
        feedback.append("Ensure your contains a digit: ")
    
    if any(x.isupper() for x in password):
        score =+1 
        upper_case = True
    else:
        feedback.append("ensure you include uppercase characters in your password:  ")
    
    if any(x.islower() for x in password):
        lower_case = True
        score =+ 1
    else:
        feedback.append("Ensure you include loercase characters inside your password")


    #create score -> rating 
    if score <= 2:
        password_strength = "Weak"
    elif score <= 4:
        password_strength = "Moderate"
    else:
        password_strength = "Strong"
    
    return password_strength, feedback


#get users password
user_password = input("Enter your exact password to evaluate its strength: ")

#call function
rating, feedback = strength_check(user_password)
print(feedback)
print(f"Your overall passwords score is : {rating}")
