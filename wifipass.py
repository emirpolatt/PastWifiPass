"""
This script finds your wifi passwords saved in the past on Linux Systems.
This script currently only works on Linux Systems in v1 version.

Note:
    Pls run with "sudo"

Author: Emir Polat
Date: 22.06.2020

"""

import os, sys, time
import subprocess
import pyfiglet

assert ('linux' in sys.platform), "This script runs only Linux Systems"

# Class of the colors to be used on the terminal screen
class tColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'

def HelloMessage():
    helloMessage = "PastWIFIPass"
    description = tColors.OKGREEN + """
    This script finds your wifi passwords saved in the past(Only Linux).
    
    For use: You just have to give the 'Run' command.
    
    For Quit: Give the 'exit' command.
    
    Author: Emir Polat (@espday)
    """
    result = tColors.OKBLUE + pyfiglet.figlet_format(helloMessage)
    print(result)
    print(description)

HelloMessage()

detectOs = os.name

def LinuxSystems():
    allNetworks = "cd /etc/NetworkManager/system-connections/ && ls -1 | sed 's/\.[a-z]*$//'"
    command = os.popen(allNetworks)
    readCommand = command.read()
    print("\n" + tColors.WARNING + readCommand)
    print(tColors.WARNING + "-------------------------------- \n")

    selectWifi = input(tColors.OKBLUE + "Which Network ? \n" + tColors.OKBLUE + "\n>>> ")

    checkFile = os.path.exists("/etc/NetworkManager/system-connections/" + selectWifi + ".nmconnection")

    if checkFile == True:
        password = "sudo sed 's/^psk=//' /etc/NetworkManager/system-connections/" + selectWifi + ".nmconnection" + " | sudo sed '16!d' "
        passwordCommand = os.popen(password)
        readPass = passwordCommand.read()
        print("Password: " + readPass)
        time.sleep(0.5)
        sys.exit()
    else:
        print(tColors.FAIL + "\n <<<<< No such file! Try again by typing 'run' >>>>>")



while True:
    runCommand = input(tColors.HEADER + ">> ")

    if runCommand == "Run" or runCommand == "run":
        LinuxSystems()


    elif runCommand != "Run" and runCommand != "run" and runCommand != 'exit':
        print("You have logged in incorrectly. Please enter run command only")

    elif runCommand == 'exit':
        print("Good bye!")
        time.sleep(1)
        sys.exit()

# Linux and Mac systems == 'posix', Windows == 'nt'
if detectOs == 'posix':
    LinuxSystems()


