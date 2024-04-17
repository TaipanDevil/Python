# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:58:42 2019

@author: azeng
Class: PRGM 1000
Using Random Library
Version 1.0
"""
import random

print("A random first dice roll : ", int(random.randrange(1,7)))

rand1 = random.randint(1,7)
rand2 = random.randint(1,7)

print("Roll 1: ", rand1,"Roll 2: ", rand2, "Sum: ", (rand1+rand2))