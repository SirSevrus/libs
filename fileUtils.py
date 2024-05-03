import os
import sys

def createFolder(folderName, path=''):
    """
    The function creates a folder at the given path, by default in the same directory otherwise the user can provide the path also.   
    Rquires folder name.   
    Basic Usage :
    createFolder('welcome') # Creates welcome folder in the same directory
    createFolder('welcome', 'dirs') # Creates welcome folder in the dirs directory
    """
    try:
        if path.strip == '':
            os.makedirs(folderName)
        elif path.strip != '':
            os.makedirs(os.path.join(path, folderName))
    except Exception as e:
        print('An error occured during creating folder named', str(folderName), ':', str(path))
        sys.exit()

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