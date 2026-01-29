# Task: Email Validator

# Develop a Python function that validates
# whether a given string is a valid email
# address. Implement checks for the format,
# including the presence of an "@" symbol and
# a domain name 
def is_valid_email(e):
    if '@' not in e :
        return False
    
    parts=e.split('@')
    if len(parts)!=2:
        return False
    
    username=parts[0]
    domain=parts[1]

    if username=="" or domain=="":
        return False

    if '.' not in domain:
        return False
    
    return True     



email=input("enter the email address(username@domain.com):")
if is_valid_email(email):
    print("valid email address")
else:
    print("invalid email address") 