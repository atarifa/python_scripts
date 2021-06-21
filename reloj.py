# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:51:13 2021

@author: ansanchez
"""
from datetime import datetime
from time import sleep
from os import system


while True:
    dt=datetime.now()
    dt.strftime("%A %d %B %Y %I:%M")
    print("la hora actual es {}:{}:{}".format(dt.hour,dt.minute,dt.second))
    sleep(1)
    system("cls")