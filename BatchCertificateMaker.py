'''
Developer : Shashank Sharma
Contributors : 

Description : Converts a MailMerged Certificate File to individual Certificate File
Input :         
    Mail-Merged File (Manual)
Interaction :
    1 : Select Excel Sheet for Names and Passwords (Manual)
    2 : Select Destination Folder (Manual)
Output :
    Individual Encrypted File in the Destination Folder (Automated)
'''

#Built-In Packages
from PyPDF2 import PdfFileWriter
import PyPDF2

#Dev Packages
import FSelect as folder
import ReadSpreadsheet as xls

def createBatchCertificates():
    #Get Certificate File
    file_path = folder.selectFile()
    
    if file_path == '':
        print('You have not selected any File for encryption')
        return 1
    else:
        #Open File for Reading
        inputFile = open(file_path.name, 'rb')
        pdfReader = PyPDF2.PdfFileReader(inputFile)
        
        #Select xls file to read Names and Passwords
        names,passwords = xls.readSheet()
        
        #Select Destination Folder
        destination_path = folder.selectFolder()
        
        for pNum in range(0,pdfReader.numPages):
            output_pdf = PdfFileWriter()
            output_pdf.addPage(pdfReader.getPage(pNum))
            
            #Encrypt Each Certificate File with passwords
            output_pdf.encrypt(passwords[pNum],'helloworld!!!')
            
            #Complete Path
            file = destination_path + '/' + names[pNum] + str(pNum+1) + '.pdf'
            
            #Create Output File
            with open(file, "wb") as out_file:
                output_pdf.write(out_file)
            
            
createBatchCertificates()