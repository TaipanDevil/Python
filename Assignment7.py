# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:52:12 2019

@author: azeng

Title: Assignment 7

"""
from datetime import datetime
import os,sys

def NowHere():
    Here = datetime.now()
    date = Here.strftime("%Y:%m:%d")
    time = Here.strftime("%H:%M:%S")
    return date,time

def Where():
    path = input("Name a file directory to count the files(C:/Whatever): ")
    return os.listdir(path)

print("The date and time is: ",NowHere())
print("\nThe number of files in your location is",len(Where()))

sys.argv[0]
print("\nThere are",len(sys.argv), " command line parameters passed in this script")