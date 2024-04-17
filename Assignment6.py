# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:22:42 2019

@author: azeng
Class: PRGM 1000
Assignment 6: Functions
Version 1.0
"""
import shutil,os

def FName():
    return input("Okay, We are going to archive a folder!\nFirst we need a name: ")
def root():
    return input("Alright! now here comes the tricky part the Directory of the file we are going to archive(eg.C:/Whatever): ")
def dest():
    return input("Right-e-o! We need a Destination(eg. C:/Test): ")
FileName = FName()
#RootDir = root()
#DestDir = dest()
os.chdir(root())

#print(FileName,RootDir,DestDir)
#shutil.make_archive(FileName,zip[RootDir[DestDir]])
shutil.make_archive(FileName,"zip")