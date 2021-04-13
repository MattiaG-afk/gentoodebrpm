#!/usr/bin/python3
import subprocess
import sys
import os
import getopt
import requests

if not len(sys.argv[1:]) or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("\033[1;31mUsage\033[0m: debrpm [OPTIONS] [FILE]\n")
    print("OPTIONS:")
    print("-h, --help\t\tShow this help message")
    print("-i, --install\t\tInstall a packet from a file .deb or .rpm")
else:
    if sys.argv[1] == '-i' or sys.argv[1] == '--install':
        file = sys.argv[2]
        if file.find('.deb') != -1:
            print("Installing the file: ", file)
            command = "sudo ar x " + file
            subprocess.run(command, shell=True)
            subprocess.run("sudo rm debian-binary control.tar.xz", shell=True)
            subprocess.run("sudo mv data.tar.xz /", shell=True)
            os.chdir("/")
            command = "sudo tar xpvf data.tar.xz >> /var/log/debrpm/" + file + ".log"
            subprocess.run(command, shell=True)
            subprocess.run("rm /data.tar.xz", shell=True)
        elif file.find('.rpm') != -1:
            print("Installing the file: ", file)
            command = "rpm2tarxz " + file
            subprocess.run(command, shell=True)
            command = "rm " + file
            subprocess.run(command, shell=True)
            command = "mv " + file.replace(".rpm", ".tar.xz") + " /"
            subprocess.run(command, shell=True)
            os.chdir("/")
            command = "sudo tar xpvf /" + file.replace(".rpm", ".tar.xz") + " >> /var/log/debrpm/" + file + ".log"
            subprocess.run(command, shell=True)
            command= "rm /" + file.replace(".rpm", ".tar.xz")
            subprocess.run(command, shell=True)
        else:
            print("Unknown file. Currently supported files are: .deb and .rpm")
    else:
        print("\033[1;31mUsage\033[0m: debrpm [OPTIONS] [FILE]\n")
        print("OPTIONS:")
        print("-h, --help\t\tShow this help message")
        print("-i, --install\t\tInstall a packet from a file .deb or .rpm")
