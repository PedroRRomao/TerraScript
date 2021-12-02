#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

All the getters of the script:

    - Templates list
    - Terraform bin version
    - The present date
    - The present time
    - Log file version

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"

import os
from datetime import date
import time
import run

## Gets all the templates from the template folder
def getTemplates(provider, template):

    templateList = []

    if template == None:
        templateList = os.listdir(run.templatesDir + str(provider))
    
    else:
        templateList.append(template)

    
    return templateList


## Costumize message depending on the user terraform version inserted on the input
def getTerraformVersion(bin):

    if bin == "terraform":

        return "most recent version from your environment"

    else:
        return "version " + bin[-2:]


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

# Gets the version from the files stored in the logs folder. The version is the last number on the name of the file and it will only change if the date on the file is the same
def getVersion(template):                           

    logs_files = os.listdir("logs")

    versions = []

    for log in logs_files:

        if template in log and getRealDate() in log:
            
            removeOut = log.replace(".out","")

            splited = removeOut.split("-")

            versions.append(int(splited[len(splited)-1]))

    if len(versions) == 0:
        
        return 1

    return (max(versions)+1) 

    