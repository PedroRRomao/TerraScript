#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Console input and console output

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"

import argparse


## Get the arguments from the terminal
def getArguments():

    argList = []
    # Initialize parser
    parser = argparse.ArgumentParser()
 
    # Adding optional argument
    parser.add_argument("-p", "--Provider", help = "The cloud provider")
    parser.add_argument("-t", "--Template", help = "Name of the template")
    parser.add_argument("-b", "--Bin", help = "Terraform bin")
 
    # Read arguments from command line
    args = parser.parse_args()

    argList.append(args.Provider)
    argList.append(args.Template)
    argList.append(args.Bin)

    return argList


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
