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

## Future Improvements



## Data Model



## Testing



## Bugs



## Validator Testing



## Technologies Used



## Deployment



## Credits