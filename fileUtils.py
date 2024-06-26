import os
import sys
import pickle

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

def readBinaryFile(path, bytes=-1, lines=False, byteLines=False):
    """
    Read binary data from a file and return the content based on specified parameters.

    Parameters:
    path (str): The path to the binary file.
    bytes (int, optional): Number of bytes to read from the file. Default is -1, meaning the whole file.
    lines (bool, optional): If True, returns the lines of the file as a list. Default is False.
    byteLines (int, optional): Number of lines to read as a list of bytes. Default is False.

    Returns:
    bytes or list: Depending on the parameters provided, returns either bytes (if bytes is specified) or a list of lines from the file in bytes format.

    Raises:
    FileNotFoundError: If the specified file path does not exist.
    """

    try:
        if lines:
            with open(path, 'rb') as file:
                data = file.readlines()
            if byteLines:
                Data = []
                for i in range(min(byteLines, len(data))):
                    Data.append(data[i])
                return Data
            else:
                return data
        else:
            with open(path, 'rb') as file:
                data = file.read(bytes)
                return data
    except FileNotFoundError:
        print('Error: File not found at path', path)
        sys.exit()
    except Exception as e:
        print('An error occurred:', str(e))
        sys.exit()

def createEmptyFile(fileName, path='', binary=False):
    """
    Create an empty file with the given name and path.

    Parameters:
    fileName (str): The name of the file to be created.
    path (str, optional): The path where the file will be created. Default is the current directory.
    binary (bool, optional): If True, creates a binary file. Default is False, which creates a text file.

    Returns:
    bool: True if the file was successfully created, False otherwise.

    Raises:
    Exception: If an error occurs during file creation.
    """
    try:
        if not binary:
            with open(os.path.join(path, fileName), 'w') as file:
                file.write('')
            return True
        else:
            with open(os.path.join(path, fileName), 'wb') as file:
                pickle.dump('', file)
            return True
    except Exception as e:
        print('An error occurred creating file named ', str(os.path.join(path, fileName)), ':', str(e))
        sys.exit()