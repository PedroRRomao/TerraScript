#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Functions to calculate the execution time of the script

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"

import run
from datetime import date
import time

def getRealDate():                                          

    data = date.today()
    joinData = str(data).replace("-", "")
    return joinData

def getTime():

    seconds = round(time.time() - run.startTime)
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    print("Execution time: %dh:%02dm:%02ds" % (hour, minutes, seconds))