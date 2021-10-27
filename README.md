# Password-locker

## Description

This project is a python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves.

## User Stories
The user would like to.... :
* To create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Delete stored account login details that i do now want anymore.
* Copy my credentials to the clipboard


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.6
* pyperclip
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/Nancy-codergirl/Password-locker.git```

* cd Password-Locker

* code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x interface.py
        $ ./interface.py
* To run test for the application
        $ python3 passlock_test.py

## shortcuts to use to navigate the appplication.
*Use the following commands:
 - cc --to create an acoount
 - login --to logint to an existing account
 - ca --to create and save credentials
 - ca-g --to create credentials and have a password generated for you and save credentials
 - display-c --to view all saved credentials
 - delete-c --to delete a saved credential
 - copy-user --to copy a credential username to the clipboard
 - copy-pass --to copy a credential password to the clipboard
 - exit --to exit the program

## Technologies Used

* python3.6

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [nancy@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2021 **Nancy Muriithi**
