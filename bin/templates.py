#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Function to get all Templates list

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"

import os
import run
import bin.threads as threads

## Gets all the templates from the template folder
def allTemplates(provider = "azure", template = None):

    if template == None:
        return os.listdir(run.templatesDir + str(provider))

    return [template]


    