#Developer : Shashank Sharma
#An Open-Source Project for Certificate Management

#In-Built Packages
import tkinter as tk
from tkinter import filedialog

#-----------------------------------------------------------------------------
#selectFolder() to select the folder of certificates

def selectFolder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

#------------------------------------------------------------------------------
#selectFile() to select individual file of certificate

def selectFile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfile()
    return file_path

#-----------------------------------------------------------------------------  