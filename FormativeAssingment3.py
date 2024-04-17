# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:48:38 2019

Andrew Zeng

Formative Activity 3

https://www.pluralsight.com/blog/it-ops/simplify-routing-how-to-organize-your-network-into-smaller-subnets
"""
IP = input("Enter an IPv4 address: ")
Subnet = input("Enter a Subnet mask: ")

OctectIP = list(IP.split("."))
byteIP0 = (int(OctectIP[0]))
byteIP1 = (int(OctectIP[1]))
byteIP2 = (int(OctectIP[2]))
byteIP3 = (int(OctectIP[3]))

OctectNet = list(Subnet.split("."))
byteNet0 = (int(OctectNet[0]))
byteNet1 = (int(OctectNet[1]))
byteNet2 = (int(OctectNet[2]))
byteNet3 = (int(OctectNet[3]))

bit3 = byteIP0 & byteNet0
bit2 = byteIP1 & byteNet1
bit1 = byteIP2 & byteNet2

if byteNet3 == 0:
    HostNum = 253 - byteNet3
else:
    HostNum = byteIP3 & byteNet3

print(bit3,".",bit2,".",bit1," is the network number and ",HostNum," is the number of hosts.")