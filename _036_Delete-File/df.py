#!/usr/bin/env python3

import os, shutil, sys

source = "test"

try:
    os.remove(source)    
except FileNotFoundError as fnfe:
    sys.exit(f"Error: {fnfe}")
except PermissionError as pe:
    sys.exit(f"Error: {pe}")
except OSError:
    inpt = input(f"Do you want delete this folder ({source}) and its file?: ")
    if inpt == 'y':
        shutil.rmtree(source) # Use shutil.rmtree(src) for deleteing folder that contains file 
        exit()
else:
    print(source, "was deleted")
