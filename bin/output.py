#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Console output

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"


## The output on the console
def writeOutput(file, output, error, provider, template):

    red = "\033[0;31m"
    green = "\033[32m"
    reset = '\033[0m'

    if len(output) == 0:
        with open(file, "wb") as fp:
                fp.write(error)
        print(red + "- The template " + template + " as generated an Error message!" + reset)
    else:
        with open(file, "wb") as fp:
                fp.write(output)
        print(green + "- Analyses complete of provider " + provider + " template " + template + reset)