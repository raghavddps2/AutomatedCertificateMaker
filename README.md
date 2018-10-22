# AutomatedCertificateMaker

An Open Source Python Project to generate Batch of Certificates. 

Developer  : [Shashank Sharma](mailto:shashankrnr32@gmail.com)
Contributors : 


## Features
- Convert single Mail Merge Certificate File to Individual Certificate Files
- All the certificate files are encrypted with password*
- Read Names and Passwords from Excel Sheet**

## Files and Folders in Project
### Main.py 
### Scripts

| Name |Description  |
|--|--|
| BatchCertificateMaker.py | Converts each page of Mail-Merged Certificate Document to individual certificates. Also Contains Encryption Feature.|
|FSelect.py|Graphical User Interface (GUI) to select folders and files|
| ReadSpreadsheet.py | To read names and passwords from a spreadsheet (.xls or .xlsx)|

## Python Modules Used in Project
It is recommended to install the following modules/packages before running Main.py

-  [xlrd](https://pypi.org/project/xlrd/)
- [tkinter](https://docs.python.org/2/library/tkinter.html)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Documentation to run the scripts
1. Clone the project to your local folder. 
2. Run Main.py using an IDE or Command Window

Interaction with File/Folder Select

1. Select Mail-Merged Certificate File
2. Select Volunteer/Participants/Co-ordinators Excel Sheet
3. Select Destination Folder to generate individual certificates (**New Folder Recommended**) 

---
### Generated File Names
The names of the file are based on the data in the spreadsheet. All the names are uppercase for readability. 

---
### Encryption of PDF
All the files generated are encrypted for security reasons. The user passwords are based on the data in the spreadsheet. There is also an admin password to each of the files which can be changed in the scripts. 
Edit the script BatchCertificateMaker.py for your requirements.

##### Admin Password to all the encrypted files
    helloworld!!!
---
### Excel Sheet Format
The scripts are written for extracting data from Sheet 1 of the spreadsheet. Add all the names and passwords to Sheet 1, column 1 and 2. The spreadsheet must contain **Name** and **Password** as heading of the columns
Edit the script ReadSpreadsheet.py as per your needs. 

**Example Table :**

| Name | Password  |
|--|--|
|John Doe | johndoe@xyz.com |
|Kurt Weller|kurtweller@ccb.com|
|Cynthia|cinth@peachworks.com|

---
## Testing 
The following project is tested on Windows. It will be tested on other platforms as well in the coming days. Feel free to leave a [mail
](mailto:shashankrnr32@gmail.com) in case of Errors/Bugs/Feedback

## Project Requirement
This project is developed as a support IEEE-RIT's e-certificate management for all the events conducted. 