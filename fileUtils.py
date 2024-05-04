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

def readTextFile(path, chars=-1, lines=False, charLines=False):
    """
    Read text from a file and return the content based on specified parameters.

    Parameters:
    path (str): The path to the text file.
    chars (int, optional): Number of characters to read from the file. Default is -1, meaning the whole file.
    lines (bool, optional): If True, returns the lines of the file as a list. Default is False.
    charLines (int, optional): Number of lines to read as a list of characters. Default is False.

    Returns:
    str or list: Depending on the parameters provided, returns either a string (if chars is specified) or a list of lines from the file.

    Raises:
    FileNotFoundError: If the specified file path does not exist.
    """

    try:
        if lines:
            with open(path, 'r') as file:
                data = file.readlines()
            if charLines:
                Data = []
                for i in range(min(charLines, len(data))):
                    Data.append(data[i])
                return Data
            else:
                return data
        else:
            with open(path, 'r') as file:
                data = file.read(chars)
                return data
    except FileNotFoundError:
        print('Error: File not found at path', path)
        sys.exit()
    except Exception as e:
        print('An error occurred:', str(e))
        sys.exit()