#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Checks if the folder where the script is running as the correct folders skeleton and if not creates it

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"


import os
import shutil
import sys
from shutil import copytree, ignore_patterns, rmtree
import run


def check_if_folders_exist():

    for path_template in ["tmp", "logs"]:
        os.makedirs("{}".format(path_template), exist_ok=True)

    # templates
    for path_template in ["azure", "aws", "gcp", "operacao"]:
        os.makedirs("templates/{}".format(path_template), exist_ok=True)


def check_if_tmp_empty():

    if len(os.listdir(run.tmpDir)) > 0:
        print("In order to proceed the tmp folder needs to be empty")
        sys.exit()

def check_if_templates_empty(provider):

    if len(os.listdir(run.templatesDir + provider)) == 0:
        print("The " + provider + " folder is empty. How can i work with all this empty space? Insert something so i can get back to work")
        sys.exit()

## Inserts the templates in the tmp folder
def createTmpFolder(templates, provider):

    for template in templates:

        src = run.templatesDir + provider + "/" + template
        copytree(src, run.tmpDir + template, ignore=ignore_patterns('*.git'))



def create_skeleton(createList, provider):

    check_if_folders_exist()                                                    # checks if the skeleton (folders in directories) for the script is created. If not, the folders missing will be created
    check_if_templates_empty(provider)                                          # checks if providers template folder is empty and sends a message to place something so the program can work
    check_if_tmp_empty()                                                        # check if the tmp folder is empty, if it is not, you will be asked to clean it before running the script again
    createTmpFolder(createList, provider)                                       # creates the tmp folders from the templates list



            
def clear_tmp():

    try:
        shutil.rmtree(run.tmpDir)
    except:
        pass