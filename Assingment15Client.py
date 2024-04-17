#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:14:56 2019

@author: Azeng
Class: PRGM1000
Title: Assignment15 TCP Client
Version: 1.0
"""
import socket

local = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
remote = ("127.0.0.1", 19000)
local.connect(remote)
local.send(b" ")
data = local.recv(1024)
local.close()
string = data
print(data.decode())