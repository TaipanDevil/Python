# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:42:55 2019

@author: azeng
Class: PGRM1000
Title: Assignment 11
Code From Flow Chart
"""
import sys,os

while(len(sys.argv) >= 2):
    try:
        os.path.exists(sys.argv[1])
        F = open(sys.argv[1])
        File = F.readlines()
        F.close()
        for L in File:
            A = L.split()
            print(A)
    except ValueError:
        print("File is not readable")