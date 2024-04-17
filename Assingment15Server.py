#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:19:51 2019

@author: Azeng
Class: PRGM1000
Title: Assignment15 TCP Server
Version: 1.0
"""
import socket, psutil
from datetime import datetime
time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
boot = "System boot time: " + str(time)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostport = ("127.0.0.1", 19000)
server.bind(hostport)
server.listen(1)

for count in range (1,2):
    socket_client,address = server.accept()
    client = socket_client
    data = client.recvfrom(1024)
    info = data[0].decode()
    print(info)
    address = str(address)
    sending = "Msg from: " + address + " ---> " + boot
    encodinginfo = sending.encode()
    client.send(encodinginfo)
    client.close()
server.close()