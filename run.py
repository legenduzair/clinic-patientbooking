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
                3. Cancel a Test
                4. Search for a Patient
                5. Delete Patient Details
                6. Exit\n
            """)
    while True:
        user_selection = input("Please select a number from the following options: ")
        if user_selection == '1':
            print("Please enter the following details to register a patient: \n")
            register_new_patient()
            break
        elif user_selection == '2':
            print("Please enter the following details to book a test: \n")
            book_test()
            break
        elif user_selection == '3':
            print("Please search for the patient first you want to delete the test for: \n")
            search_test()
            break
        elif user_selection == '4':
            print("Please follow the instructions on the search menu: \n")
            search_patient()
            break
        elif user_selection == '5':
            print("Please search for the patient you would like to delete. \n")
            search_patient()
        elif user_selection == '6':
            print("LabClinic is now shutting down... \n")
            exit_system()
            break
        else:
            print("Invalid input. Please enter any digit from 1-6")


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

    return update_worksheet_patient(register_new_patient)


def validate_name(f_name):
    """
    Checks if the first name entered is valid.
    """
    pattern = "[a-zA-Z]"
    if (re.search(pattern, f_name)):
        return True
    else:
        print("Invalid input. Please try again.")
        return False


def validate_name(l_name):
    """
    Checks if the last name entered is valid.
    """
    pattern = "[a-zA-Z]"
    if (re.search(pattern, l_name)):
        return True
    else:
        print("Invalid input. Please try again.")
        return False


def validate_dob(date_of_birth):
    """
    Checks if the date of birth entered is valid.
    """
    pattern = "^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$"
    if (re.search(pattern, date_of_birth)):
        return True
    else:
        print("Invalid input. Please try again entering your D.O.B in dd/mm/yyyy format")
        return False


def validate_number(mobile_number):
    """
    Checks if the mobile number entered is valid.
    """
    pattern = "^(07\d{8,12}|447\d{7,11})$"
    if (re.search(pattern, mobile_number)):
        return True
    else:
        print("Invalid number. Please try again.")
        return False


def validate_email(email_address):
    """
    Checks if the email address entered is valid.
    """
    pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|co.uk|net)"
    if (re.search(pattern, email_address)):
        return True
    else:
        print("Invalid email address. Please try again.")
        return False


def validate_name(full_name):
    """
    Checks if the first name entered is valid.
    """
    pattern = "[a-zA-Z]"
    if (re.search(pattern, full_name)):
        return True
    else:
        print("Invalid input. Please try again.")
        return False


def registeranother_or_book():
    """
    Allows the user to choose an option between registering another new patient,
    booking a test for the current patient being entered or traversing back to
    the main menu.
    """
    while True:
        reg_or_book = input("If you would like to register another patient, please press A. If you would look to book a test for the current patient, please press T. To go back to the main menu, please press B \n")
        if reg_or_book == "A" or reg_or_book == "a":
            register_new_patient()
            break
        elif reg_or_book == "T" or reg_or_book == "t":
            book_test()
            break
        elif reg_or_book == "B" or reg_or_book == "b":
            main_menu()
            break
        else:
            print("Invalid input. Please choose from A, B or C.")
            registeranother_or_book()
        return False


def book_test():
    """
    Books an appointment for a corresponding patient by adding details
    of full name, test that is required, appointment time 
    and any special requirements that are necessary for the booking.
    """
    book_test = {}

    while True:
        full_name = input("Full Name: ")
        if validate_name(full_name):
            break
        else:
            continue
    book_test["Full Name"] = full_name

    while True:
        test_required = input("Test Required: ")
        if not test_required:
            print("Please enter a test for the patient.")
        else:
            break
    book_test["Test Required"] = test_required

    while True:
        appointment_time = input("Appointment Time: ")
        if not appointment_time:
            print("Please enter a time for the appointment.")
        else:
            break
    book_test["Appointment Time"] = appointment_time

    while True:
        special_requirements = input("Special Requirements: ")
        if not special_requirements:
            print("Please enter Yes or No.")
        else:
            break
    book_test["Special Requirements"] = special_requirements

    return update_worksheet_appointment(book_test)


def book_test_or_delete(row_number):
    """
    Allows the user to book a test after registering or searching for a 
    patient instead of having to go back to the main menu.
    """
    while True:
        appointment = input("Would you like to book an appointment for this patient? If so, please press A. Would you like to delete this patient? If so, please press D. If you would like to go back to the main menu: Please press B \n")
        if appointment == "A" or appointment == "a":
            book_test()
            break
        elif appointment == "D" or appointment == "d":
            delete_one_patient(row_number)
            break
        elif appointment == "B" or appointment == "b":
            main_menu()
            break
        else:
            print("Invalid input. Please choose from A or B.")
            book_test_or_delete()
        return False


def book_another_test():
    """
    Allows the user to book an additional appointment or 
    go back to the main menu after booking the first one.
    """
    while True:
        another = input("Would you like to book another appointment? If so, please press A. If you would like to go back to the main menu: Please press B \n")
        if another == "A" or another == "a":
            book_test()
            break
        elif another == "B" or another == "b":
            main_menu()
            break
        else:
            print("Invalid input. Please choose from A or B.")
            book_another_test()
        return False


def update_worksheet_patient(register_new_patient):
    """
    Updates the worksheet by adding details of the newly registered patient.
    """
    new_patient_worksheet = SHEET.worksheet('patient_registration')
    new_patient_worksheet.append_row([x for x in register_new_patient.values()])
    print('New patient has been registered and the files have been updated! \n')
    registeranother_or_book()


def update_worksheet_appointment(book_test):
    """
    Updates the worksheet by adding details of a newly booked appointment for a patient.
    """
    new_appointment_worksheet = SHEET.worksheet('appointment_registration')
    new_appointment_worksheet.append_row([x for x in book_test.values()])
    print('New appointment has been booked for this patient! \n')
    book_another_test()


def search_test():
    """
    Allows the user to search for any patient by their full name
    to retrieve test details. 
    """
    print("-----Please Search Tests By Entering Patient's Full Name:-----")
    search_test_option = "Full Name"

    if search_test_option == "Full Name":
        find_input_test = input("Full Name: ")
        fullname = column_acquire_two("Full Name", find_input_test)
        search_test_string = fullname
    else:
        print("Invalid input. Please try again.")

    if search_test_string:
        for cell_value_two in (search_test_string):
            row_number_test = cell_value_two.row
            value_list_two = APPOINTMENT.row_values(row_number_test)
            listWithElemTwo = " ".join(map(str, value_list_two))

            print("The following test details for this patient have been found!")
            print(listWithElemTwo)
            delete_one_test(row_number_test)
    else:
        print("Test not found for this patient. Please try again.")
        search_test()


def column_acquire_two(column, value):
    """
    Acquires the column and value of each test input. 
    """
    print("Searching for test booked for patient... \n")
    column_number_acquire_two = APPOINTMENT.findall(value)

    return column_number_acquire_two


def delete_one_test(row_number_test):
    """
    Allows the user to select between yes or no when cancelled a test.
    """
    delete_test_option = input("Are you sure you want to cancel this test? If yes, please press Y. If no, please press N. \n")
    while True:
        if delete_test_option == "Y" or delete_test_option == "y":
            print("Test is now being cancelled... \n")
            delete_test_row(row_number_test)
        elif delete_test_option == "N" or delete_test_option == "n":
            print("Test has not been cancelled and is still in the system. Now taking you back to the main menu. \n")
            main_menu()
        else: 
            print("Invalid input. Please try again.")
            search_test()
            break
        return False


def delete_test_row(row_number_test):
    """
    Removes a test of a patient by deleting a row from the APPOINTMENT worksheet
    on gspread.
    """
    deleted_test = APPOINTMENT.delete_rows(row_number_test)
    print("This test has now been cancelled and has been removed the system. \n")
    main_menu()
    return deleted_test


def search_patient():
    """
    Allows the user to access a search menu to find any patient by their 
    first name, surname or date of birth. 
    """
    print("-----Search By:-----")
    print("--------------------")
    print("---A. First Name---")
    print("----B. Surname----")
    print("--C. Date of Birth--")
    print("---D. Main Menu---")
    print("--------------------")
    while True:
        search = input("Please choose an option from A to D. \n")
        if search == "A" or search == "a":
            search_acquire("First Name")
        elif search == "B" or search == "b":
            search_acquire("Surname")
        elif search == "C" or search == "c":
            search_acquire("Date of Birth")
        elif search == "D" or search == "d":
            main_menu()
        else: 
            print("Invalid input. Please try again.")
            search_patient()
            break
            return False


def search_acquire(search_option):
    """
    Acquires the input from the initial register new patient function and 
    searches the gspread database for those inputs. Once acquired, the 
    information of the patient is translated into a string.
    """
    if search_option == "First Name":
        find_input = input("First Name: ")
        first_name = column_acquire("First Name", find_input)
        search_string = first_name
    elif search_option == "Surname":
        find_input = input("Last Name: ")
        last_name = column_acquire("Surname", find_input)
        search_string = last_name
    elif search_option == "Date of Birth":
        find_input = input("Date of Birth: ")
        dob = column_acquire("Date of Birth", find_input)
        search_string = dob
    else:
        print("Invalid input. Please try again.")
    
    if search_string:
        for cell_value in (search_string):
            row_number = cell_value.row
            value_list = PATIENT.row_values(row_number)
            listWithElem = " ".join(map(str, value_list))

        print("The following patient has been found!")
        print(listWithElem)
        book_test_or_delete(row_number)
    else:
        print("Patient not found. Please try again.")
        search_patient()
    

def column_acquire(column, value):
    """
    Acquires the column and value of each patient input. 
    """
    print("Searching for patient... \n")
    column_number_acquire = PATIENT.findall(value)

    return column_number_acquire


def delete_one_patient(row_number):
    """
    Allows the user to select between yes or no when removing patient details.
    """
    delete_option = input("Are you sure you want to delete this patient? If yes, please press Y. If no, please press N. \n")
    while True:
        if delete_option == "Y" or delete_option == "y":
            print("Patient is being removed... \n")
            delete_patient_row(row_number)
        elif delete_option == "N" or delete_option == "n":
            print("Patient has not been removed and is still in the system. Now taking you back to the main menu. \n")
            main_menu()
        else: 
            print("Invalid input. Please try again.")
            search_patient()
            break
        return False


def delete_patient_row(row_number):
    """
    Removes a patient by deleting a row from the PATIENT worksheet
    on gspread.
    """
    deleted_patient = PATIENT.delete_rows(row_number)
    print("This patient's details are now being removed from the system. \n")
    main_menu()
    return deleted_patient
    

def exit_system():
    """
    Exits the programme when chosen from the main menu.
    """
    print("-----------LabClinic has now been shut down-----------")
    print("------------Thank you for using our system------------")
    print("-----------------Have a lovely day!-----------------")


def main():
    main_menu()
    register_new_patient()
    book_test()


print("--------------------------------------------------------------")
print("--------------------Welcome to LabClinic--------------------")
print("----------A client registration system that allows----------")
print("---------------you to register patient details---------------")
print("-----------------and book laboratory tests-----------------")
print("--------------------------------------------------------------\n")
main()