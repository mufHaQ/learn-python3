#!/usr/bin/env python3

import os

path = "/home/haq/dev/python/learn-python3/_031_File-Detection/" + input("Masukkan nama file/folder: ")

if os.path.exists(path):
    print("That location exists!")

    if os.path.isfile(path):
        print("That is file")
    elif os.path.isdir(path):
        print("That is directory")

else:
    print("That location doesn't exists!")
