#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Module with all the functions to run one or more threads.
Uses a queue and runs the threads

"""
__author__= "Pedro Filipe Rosa Gonçalves Romão"

import subprocess
from subprocess import DEVNULL
import _thread
import time
import bin.output as output
#import complement.versions as version
import bin.execution_time as execution_timer
import run

## The queue for the threads. Receives the full template list. Updates the list as the templates exit the queue.
def queue(temp_list, provider, bin):

    try:
    
        if len(temp_list) >= 1 and run.processingCount < run.maxThread:

            slots = run.maxThread-run.processingCount
            tupNew = temp_list[0:slots]
            runThread(tupNew, provider, bin)
            temp_list = temp_list[slots:]
            queue(temp_list, provider, bin)

        while (run.processingCount == run.maxThread) or (run.processingCount!=0 and len(temp_list) < run.maxThread):
            time.sleep(10)
            queue(temp_list, provider, bin)
        

    except:
        print("Error: unable to start thread")


def runThread(listForThread, provider, bin):

    try:

        run.processingCount +=1
    
        _thread.start_new_thread( runTerraform, (listForThread, 2, provider, bin) )

    except _thread.error:
        print("Error in thread ")

## Where the thread enters to run the template
def runTerraform(templates, delay, provider, bin):

    for template in templates:
        #version = version.getVersion(template)
        #logFile = "logs/" + template + "-" + getRealDate() + "-" + str(version) + ".out"
        logFile = "logs/{}-{}.out".format(template, execution_timer.getRealDate())
        print("- Analysing provider {} template {}".format(provider, template))

        time.sleep(delay)
        subprocess.run("{} -chdir={}{} init".format(bin, run.tmpDir, template), shell=True, stdout=DEVNULL)
        sp=subprocess.run("{} -chdir={}{} plan -no-color".format(bin, run.tmpDir, template), shell=True, capture_output=True)
        output.writeOutput(logFile, sp.stdout, sp.stderr, provider, template)
    
    run.processingCount -= 1
