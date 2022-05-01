#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Console input

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"

import argparse


## Get the arguments from the terminal
def getArguments():

    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("-p", "--provider", help = "The cloud provider", default = "azure")
    parser.add_argument("-t", "--template", help = "Name of the template")
    parser.add_argument("-b", "--bin", help = "Terraform bin", default = "terraform")
 
    # Read arguments from command line
    args = parser.parse_args()
    
    
    return args

## Costumize message depending on the user terraform version inserted on the input
def terraformVersion(bin):

    if bin == "terraform":

        return "most recent version from your environment."

    else:
        return "version " + bin[-2:]
