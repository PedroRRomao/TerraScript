import os
import shutil
import subprocess
import sys
from shutil import copytree, ignore_patterns, rmtree
from datetime import date
import argparse
from subprocess import DEVNULL
import _thread
import time


startTime = time.time()

dir_path = os.path.dirname(os.path.realpath(__file__))

templatesDir = "{}/templates/".format(dir_path)
tmpDir = "{}/tmp/".format(dir_path)
version = 1
limiteThread = 3                                            ## Define here the number of threads running at the same time
processingCount = 0

def main():

    terraVersion = getTerraformVersion(binTerraform)
    print("Hello, your script is starting with terraform " + terraVersion)
    check_if_folders_exist()                                        # checks if the skeleton (folders in directories) for the script is created. If not, the folders missing will be created
    check_if_templates_empty(providerFolder)                        # checks if providers template folder is empty and sends a message to place something so the program can work
    templateList = getTemplates(providerFolder, templateName)       # get the templates list
    check_if_tmp_empty()                                            # check if the tmp folder is empty, if it is not, you will be asked to clean it before running the script again
    createTmpFolder(templateList, providerFolder)                   # creates the tmp folders from the templates list
    queue(tuple(templateList))                                      # A queue to run the threads for the terraform templates. The maximum is the number on the variable limiteThread 
    #clear_tmp()

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

## Costumize message depending on the user terraform version inserted on the input
def getTerraformVersion(bin):

    if bin == "terraform":

        return "most recent version from your environment"

    else:
        return "version " + bin[-2:]

## Gets all the templates from the template folder
def getTemplates(provider, template):

    templateList = []

    if template == None:
        templateList = os.listdir(templatesDir + str(provider))
    
    else:
        templateList.append(template)

    
    return templateList

def getRealDate():                                          

    data = date.today()
    joinData = str(data).replace("-", "")
    return joinData

# Gets the version from the files stored in the logs folder. The version is the last number on the name of the file and it will only change if the date on the file is the same
def getVersion(template):                           

    logs_files = os.listdir("logs")

    versions = []

    for log in logs_files:

        if template in log and getRealDate() in log:
            
            removeOut = log.replace(".out","")

            splited = removeOut.split("-")

            versions.append(int(splited[len(splited)-1]))

    if len(versions) == 0:
        
        return 1

    return (max(versions)+1) 

## Inserts the templates in the tmp folder
def createTmpFolder(templates, provider):

    for template in templates:

        src = templatesDir + provider + "/" + template
        copytree(src, tmpDir + template, ignore=ignore_patterns('*.git'))

## Creates the skeleton of the project if it doesnt already exist
def check_if_folders_exist():

    listFolders = set(os.listdir())

    if not "templates" in listFolders:
        os.mkdir("templates")
    
    if not "tmp" in listFolders:
        os.mkdir("tmp")

    if not "logs" in listFolders:
        os.mkdir("logs")

    subFolders = set(os.listdir("templates"))

    if not "azure" in subFolders:
         os.mkdir("templates/azure")

    if not "aws" in subFolders:
         os.mkdir("templates/aws")

    if not "gcp" in subFolders:
         os.mkdir("templates/gcp")

    if not "operacao" in subFolders:
         os.mkdir("templates/operacao")

def check_if_tmp_empty():

    if len(os.listdir(tmpDir)) > 0:
        print("In order to proceed the tmp folder needs to be empty")
        sys.exit()

def check_if_templates_empty(provider):

    if len(os.listdir(templatesDir + provider)) == 0:
        print("The " + provider + " folder is empty. How can i work with all this empty space? Insert something so i can get back to work")
        sys.exit()

## The queue for the threads. Receives the full template list. Updates the list as the templates exit the queue.
def queue(temp_list):

    global processingCount

    try:
    
        if len(temp_list) >= 1 and processingCount < limiteThread:

            slots = limiteThread-processingCount
            tupNew = temp_list[0:slots]
            runThread(tupNew)
            temp_list = temp_list[slots:]
            queue(temp_list)

        while (processingCount == limiteThread) or (processingCount!=0 and len(temp_list) < limiteThread):
            time.sleep(10)
            queue(temp_list)
        

    except:
        print("Error: unable to start thread")


def runThread(listForThread):

    global processingCount

    try:

        processingCount +=1
    
        _thread.start_new_thread( runTerraform, (listForThread, 2) )

    except _thread.error:
        print("Error in thread ")

## Where the thread enters to run the template
def runTerraform(templates, delay):
    
    global processingCount

    for template in templates:

        version = getVersion(template)
        logFile = "logs/" + template + "-" + getRealDate() + "-" + str(version) + ".out"
        print("- Analysing provider " + providerFolder + " template " + template)
        time.sleep(delay)
        subprocess.run(binTerraform + " -chdir=" + tmpDir + template + " init", shell=True, stdout=DEVNULL)
        sp=subprocess.run(binTerraform + " -chdir="+tmpDir + template+" plan -no-color", shell=True, capture_output=True)
        writeOutput(logFile, sp.stdout, sp.stderr, providerFolder, template)

    processingCount -= 1

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
    
def getTime():

    seconds = round(time.time() - startTime)
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    print("Execution time: %dh:%02dm:%02ds" % (hour, minutes, seconds))

def clear_tmp():
    shutil.rmtree(tmpDir)


if __name__ == "__main__":
    
    providerFolder  = getArguments()[0]
    binTerraform    = getArguments()[2]

    if providerFolder == None:
        providerFolder = "azure"

    if binTerraform == None:
        binTerraform = "terraform"

    templateName = getArguments()[1]
    
    main()

    getTime()