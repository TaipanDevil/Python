#!/usr/bin/python3 
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 08:15:55 2019

@author: azeng
Class: PGRM1000
Title: Assignement 14
Version. 1.0
"""
import socket

local = socket.socket()
remote = ("192.168.91.138" , 17)
local.connect(remote)
local.send(b" ")
Buffer = local.recv(512)
local.close()
string = Buffer.decode()
print("Today's Quote of the Day is: {}".format(string))