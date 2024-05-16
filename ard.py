"""
this python file ard stands for auto requirement download.
This python module can be just imported and the init function can be imported from it and the 
absolute path of the requirement can be passed as argument and can be left blank for the 
file in the same directory.
"""

import os
import sys
import time
import subprocess

errorMsg = "This is a fault with the library not your code!"

def checkFile(filePath):
    try:
        if os.path.exists(filePath):
            return True
        elif not os.path.exists(filePath):
            return False
        else:
            print(f'An unknown error occured in checkFile()!\n{str(errorMsg)}')
            sys.exit()
    except Exception as e:
        print(f'An error occured in checkFile(): {str(e)}\n{errorMsg}')
        sys.exit(-1)

def init(filePath=None):
    try:
        if checkFile(filePath) == True:
            with open(filePath, 'r') as file:
                reqs = file.readlines()
                file.close()
            if len(reqs) > 0:
                print(f'Found {str(len(reqs))} Requirements!')
            for req in reqs:
                print(f'Installing rquirement : {str(req)}')
                t1 = time.time()
                x = subprocess.run(f'pip install {str(req).strip()}', shell=True, stdout=subprocess.DEVNULL)
                t2 = time.time()
                if x.returncode != 0:
                    print(f'Installation Failed with status code : {str(x.returncode)}!')
                else:
                    print(f'[+] Installed {str(req)}, time elapsed : {str(round(t2 - t1, 2))} seconds...')
            print(f'\nInstalled requirements {str(len(reqs))} sucessfully!\nYour program will execute in 5 seconds...')
            time.sleep(5)
            subprocess.run('clear', shell=True)
        elif checkFile(filePath) == False:
            print(f'Requirements.txt not found, leaving it. Running the code directly.')
    except Exception as e:
        print(f'An error occured in init(): {str(e)}\n{errorMsg}')
        sys.exit(-1)
