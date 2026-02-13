#Task: Password Strength Checker

#Create a Python function that evaluates
#the strength of a password entered by the
#user. Implement checks for factors such as
#length, presence of uppercase and
#lowercase letters, digits, and special characters.

import re

def password_checker(password):
    strength = 0 
    
    if(len(password)>8):
        strength+=1
    else:
        print("Password too short. Minimum 8 characters recommended.")
    
    if re.search(r"[a-z]", password):
        strength+=1
    else:
        print("Add at least one lowercase letter.")
        
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        print("Add at least one uppercase letter.")
        
    if re.search(r"\d", password):
        strength += 1
    else:
        print("Add at least one number.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        print("Add at least one special character (e.g., !@#$%).")
        
        
    if strength == 5:
        return "Very Strong"
    elif strength >= 3:
        return "Moderate"
    else:
        return "Weak"
    
user_password = input("Enter your password: ")
result = password_checker(user_password) 
print(f"Password Strength: {result}")