#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main function
Terraform script to run X number of modules at the same time.

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"

import os
import time
import bin.templates as get
import bin.skeleton as skeleton
import bin.threads as thread
import bin.input as input
import bin.execution_time as execution_time

startTime = time.time()

dir_path = os.path.dirname(os.path.realpath(__file__))

templatesDir = "{}/templates/".format(dir_path)
tmpDir = "{}/tmp/".format(dir_path)
logsDir = "{}/logs/".format(dir_path)

########### static variable, dont edit ########################

version = 1

processingCount = 0         

###############################################################

maxThread = 3                                                                                             # Define here the number of threads running at the same time

def main():

    provider = parameters.provider
    template = parameters.template
    bin = parameters.bin

    print("\033[0;33m Hello, your script is starting with terraform's " + input.terraformVersion(bin) + "\033[0m")
    skeleton.create_skeleton(provider)                                                                            # creates athe skeleton if firt time using
    templateList = get.allTemplates(provider, template)                                                   # get the templates list
    skeleton.createTmpFolder(templateList, provider)
    thread.queue(tuple(templateList), provider, bin)                                                      # A queue to run the threads for the terraform templates. The maximum is the number on the variable limiteThread 
    skeleton.clear_tmp()

if __name__ == "__main__":

    parameters = input.getArguments()

    main()

    execution_time.getTime()

