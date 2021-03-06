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
  - If there is no test found, the programme will prompt the user to try again or ask if they want to return to the main menu. 

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
When developing this project, a data model was used when creating the database. The data model is shown below:

| Title                | Data Type |
|----------------------|-----------|
| First Name           | CharField |
| Surname              | CharField |
| Date of Birth        | Date      |
| Mobile Number        | Integer   |
| Email Address        | Email     |
| Full Name            | CharField |
| Test Required        | CharField |
| Appointment Time     | Time      |
| Special Requirements | CharField |

## Testing
During the development of LabClinic, the project went through rigorous testing to ensure a fully functional terminal programme was delivered at the end; A programme that has utilised defensive programming and that is also compatible with Heroku. To achieve this, I generated a flow chart of the structure of the programme. 

The 'main' and 'main menu' functions were developed first as they were part of the foundation of the project and it was the first thing the user would have access to when running the programme. After this, I went down the main menu options and created a function for each of the six choices. There were also mini functions that were involved with the main functions such as the validation functions that would help validate the input of credentials entered by the user. These validation function included regular expressions which was thoroughly researched on external sources such as Stack Overflow and YouTube. Different regex were used to experiment the validation of inputs until the correct one was acquired. When registering a new patient or booking a blood test, I had to make sure that these credentials were added to my Google Worksheets accordingly. In the same way, when deleting a patient or cancelling a test, I had to make sure that these credentials were removed from my Google Worksheets accordingly. To achieve this, I attempted to add and remove many user credentials every 5 minutes to ensure my programme was fully functional with the database.

Between the development of each main user selection, I used defensive programming and print statements to verify that if the user attempted to enter something else, the programme would return with a message to tell the user that the input was invalid and prompted them to try again. I also had to make sure that the user had an option to return to the main menu rather than being stuck in an infinite loop of entering patient or test data.

I would like to mention that in my requirements.txt file, there are a couple of libraries that are included but are not required for the programme to operate. These include 'sqlparse', 'Django', 'asgiref' and 'backports.zoneinfo'. These were installed as they were needed when experimenting with my programme to include other features which have now been omitted from the code. I have researched on many external sources on how to remove these libraries from my requirements.txt file but I have had no luck. Although this doesnt affect the functionality of my Python code in the Gitpod and Heroku terminals, I thought it would be important to mention this statement.

## Bugs
During the development of LabClinic, I encountered few bugs that needed attention. These are listed below:

### Fixed Bugs
  - Bug No 1
    - Problem: If the selection is chosen to exit the programme right after accessing the search menu to search for a patient, the statement 'Please choose an option from A to D.' would appear after the exit programme message. 
    - Cause: There was no break statement after each search acquire variable input in the search patient function which allowed the message to appear even after the programme had been closed down.
    - Fix: A break statement was added after each search acquire variable input in the search patient function.
  
  - Bug No 2
    - Problem: If the selection is chosen to exit the programme after accessing the search menu to search for a test, the statement 'Select from the options above' would appear after the exit programme message.
    - Cause: There was no break statement in the main menu function after calling the search test function. 
    - Fix: A break statement was added after the called search test function in the main menu function.


## Validator Testing
When examining the python code for any errors, [PEP8](http://pep8online.com/) returned no errors as shown in the screenshot below:

![PEP8 Validation](/documentation/screenshots/pep8-validator-ss.png)

## Technologies Used

- Languages
    - Python3 is the only programming language used to develop this project.
  
  - Libraries
    - [Google Sheets](https://www.google.co.uk/sheets/about/) was used to create a database with two worksheets, patient and appointment. [Gspread](https://docs.gspread.org/en/latest/) is a Python API used for the programme to access the database on Google Sheets. These gspread worksheets are used to handle patient and test information when the user operates the programme. When registering a patient or booking a blood test, these details will be added to the gspread worksheets. When deleting a patient or cancelling a blood test, these details will be removed from the gspread worksheets.
    - Throughout this project, regular expressions were used to validate many credentials using the [Regex library](https://docs.python.org/3/library/re.html).
    - [Tables Generator](https://www.tablesgenerator.com/markdown_tables) was used to create a markdown table for the data model used for this Python project.
    - To deploy this project and obtain an active link, [Heroku](https://www.heroku.com/) was used. 

## Deployment
This project was deployed using Code Institute's mock terminal template in Heroku. After getting the project files ready for Heroku, the following steps were carried out to ensure successful deployment:

  - Create a Heroku account and sign in.
  - From the Heroku dashboard, select the 'Create new app' button.
  - Input a unique app name and select your region. Then click on 'create app'.
  - After this, navigate to the 'Settings' tab.
  - Scroll down to the 'Config Vars' section and click on 'Reveal Config Vars'.
  - In the field for KEY, enter 'CREDS' and for the VALUE, copy and paste the entire 'creds.json' file from your Gitpod workspace and input into here.
  - In the second field for KEY, enter 'PORT' and for the VALUE, enter '8000'.
  - After inputting both keys and values, select the 'Add' button to add these config vars.
  - Then scroll down to the 'Buildpacks' section and click on 'Add Buildpack'.
  - In the 'Enter Buildback URL' input, select Python and click 'Save Changes'.
  - Repeat this for the Node.JS buildpack and save changes once more. (Make sure that the buildpacks are in the relevant order: Python first, then Node.JS second).
  - After configuring the settings, navigate to the 'Deploy' tab.
  - In the 'Deployment method' section, click on 'Connect to GitHub' and confirm to connect to GitHub.
  - After this, search for your GitHub repository by entering the exact name of it. When it appears, click on the 'Connect' button to connect the Heroku app to your repository.
  - After this, click on the 'Enable Automatic Deploys' button if you want any commited and pushed changes from GitHub to appear on the Heroku terminal.
  - Then scroll down and click the 'Deploy Branch' button.
  - After it is deployed, a message will appear stating 'Your app was successfully deployed'. A button will pop up for you to click on to display your project on the Heroku terminal.

The final deployed link for the Heroku terminal project is provided over here: [LabClinic](https://clinic-patientbooking.herokuapp.com/)

## Credits

### Content and Special Thanks

- All of the Python code was written by myself with the help of my tutor, [Richard Wells](https://github.com/D0nni387) and the Code Institute Slack community to assist me with the logic behind the complicated functions in my programme. 
- [Stack Overflow](https://stackoverflow.com/) and [Kite's Regex Tutorials](https://www.youtube.com/watch?v=UQQsYXa1EHs) were used to understand the logic of regular expressions and how to integrate them within my Python code.
- The [NHS Website](https://www.nhs.uk/conditions/blood-tests/types/) and my personal laboratory knowledge to provide me details of blood tests that are important to real life clinical patients.
