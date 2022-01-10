import re
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
                2. Book a Blood Test
                3. Cancel an Appointment
                4. Search for a Patient
                5. Delete Patient Details
                6. Exit\n
            """)
    while True:
        user_selection = input("Select a number from the options above: \n")
        if user_selection == '1':
            print("Enter the following details to register a patient: \n")
            register_new_patient()
            break
        elif user_selection == '2':
            print("----Enter the following details to book a test:---- \n")
            book_test()
            break
        elif user_selection == '3':
            print("Search for the patient you want to delete the test for: \n")
            search_test()
            break
        elif user_selection == '4':
            print("Follow the instructions on the search menu: \n")
            search_patient()
            break
        elif user_selection == '5':
            print("Search for the patient you would like to delete. \n")
            search_patient()
            break
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
        f_name = input("First Name: \n")
        first_pattern = "[a-zA-Z]"
        first_match = re.search(first_pattern, f_name)
        if first_match:
            break
        else:
            print("Please enter your first name.")
    register_new_patient["First Name"] = f_name

    while True:
        l_name = input("Last Name: \n")
        last_pattern = "[a-zA-Z]"
        last_match = re.search(last_pattern, l_name)
        if last_match:
            break
        else:
            print("Please enter your last name.")
    register_new_patient["Surname"] = l_name

    while True:
        date_of_birth = input("Date of Birth: \n")
        if validate_dob(date_of_birth):
            break
        else:
            continue
    register_new_patient["Date of Birth"] = date_of_birth

    while True:
        print("Please enter a valid UK mobile number.")
        mobile_number = input("Mobile Number: \n")
        if validate_number(mobile_number):
            break
        else:
            continue
    register_new_patient["Mobile Number"] = mobile_number

    while True:
        email_address = input("Email Address: \n")
        if validate_email(email_address):
            break
        else:
            continue
    register_new_patient["Email Address"] = email_address

    return update_worksheet_patient(register_new_patient)


def validate_dob(date_of_birth):
    """
    Checks if the date of birth entered is valid.
    """
    pattern = "^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$"
    if re.search(pattern, date_of_birth):
        return True
    else:
        print("Invalid input. Please try entering your D.O.B in dd/mm/yyyy.")
        return False


def validate_number(mobile_number):
    """
    Checks if the mobile number entered is valid.
    """
    pattern = "^(07\d{8,12}|447\d{7,11})$"
    if re.search(pattern, mobile_number) and len(mobile_number) == 11:
        return True
    else:
        print("Invalid number. Please try again.")
        return False


def validate_email(email_address):
    """
    Checks if the email address entered is valid.
    """
    pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|co.uk|net)"
    if re.search(pattern, email_address):
        return True
    else:
        print("Invalid email address. Please try again.")
        return False


def registeranother_or_book():
    """
    Allows the user to choose an option between registering another new patient
    booking a test for the current patient being entered or traversing back to
    the main menu.
    """
    while True:
        reg_or_book = input("""
        -----------------------------------------
        To register a new patient, please press 1.
        To book a blood test for this patient, please press 2.
        (Please choose from the following blood tests:
        Cholesterol, Blood Count, Thyroid, Liver, Electrolyte)
        To go back to the main menu, please press Q.
        ----------------------------------------- \n
        """)
        if reg_or_book == "1":
            register_new_patient()
            break
        elif reg_or_book == "2":
            book_test()
            break
        elif reg_or_book == "Q" or reg_or_book == "q":
            main_menu()
            break
        else:
            print("Invalid input. Please choose from 1, 2 or Q.")
            registeranother_or_book()
        return False


def book_test():
    """
    Books a blood test for a corresponding patient by adding details
    of full name, test that is required, appointment time
    and any special requirements that are necessary for the booking.
    """
    book_test = {}

    while True:
        full_name = input("Full Name: \n")
        full_pattern = "[a-zA-Z]"
        full_match = re.search(full_pattern, full_name)
        if full_match:
            break
        else:
            print("Please enter your full name.")
    book_test["Full Name"] = full_name

    while True:
        print("---Please choose from the following blood tests:---")
        print("Cholesterol, Blood Count, Thyroid, Liver, Electrolyte \n")
        test_required = input("Blood Test Required: \n")
        test_pattern = "Cholesterol|Blood Count|Thyroid|Liver|Electrolyte"
        test_match = re.search(test_pattern, test_required)
        if test_match:
            break
        else:
            print("Please enter a test for the patient. \n")
            continue
    book_test["Blood Test"] = test_required

    while True:
        appointment_time = input("Appointment Time: \n")
        time_pattern = "^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
        time_match = re.search(time_pattern, appointment_time)
        if time_match:
            break
        else:
            print("Please enter a time for the appointment in HH:MM.")
            continue
    book_test["Appointment Time"] = appointment_time

    while True:
        print("Please enter Yes/Y or No/n")
        special_requirements = input("Special Requirements: \n")
        sr_pattern = "[Yes|No]"
        sr_match = re.search(sr_pattern, special_requirements)
        if sr_match:
            break
        else:
            continue
    book_test["Special Requirements"] = special_requirements

    return update_worksheet_appointment(book_test)


def book_test_or_delete(row_number):
    """
    Allows the user to book a test or delete
    the patient after registering or searching for a
    patient instead of having to go back to the main menu.
    """
    while True:
        appointment = input("""
        -------------------------------------------------------
        To book a blood test for this patient, please press 1.
        (Please choose from the following blood tests:
        Cholesterol, Blood Count, Thyroid, Liver, Electrolyte)
        To delete this patient, please press 2.
        To go back to the main menu, please press Q.
        ------------------------------------------------------- \n
        """)
        if appointment == "1":
            book_test()
            break
        elif appointment == "2":
            delete_one_patient(row_number)
            break
        elif appointment == "Q" or appointment == "q":
            main_menu()
            break
        else:
            print("Invalid input. Please choose from 1, 2 or Q.")
            book_test_or_delete(row_number)
        return False


def book_another_test():
    """
    Allows the user to book an additional appointment or
    go back to the main menu after booking the first one.
    """
    while True:
        another = input("""
        --------------------------------------------
        To book another blood test, please press 1.
        To go back to the main menu, please press Q.
        --------------------------------------------\n
        """)
        if another == "1":
            book_test()
            break
        elif another == "Q" or another == "q":
            main_menu()
            break
        else:
            print("Invalid input. Please choose from 1 or Q.")
            book_another_test()
        return False


def update_worksheet_patient(register_new_patient):
    """
    Updates the worksheet by adding details of the newly registered patient.
    """
    new_patient_wrksheet = SHEET.worksheet('patient_registration')
    new_patient_wrksheet.append_row([x for x in register_new_patient.values()])
    print('New patient has been registered and files have been updated! \n')
    registeranother_or_book()


def update_worksheet_appointment(book_test):
    """
    Updates the worksheet by adding details of a newly booked appointment
    for a patient.
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
        find_input_test = input("Full Name: \n")
        fullname = column_acquire_two(find_input_test)
        search_test_string = fullname
    else:
        print("Invalid input. Please try again.")

    if search_test_string:
        for cell_value_two in (search_test_string):
            row_number_test = cell_value_two.row
            value_list_two = APPOINTMENT.row_values(row_number_test)
            listWithElemTwo = " ".join(map(str, value_list_two))

            print("The following test details for patient have been found!")
            print(listWithElemTwo)
            delete_one_test(row_number_test)
            break
    else:
        print("Test not found for this patient. Please try again.")
        return_to_menu()


