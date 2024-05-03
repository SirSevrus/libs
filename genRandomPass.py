import random
import string

def genDigitsOnly(length=16):
    """
    The function generates a random string consisting only of numbers of the length provded by the user.  
    By default length is 16.
    Basic Example Usage:
    length = 100
    genDigitsOnly(length) # The function returns the string.   
    """

    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    password = ''
    count = 1
    item = random.choice(digits)
    password += str(item)
    while count < length:
        item = random.choice(Digits)
        password += str(item)
        count += 1
    return password

def genLowerCaseOnly(length=16):
    """
    This Function generates a random string consisting of only lower case letters of the length provided by the user.
    By default length is 16.
    Basic Example:
    length = 100
    genLowerCaseOnly(length)  # the function returns the string.
    """
    alphabets = string.ascii_lowercase
    password = ''
    for i in range(length):
        item = random.choice(alphabets)
        password += item
    print(password)

def genUpperCaseOnly(length=16):
    """
    This Function generates a random string consisting of only upper case letters of the length provided by the user.
    By default length is 16.
    Basic Example:
    length = 100
    genUpperCaseOnly(length)  # the function returns the string.
    """
    alphabets = string.ascii_uppercase
    password = ''
    for i in range(length):
        item = random.choice(alphabets)
        password += item
    print(password)

def genMixedAlphabets(length=16):
    """
    This Function generates a random string consisting of lower case letters and upper case letters of the length provided by the user.
    By default length is 16.
    Basic Example:
    length = 100
    genMixedAlphabets(length)  # the function returns the string.
    """
    alphabets = string.ascii_uppercase + string.ascii_lowercase
    password = ''
    for i in range(length):
        item = random.choice(alphabets)
        password += item
    print(password)

def genMixed(length=16):
    """
    This Function generates a random string consisting of lower case letters, upper case letters, numbers and underscore (_) of the length provided by the user.
    By default length is 16.
    Basic Example:
    length = 100
    genMixed(length)  # the function returns the string.
    """
    alphabets = string.ascii_uppercase + string.ascii_lowercase + '_0123456789' 
    password = ''
    for i in range(length):
        item = random.choice(alphabets)
        password += item
    print(password)

# Example Usage
# genDigitsOnly(1000)
# genLowerCaseOnly(100)
# genUpperCaseOnly(100)
# genMixedAlphabets(100)
# genMixed()