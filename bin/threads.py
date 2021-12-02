#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Uses a queue and runs the threads

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"

import subprocess
from subprocess import DEVNULL
import _thread
import time
import bin.variables as var
import bin.console as csl
import bin.getters as get
import run



## The queue for the threads. Receives the full template list. Updates the list as the templates exit the queue.
def queue(temp_list):

    try:
    
        if len(temp_list) >= 1 and var.processingCount < var.maxThread:

            slots = var.maxThread-var.processingCount
            tupNew = temp_list[0:slots]
            runThread(tupNew)
            temp_list = temp_list[slots:]
            queue(temp_list)

        while (var.processingCount == var.maxThread) or (var.processingCount!=0 and len(temp_list) < var.maxThread):
            time.sleep(10)
            queue(temp_list)
        

    except:
        print("Error: unable to start thread")


def runThread(listForThread):

    try:

        var.processingCount +=1
    
        _thread.start_new_thread( runTerraform, (listForThread, 2) )

    except _thread.error:
        print("Error in thread ")



## Where the thread enters to run the template
def runTerraform(templates, delay):

    for template in templates:

        version = get.getVersion(template)
        logFile = "logs/" + template + "-" + get.getRealDate() + "-" + str(version) + ".out"
        print("- Analysing provider " + var.providerFolder + " template " + template)
        time.sleep(delay)
        subprocess.run(var.binTerraform + " -chdir=" + run.tmpDir + template + " init", shell=True, stdout=DEVNULL)
        sp=subprocess.run(var.binTerraform + " -chdir="+ run.tmpDir + template+" plan -no-color", shell=True, capture_output=True)
        csl.writeOutput(logFile, sp.stdout, sp.stderr, var.providerFolder, template)

    var.processingCount -= 1
