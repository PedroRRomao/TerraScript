#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main function
Terraform script to run X number of modules at the same time.

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"

import os
import time
import bin.getters as get
import bin.skeleton as skl
import bin.threads as trd
import bin.variables as var

startTime = time.time()

dir_path = os.path.dirname(os.path.realpath(__file__))

templatesDir = "{}/templates/".format(dir_path)
tmpDir = "{}/tmp/".format(dir_path)
logsDir = "{}/logs/".format(dir_path)

def main():

    terraVersion = get.getTerraformVersion(var.binTerraform)
    print("Hello, your script is starting with terraform " + terraVersion)
    templateList = get.getTemplates(var.providerFolder, var.templateName)
    skl.create_skeleton(templateList)                                                   # get the templates list
    trd.queue(tuple(templateList))                                                    # A queue to run the threads for the terraform templates. The maximum is the number on the variable limiteThread 
    #clear_tmp()


if __name__ == "__main__":
    
    main()

    get.getTime()

