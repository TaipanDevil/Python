# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:04:27 2019

@author: azeng
Course:PGRM1000
Title: Assignment 10 - Collections
Version: 1.0
"""
def Fruit():
    F = open("C:\\Test\\fruit.txt","r")

    Raw1 = F.read()
    print(Raw1)
    F.close()

Fruit()
print()

f = open("C:\\test\\fruit.txt","r")
numbers = f.readlines()
print(numbers.sort())
for num in numbers:
    if(len(num) == 5):
        print(num)