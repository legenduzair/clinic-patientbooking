# LabClinic
## Introduction

LabClinic is a project that operates in the mock terminal provided by Code Institute, in Heroku. This project was built using only one programming language, Python.

In health care, it is vital that the programmes that are used by employees are reliable, quick and as efficient as possible. These automated systems can help make a huge difference in a patient receiving the correct diagnosis and treatment. LabClinic is an automated programme that allows the user to access patient details and book laboratory blood tests with ease. 

The system gives the user multiple options when handling patient records. This includes registering a new patient, searching for an existing patient and deleting an existing patient. Laboratory blood test appointments can also be booked and cancelled for a patient. The last option is present for the user to exit the programme to shut it down. 

![Responsive Screenshot Markup](/documentation/screenshots/responsive-project3.png)

## UX & Planning

### Project Goals
- As a developer of this command-line project, I want to build an automated programme that can assist laboratory professionals in handling patient information and booking blood tests as having the correct functional software can make a huge difference in this field as employees operate with urgent samples and tests.
- Whilst accessing the various options that are offered to the user in this programme, I want to make sure that no errors are present which would potentially cause difficulty for the user. 
- I want to develop a project that is completely accessible to the user and also operates with with my Google API's (Google Sheets and Google Drive) when they input their credentials into the terminal.

### User Stories
- As a user, I would like this programme to be functional and easy to understand. It should not be complicated and the options should be easily accessible.
- As a user, I would like to get to my options quickly whether if its registering a new patient or booking a test as there would be potentially many clients to go record in the health care field.

