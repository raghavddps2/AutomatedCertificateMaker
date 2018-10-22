'''
Developer : Shashank Sharma
Contributors : 

Description : 
    Read Name, Password (Email-id) from List of Participants/Volunteers
    Refer to Github ReadMe for Excel Sheet Configuration
Interaction : 
    Select Spreadsheet in .xls format
Output : 
    List of Names and Passwords
'''

#In-Built Packages
import xlrd as xls

#Dev Packages
import FSelect as folder

def readSheet():
    #Get Certificate File
    file_path = folder.selectFile()
    
    if file_path == '' or str(file_path)=='None':
        print('You have not selected any File for encryption')
        return 1
    else:    
        #Open File for Reading
        wb = xls.open_workbook(file_path.name) 
        sheet = wb.sheet_by_index(0)
        
        #Get Names
        names = [str(sheet.cell_value(i,0)) for i in range(1,sheet.nrows)]
        names = [x.upper() for x in names]
        names = [x.strip() for x in names]
        
        #Get Passwords
        passwords = [str(sheet.cell_value(i,1)) for i in range(1,sheet.nrows)]
        
        #return Names, Passwords to Calling Module
        return names,passwords
        
