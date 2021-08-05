#!/usr/bin/env python3

# copyfile(): copies contents of a file
# copy()    : copyfile() + permission mode + destination, can be ad directory
# copy2()   : copy() + copies metadata (file's creation and modification times)

import shutil
import os


# os.mkdir('cpy')
# shutil.copyfile('main.txt', 'cpy/copy.txt')
shutil.copytree('cpy', 'new_cpy')
