import os
import sys

def checkFolder(path):
    """
    The function checks the existence of a folder. The folder path will be given by the user as argument.   
    Basic Usage:
    checkFolder(your_folder_path)  # the function returns the existence as True for exists and False for not exists and exits with message for error.
    """
    try:
        if os.path.exists(path):
            return True
        elif not os.path.exists(path):
            return False
    except Exception as e:
        print('An error occured checking existence of folder at', str(path), ' : ',  str(e))
        sys.exit()

def checkFile(path):
    """
    The function checks the existence of a file. The file path will be given by the user as argument.   
    Basic Usage:
    checkFile(your_file_path)  # the function returns the existence as True for exists and False for not exists and exits with message for error.
    """
    try:
        if os.path.isfile(path):
            return True
        elif not os.path.isfile(path):
            return False
    except Exception as e:
        print('An error occured checking existence of file at', str(path), ' : ',  str(e))
        sys.exit()