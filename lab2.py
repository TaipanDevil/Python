# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:01:58 2019

@author: azeng
Class: PGRM1000
Title: Lab 2
Version: 1.0
"""
import sys,os

if(len(sys.argv) >= 3):
    if(os.path.exists(sys.argv[1])):
        try:
            file = open(sys.argv[1])
            #Lines = file.split()
            for "%PIX-3-106014" in file:
                Lines
                hits = 0
                for ("src outside:", sys.argv[3]) in Lines:
                    hits += 1
            print(hits)
        except IOError:
            print("ERROR: IP address not found.")
    else:
        print("ERROR: File Path Not Found.")
elif(len(sys.argv) < 3):
    print("Expecting more command line parameters: Python **Lab2.py 192.168.1.1")
    