### Programme Structure 
Before initiating the project, I planned the structural layout of the programme by creating a flow chart on [Diagrams](https://app.diagrams.net/).

![Structural flow chart of project](/documentation/screenshots/flowchart-labclinic.png)

The flow chart initiates with the Main Menu where the user has the option to choose from 6 inputs; Registering a patient, Booking a blood test, Cancelling a blood test, Searching for an existing patient, Deleting an existing patient and finally closing down the programme. After each task is completed, the user has the option to go continue or go back to the main menu. 

## Features
### Existing Features
- Main Menu
  - The initial start up screen welcomes the user to LabClinic with a greeting message.  
  - Below this message, the main menu is located where the user has six different options to choose from. These include register a new patient, book a blood test, cancel an appointment, search for a patient, delete patient details and exit the programme. In order to access either of these options, the user will have to input any number from 1 to 6. Any other number inputted will result in an error stating that it is an invalid input and prompts the user to try again.

  ![Main menu](/documentation/screenshots/main-menu-ss.png)

- Register New Patient
  - When the user inputs the number '1', they are taken to the screen where they can input details to register a new patient. These details include first name, surname, date of birth, mobile number and an email address. Once the inputs have surpassed all validation checks, a message will pop up which will address the user that a patient has been registered. These patient details will be added to the gspread patient worksheet.
  - For the first and last names to be validated, the input has to be alphabetical only. 
  - For the date of birth to be validated, the input has to be in DD/MM/YYYY format. If the user enters anything else, the programme will prompt the user to input a date of birth in the set format.
  - For the email address to be validated, the input can contain anything (letters and numbers), has to have an '@' symbol and must contain '.com', '.co.uk' or '.net' at the end. If the user enters anything else, they will be prompted to input an email address again. 
  - For the mobile number to be validated, the input has to be a UK mobile number (starting with 07) and should be 11 digits in length. If the user enters anything else, they will be prompted to input a mobile number again.
  - After registering a new patient, the user will have an option to register another patient, book a test for the newly registered patient or return to the main menu.

![Register a new patient](/documentation/screenshots/register-new-patient-ss.png)

- Book a Blood Test
  - When the user inputs the number '2', they are taken to the screen where they can input details to book a blood test. These details include full name, blood test required, appointment time and special requirements. Once the inputs have surpassed all validation checks, a message will pop up which will address the user that a test has been booked. These test details will be added to the gspread appointment worksheet.
  - For the full name to be validated, the input has to be alphabetical only.
  - For the blood test required to be validated, the input has to be test names only from the selection provided by the programme when the user first chooses the option to book a blood test. 
  - For the appointment time to be validated, the input has to be in HH:MM format and in digits only. 
  - For the special requirements to be validated, the input has to be a selection from 'yes' or 'no'.
  - After booking a blood test, the user will have an option to book another blood test or return to the main menu.

![Book a blood test](/documentation/screenshots/book-blood-test-ss.png)

- Cancel an Appointment 
  - When the user inputs the number '3', they are taken to the screen where they can find the test they would like to delete. To search for the test, the user will have to input the full name of the patient. If the examined test is on the gspread worksheet, the relevant booked test for the patient will be returned.
  - The user will then have an option to either delete the test or go back to the main menu. When the test is deleted, the corresponding row of that appointment will be removed from the gspread appointment worksheet.
  - If there is no test found, the programme will prompt the user to try again. 

![Cancel a blood test](/documentation/screenshots/cancel-test-ss.png)

- Search for a Patient
  - When the user inputs the number '4', they are taken to a search menu where they can find the patient by inputting any one of three credentials. These include first name, last name and date of birth. If the examined patient is on the gspread worksheet, the relevant patient with their details will be returned and displayed to the user. 
  - Once the patient has been returned, the user has an option to either book a blood test, delete the patient or traverse back to the main menu.
  - If there is no patient found, the programme will prompt the user to try again.

![Search menu](/documentation/screenshots/search-menu-ss.png)

![Search options after finding patient](/documentation/screenshots/search-patient-options-ss.png)

- Delete Patient Details
 - When the user inputs the number '5', they are taken to the same search menu as from the option above. After finding the patient by inputting any one of the three credentials and if the patient is present on the gspread worksheet, they will be returned and displayed to the user. 
 - The user will then have an option to delete the patient along with many other options. If the user chooses to delete, a final confirmation message is displayed ensuring they make the correct decision. 
 - If the user confirms that the patient should be deleted, then the corresponding row of that patient will be removed from the gspread patient worksheet.
 - If there is no patient found, the programme will prompt the user to try again.

![Delete a patient](/documentation/screenshots/delete-patient-ss.png)

- Exit Programme
  - When the user inputs the number '6', they will be provided with a message telling them that the programme has been shut down and thanks the user for operating the programme.
  - Once the programme has been closed, the user will have to run the programme again to access the main menu.

![Exit programme](/documentation/screenshots/exit-programme-ss.png)

## Future Improvements
Ongoing improvements and developments are vital to any project and their success. Future ideas I would implement are:

  - Integrating an option in the programme that allows the user to update any credentials of a patient instead of having to register a new patient or searching for the patient and deleting the whole record. This would make it easier for the user to manage patient details quickly and as efficiently as possible. 
  - Adding a feature to the programme that double checks the patient and test records if the user enters the same patient or test into the programme. If the same patient or test is entered, the programme would return a message stating that the patient or test has already been registered. 
  - To take it to a more advanced level, integrating the logic of generating random ID's that include a certain number of digits could be assigned to a patient or a test after each one is recorded and added to the gspread worksheets. These patient or test ID's can be used in the search tool of the programme to handle and manage patient records.


## Data Model



## Testing

  

## Bugs



## Validator Testing



## Technologies Used

- Languages
    - Python3 is the only programming language used to develop this project.
  
  - Libraries
    - [Google Sheets](https://www.google.co.uk/sheets/about/) was used to create a database with two worksheets, patient and appointment. [Gspread](https://docs.gspread.org/en/latest/) is a Python API used for the programme to access the database on Google Sheets. These gspread worksheets are used to handle patient and test information when the user operates the programme. When registering a patient or booking a blood test, these details will be added to the gspread worksheets. When deleting a patient or cancelling a blood test, these details will be removed from the gspread worksheets.
    - Throughout this project, regular expressions were used to validate many credentials using the [Regex library](https://docs.python.org/3/library/re.html).
    - To deploy this project and obtain an active link, [Heroku](https://www.heroku.com/) was used. 



## Deployment



## Credits