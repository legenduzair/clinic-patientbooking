import gspread
from google.oauth2.service_account import Credentials

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
    
def register_new_patient():
    """
    Register new patient by adding first name, surname, date of birth,
    mobile number and email address. Validate that the user
    has entered correct information otherwise display error
    """
    register_new_patient = {}

    while True:
        f_name = input("First Name: ")
        if not f_name:
            print("Please input your first name")
        else:
            break
    register_new_patient["First Name"] = f_name

    while True:
        l_name = input("Last Name: ")
        if not l_name:
            print("Please input your last name")
        else:
            break
    register_new_patient["Surname"] = l_name

    while True:
        date_of_birth = input("Date of Birth: ")
        if not date_of_birth:
            print("Please enter your date of birth in the correct format")
        else:
            break
    register_new_patient["Date of Birth"] = date_of_birth

    while True:
        mobile_number = input("Mobile Number: ")
        if not mobile_number:
            print("Please input a mobile number")
        else:
            break
    register_new_patient["Mobile Number"] = mobile_number

    while True:
        email_address = input("Email Address: ")
        if not email_address:
            print("Please input an email address")
        else:
            break
    register_new_patient["Email Address"] = email_address


def main():
    main_menu()
    register_new_patient()

print("--------------------Welcome to LabClinic--------------------")
print("----------A client registration system that allows----------")
print("---------------you to register patient details---------------")
print("-----------------and book laboratory tests-----------------\n")
main()