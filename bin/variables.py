#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Static variables and variables to modify the running of the script.
Change the maxThread variable to specify the maximum number of threads running
Change providersList to build your own provider skeleton folders

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"

import bin.console as console


########### static variable, dont edit ########################

version = 1

processingCount = 0         

###############################################################

maxThread = 3                                                       # Define here the number of threads running at the same time

providersList = ["aws", "azure", "gcp", "operacao"]

providerFolder  = console.getArguments()[0]
binTerraform    = console.getArguments()[2]

if providerFolder == None:
    providerFolder = "azure"

if binTerraform == None:
    binTerraform = "terraform"

templateName = console.getArguments()[1]