def column_acquire_two(value):
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
    delete_test_option = input("""
    -----------------------------------------------------------------
    Are you sure you want to delete this test? If so, please press Y.
    If you do not and you want to return to the main menu, please press N.
    ----------------------------------------------------------------- \n
    """)
    while True:
        if delete_test_option == "Y" or delete_test_option == "y":
            print("Test is now being cancelled... \n")
            delete_test_row(row_number_test)
        elif delete_test_option == "N" or delete_test_option == "n":
            print("Test has not been cancelled. \n")
            main_menu()
        else:
            print("Invalid input. Please try again.")
            search_test()
            break
        return False


def delete_test_row(row_number_test):
    """
    Removes a test of a patient by deleting a row from the APPOINTMENT
    worksheet on gspread.
    """
    deleted_test = APPOINTMENT.delete_rows(row_number_test)
    print("Test has now been cancelled and has been removed the system. \n")
    main_menu()
    return deleted_test


def search_patient():
    """
    Allows the user to access a search menu to find any patient by their
    first name, surname or date of birth.
    """
    print("-----Search By:-----")
    print("--------------------")
    print("---1. First Name---")
    print("----2. Surname----")
    print("--3. Date of Birth--")
    print("---Q. Main Menu---")
    print("--------------------\n")
    while True:
        search = input("Please choose an option from 1-3 or Q. \n")
        if search == "1":
            search_acquire("First Name")
            break
        elif search == "2":
            search_acquire("Surname")
            break
        elif search == "3":
            search_acquire("Date of Birth")
            break
        elif search == "Q" or search == "q":
            main_menu()
            break
        else:
            print("Invalid input. Please try again.")
            search_patient()
            break


def search_acquire(search_option):
    """
    Acquires the input from the initial register new patient function and
    searches the gspread database for those inputs. Once acquired, the
    information of the patient is translated into a string.
    """
    if search_option == "First Name":
        find_input = input("First Name: \n")
        first_name = column_acquire(find_input)
        search_string = first_name
    elif search_option == "Surname":
        find_input = input("Last Name: \n")
        last_name = column_acquire(find_input)
        search_string = last_name
    elif search_option == "Date of Birth":
        find_input = input("Date of Birth: \n")
        dob = column_acquire(find_input)
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


def column_acquire(value):
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
    delete_option = input("""
    -----------------------------------------------------------------
    Are you sure you want to delete this patient? If so, please press Y.
    If you do not and you want to return to the main menu, please press N.
    ----------------------------------------------------------------- \n
    """)
    while True:
        if delete_option == "Y" or delete_option == "y":
            print("Patient is being removed... \n")
            delete_patient_row(row_number)
        elif delete_option == "N" or delete_option == "n":
            print("Patient has not been removed.\n")
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


def return_to_menu():
    """
    Provides the user with an option to search for a test or
    return to the main menu after certain tasks.
    """
    while True:
        return_option = input("""
        ------------------------------------------------------------------
        Would you like to return to the main menu? If so, please press Q.
        If you would like to search for a new test, please press 1.
        ------------------------------------------------------------------
        """)
        if return_option == 'Q' or return_option == 'q':
            main_menu()
            break
        elif return_option == '1':
            search_test()
            break
        else:
            print("Invalid input, please try again.")
            return_to_menu()
            break
        return False


def exit_system():
    """
    Exits the programme when chosen from the main menu.
    """
    print("-----------LabClinic has now been shut down-----------")
    print("------------Thank you for using our system------------")
    print("-----------------Have a lovely day!-----------------")


def main():
    """
    Initiates the programme.
    """
    main_menu()


print("--------------------------------------------------------------")
print("--------------------Welcome to LabClinic--------------------")
print("----------A client registration system that allows----------")
print("---------------you to register patient details---------------")
print("-----------------and book laboratory tests-----------------")
print("--------------------------------------------------------------\n")
main()
