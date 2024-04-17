# -*- coding: utf-8 -*-
"""
Spyder Editor

Andrew Zeng 
PRGM1000

Decimal to Hex and Binary
"""
User1 = input("Enter a number: ")
User2 = input("Enter a second number: ")

First = int(User1)
Second = int(User2)

One = hex(First)
Two = hex(Second)
Three = bin(First)
Four = bin(Second)

print(
      First, "is ", One,"in hex and ", Three," in binary.")

print(
      Second, "is ", Two,"in hex and ", Four,"in binary.")