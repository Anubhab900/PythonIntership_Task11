import email
import re

##============================================================================##
def validate_email(email):
    '''Validate Email Address'''
    pattern= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

def validate_phone_number(phone_number):
    '''Validate Phone Number (10 digits)'''
    pattern = r'^\d{10}$'
    if re.match(pattern, phone_number):
        return True
    return False

def validate_postal_code(postal_code):
    '''Validate Postal Code (5 digits)'''
    pattern = r'^\d{5}$'
    if re.match(pattern, postal_code):
        return True
    return False


##============================================================================##

def ValidationCenter():
    '''Validation Center Class'''
    email= input("Enter email address: ").strip()
    phone_number= input("Enter phone number: ").strip()
    postal_code= input("Enter postal code: ").strip()



    test_cases={
      "Emails": [
         "test@example.com"],
      "Phone Numbers": [
        "1234567890"
               ],
      "Postal Codes": [
        "12345"
         ]
    }

    #Email Validation
    if email in test_cases["Emails"]:
        print("Email address already exists. And is valid.")
    elif validate_email(email):
        test_cases["Emails"].append(email)
        print("Valid Email Address")
        print(test_cases["Emails"])
    else:
        print("Invalid Email Address")
    
    #Phone Number Validation
    if phone_number in test_cases["Phone Numbers"]:
        print("Phone number already exists. And is valid.")
    elif validate_phone_number(phone_number):
        test_cases["Phone Numbers"].append(phone_number)
        print("Valid Phone Number")
        print(test_cases["Phone Numbers"])
    else:
        print("Invalid Phone Number")
    
    #Postal Code Validation
    if postal_code in test_cases["Postal Codes"]:
       print("Postal code already exists. And is valid.")
    elif validate_postal_code(postal_code):
       test_cases["Postal Codes"].append(postal_code)
       print("Valid Postal Code")
       print(test_cases["Postal Codes"])
    else:
       print("Invalid Postal Code")

ValidationCenter()                           
