import gspread
from google.oauth2.service_account import Credentials
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('clinic-patientbooking')

PATIENT = SHEET.worksheet('patient_registration')
APPOINTMENT = SHEET.worksheet('appointment_registration')

def main_menu():
    """
    Main menu where the user can select between six diverse options
    """
    print("""
            --------------Main Menu--------------
                1. Register New Patient
                2. Book a Test
                3. Update Patient Details
                4. Search for Patient Details
                5. Delete Patient Details
                6. Exit\n
            """)
    while True:
        user_selection = input("Please select a number from the following options: ")
        if user_selection == '1':
            print("Please enter the following details to register a patient: \n")
            register_new_patient()
            break

def register_new_patient():
    """
    Register new patient by adding first name, surname, date of birth,
    mobile number and email address. Validate that the user
    has entered correct information otherwise display error
    """
    register_new_patient = {}

    while True:
        f_name = input("First Name: ")
        if validate_name(f_name):
            break
        else:
            continue
    register_new_patient["First Name"] = f_name

    while True:
        l_name = input("Last Name: ")
        if validate_name(l_name):
            break
        else:
            continue
    register_new_patient["Surname"] = l_name

    while True:
        date_of_birth = input("Date of Birth: ")
        if validate_dob(date_of_birth):
            break
        else:
            continue
    register_new_patient["Date of Birth"] = date_of_birth

    while True:
        mobile_number = input("Mobile Number: ")
        if validate_number(mobile_number):
            break
        else:
            continue
    register_new_patient["Mobile Number"] = mobile_number

    while True:
        email_address = input("Email Address: ")
        if validate_email(email_address):
            break
        else:
            continue
    register_new_patient["Email Address"] = email_address

def validate_name(f_name):
    pattern = "[a-zA-Z]"
    if (re.search(pattern, f_name)):
        return True
    else:
        print("Invalid input. Please try again.")
        return False

def validate_name(l_name):
    pattern = "[a-zA-Z]"
    if (re.search(pattern, l_name)):
        return True
    else:
        print("Invalid input. Please try again.")
        return False

def validate_dob(date_of_birth):
    pattern = "^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$"
    if (re.search(pattern, date_of_birth)):
        return True
    else:
        print("Invalid input. Please try again entering your D.O.B in dd/mm/yyyy format")
        return False

def validate_number(mobile_number):
    pattern = "^(07\d{8,12}|447\d{7,11})$"
    if (re.search(pattern, mobile_number)):
        return True
    else:
        print("Invalid number. Please try again.")
        return False

def validate_email(email_address):
    pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|co.uk|net)"
    if (re.search(pattern, email_address)):
        return True
    else:
        print("Invalid email address. Please try again.")
        return False

def main():
    main_menu()
    register_new_patient()

print("--------------------Welcome to LabClinic--------------------")
print("----------A client registration system that allows----------")
print("---------------you to register patient details---------------")
print("-----------------and book laboratory tests-----------------\n")
main()