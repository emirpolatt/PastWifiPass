"""
This script finds your wifi passwords saved in the past on Linux and Windows Systems.
This script currently only works on Linux and Windows in v1 version but there might be some errors in windows systems.
Runs smoothly on Linux.

Author: Emir Polat
Date: 22.06.2020

"""

import os, sys
from subprocess import check_output
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

def banner():
    print(tColors.OKBLUE+" ____           _ __        _____ _____ ___ ____ ")
    print(tColors.OKBLUE+"|  _ \ __ _ ___| |\ \      / /_ _|  ___|_ _|  _ \ __ _ ___ ___  ")
    print(tColors.OKBLUE+"| |_) / _` / __| __\ \ /\ / / | || |_   | || |_) / _` / __/ __| ")
    print(tColors.OKBLUE+"|  __/ (_| \__ \ |_ \ V  V /  | ||  _|  | ||  __/ (_| \__ \__ \ ")
    print(tColors.OKBLUE+"|_|   \__,_|___/\__| \_/\_/  |___|_|   |___|_|   \__,_|___/___/ ")

    description = tColors.OKGREEN + """
    This script finds your wifi passwords saved in the past(Only Linux and Windows Systems, V1).
    
    For use: You just have to give the 'Run' command.
    
    For quit: Give the 'exit' command.
    
    Author: Emir Polat (@espday)
    """
    print(description)

banner()

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
    allNetworks = check_output("netsh wlan show profile", shell=True)
    print("\n" + tColors.WARNING + str(allNetworks))
    print(tColors.WARNING + "-------------------------------- \n")

    selectWifi = input(tColors.OKBLUE + "Which Network ? \n" + tColors.OKBLUE + "\n>>> ")

    if selectWifi == 'exit':
        print("Good bye")
        sleep(0.5)
        sys.exit()

    passwordCommand = check_output("netsh wlan show profile name="+ selectWifi +" key=clear", shell=True)
    print("Password: " + str(passwordCommand))
    sleep(0.5)
    sys.exit()

while True:
    runCommand = input(tColors.HEADER + ">> ")

    if runCommand == "Run" or runCommand == "run":
        # Linux and Mac systems = 'posix', Windows Systems = 'nt'
        if detectOs == 'posix':
            LinuxSystems()
        elif detectOs == 'nt':
            WinSystems()
        else:
            print("Coming Soon ...")
            sleep(0.5)
            sys.exit()

    elif runCommand == 'exit':
        print("Good bye!")
        sleep(0.5)
        sys.exit()

    else:
        print("You have logged in incorrectly. Please enter run command only")


