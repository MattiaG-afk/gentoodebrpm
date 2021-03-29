#!/usr/bin/python3
import subprocess
import sys
import os
import getopt
import requests

if not len(sys.argv[1:]) or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("\033[1;31mUsage\033[0m\n: debrpm [OPTIONS] [FILE]\n")
    print("OPTIONS:")
    print("-h, --help\t\tShow this help message")
    print("-i, --install\t\tInstall a packet from the remote repository")
    print("-l, --local-install\tInstall a packet from a file .deb or .rpm")
    print("-s, --search\t\tSearch for a packet")
    print("-u, --update\t\tUpdate the local list of available packets in the repo")
else:
    if sys.argv[1] == '-i' or sys.argv[1] == '--install':
        print("AVAILABLE SOON")
    if sys.argv[1] == '-l' or sys.argv[1] == '--local-install':
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
            subprocess.run("sudo rm data.tar.xz", shell=True)
        elif file.find('.rpm') != -1:
            print("Installing the file: ", file)
            command = "rpm2tarxz " + file
            subprocess.run(command, shell=True)
            command = "rm " + file
            subprocess.run(command, shell=True)
            command = "mv " + file.replace(".rpm", ".tar.xz") + " /"
            subprocess.run(command, shell=True)
            os.chdir("/")
            command = "sudo tar xpvf " + file.replace(".rpm", ".tar.xz") + " >> /var/log/debrpm/" + file + ".log"
            subprocess.run(command, shell=True)
            command= "sudo rm " + file.replace(".rpm", ".tar.xz")
            subprocess.run(command, shell=True)
        else:
            print("Unknown file. Currently supported files are: .deb and .rpm")
    if sys.argv[1] == '-s' or sys.argv[1] == '--search':
        file = open('/var/db/repos/debrpm/packages.txt', 'r')
        find = 0
        packets = file.readlines()
        for packet in packets:
            if(packet.find(sys.argv[2])) != -1:
                find = find + 1
        if find != 0:
            print("Found " + str(find) + " matches")
        else:
            print("The package is not in the repository")
    if sys.argv[1] == '-u' or sys.argv[1] == '--update':
        print("Updating the /var/db/repos/debrpm/packages.txt file...")
        r = requests.get('https://raw.githubusercontent.com/MattiaG-afk/debrpm-repo/main/packages.txt', allow_redirects=True)
        open('/var/db/repos/debrpm/packages.txt', 'wb').write(r.content)
