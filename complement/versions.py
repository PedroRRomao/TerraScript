#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Function to get a specific version by analysing the templates inside log folder.
Checks the date and if the date is the same, checks the last digit.
If there is no digit then appends 1 if there is a digit then + 1 to the digit.

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"

import os
import bin.execution_time as time

#### If you dont want to delete the log files then use this version function on the end of the log file string to have versions depending on the date ############################

# Gets the version from the files stored in the logs folder. The version is the last number on the name of the file and it will only change if the date on the file is the same
def getVersion(template):                           

     logs_files = os.listdir("logs")

     versions = []

     for log in logs_files:

         if template in log and time.getRealDate() in log:
            
             removeOut = log.replace(".out","")

             splited = removeOut.split("-")

             versions.append(int(splited[len(splited)-1]))

     if len(versions) == 0:
        
         return 1

     return (max(versions)+1) 