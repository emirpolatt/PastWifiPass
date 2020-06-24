"""
This script finds your wifi passwords saved in the past on Linux Systems.
This script currently only works on Linux Systems in v1 version.

Note:
    Pls run with "sudo"

Author: Emir Polat
Date: 22.06.2020

"""

import os, sys
import pyfiglet
from time import sleep

assert ('linux' or 'windows' in sys.platform), "This script runs only Linux and Windows Systems"


# Class of the colors to be used on the terminal screen
class tColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'

if not os.getuid() == 0:
    sys.exit(tColors.FAIL + "Wifipass has to be run with root")

def HelloMessage():
    result = tColors.OKBLUE + pyfiglet.figlet_format("PastWIFIPass")
    print(result)

    description = tColors.OKGREEN + """
    This script finds your wifi passwords saved in the past(Only Linux, V1).
    
    For use: You just have to give the 'Run' command.
    
    For quit: Give the 'exit' command.
    
    Author: Emir Polat (@espday)
    """
    print(description)

HelloMessage()

detectOs = os.name

def LinuxSystems():
    # This is linux commands for the find of past wifi passwords.
    # Normally the files where wifi passwords are kept on Linux end with ".nmconnection".
    # With the sed command and the parameters we give afterwards, we delete this ".nmconnection" extension and show it to the user.
    # For example: wifi.nmconnection to -> Only: wifi
    allNetworks = "cd /etc/NetworkManager/system-connections/ && ls -1 | sed 's/\.[a-z]*$//'"
    command = os.popen(allNetworks)
    readCommand = command.read()
    print("\n" + tColors.WARNING + readCommand)
    print(tColors.WARNING + "-------------------------------- \n")

    selectWifi = input(tColors.OKBLUE + "Which Network ? \n" + tColors.OKBLUE + "\n>>> ")

    if selectWifi == 'exit':
        print("Good bye")
        sleep(0.5)
        sys.exit()

    # We check if there is a file with the entered value -> selecWifi
    checkFile = os.path.exists("/etc/NetworkManager/system-connections/" + selectWifi + ".nmconnection")

    if checkFile == True:
        #  If there is such a file; By taking root permissions, we go to the required directory,
        #  delete the 'psk =' value where the password is kept,
        #  and by calling only the 16th line of the file with many lines, we only get the password.
        password = "sudo sed 's/^psk=//' /etc/NetworkManager/system-connections/" + selectWifi + ".nmconnection" + " | sudo sed '16!d' "
        passwordCommand = os.popen(password)
        readPass = passwordCommand.read()
        print("Password: " + readPass)
        sleep(0.5)
        sys.exit()
    else:
        print(tColors.FAIL + "\n <<<<< No such file! Try again by typing 'run' >>>>>")

def WinSystems():
    allNetworks = "netsh wlan show profile key=clear"
    command = os.popen(allNetworks)
    readCommand = command.read()
    print("\n" + tColors.WARNING + readCommand)
    print(tColors.WARNING + "-------------------------------- \n")

    selectWifi = input(tColors.OKBLUE + "Which Network ? \n" + tColors.OKBLUE + "\n>>> ")

    if selectWifi == 'exit':
        print("Good bye")
        sleep(0.5)
        sys.exit()

    checkFile = os.path.exists("/etc/NetworkManager/system-connections/" + selectWifi + ".nmconnection")

    if checkFile == True:
        #  If there is such a file; By taking root permissions, we go to the required directory,
        #  delete the 'psk =' value where the password is kept,
        #  and by calling only the 16th line of the file with many lines, we only get the password.
        password = "netsh wlan show profile name=" + selectWifi + "key=clear"
        passwordCommand = os.popen(password)
        readPass = passwordCommand.read()
        print("Password: " + readPass)
        sleep(0.5)
        sys.exit()
    else:
        print(tColors.FAIL + "\n <<<<< No such Wifi Name! Try again by typing 'run' >>>>>")

while True:
    runCommand = input(tColors.HEADER + ">> ")

    if runCommand == "Run" or runCommand == "run":
        LinuxSystems()

    elif runCommand == 'exit':
        print("Good bye!")
        sleep(0.5)
        sys.exit()

    else:
        print("You have logged in incorrectly. Please enter run command only")

# Linux and Mac systems == 'posix', Windows == 'nt'
if detectOs == 'posix':
    LinuxSystems()

elif detectOs == "nt":
    WinSystems()

else:
    sleep(0.5)
    sys.exit(tColors.WARNING + "Coming Soon ...")


