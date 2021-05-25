#!/usr/bin/python3
import os, sys, subprocess
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showinfo, showerror
from tkinter import *

options = {}
log_dir = '/var/log/debrpm'
tmp_dir = '/var/tmp/debrpm'

def fillEntry(entry, value):
    entry.delete(0, END)
    entry.insert(0, value)

def installFile(file, root='/'):
    try:
        log_file = os.path.join(log_dir, file + '.log')
        open(log_file, 'w').write('Root directory:' + root)
        if file.find('.deb') != -1:
            print("Installing the file:", file)
            subprocess.run("sudo cp %s %s" % (os.path.join(os.curdir, file), os.path.join(tmp_dir, file)), shell=True)
            os.chdir(tmp_dir)
            subprocess.run("sudo ar x %s" % os.path.join(tmp_dir, file), shell=True)
            subprocess.run("rm -f %s %s" % (os.path.join(tmp_dir, "debian-binary"), os.path.join(tmp_dir, "control.tar.xz")), shell=True)
            subprocess.run("sudo tar xpvf %s >> %s" % (os.path.join(tmp_dir, "data.tar.xz"), log_file), shell=True)
            subprocess.run("rm -f %s" % os.path.join(tmp_dir, "data.tar.xz"), shell=True)
            subprocess.run("mv %s %s" % (os.path.join(tmp_dir, "*"), root), shell=True)
            showinfo('Debrpm GUI', 'Package installed successfully')
        elif file.find('.rpm') != -1:
            print("Installing the file:", file)
            subprocess.run("sudo cp %s %s" % (os.path.join(os.curdir, file), os.path.join(tmp_dir, file)), shell=True)
            os.chdir(tmp_dir)
            subprocess.run("rpm2tarxz %s" % os.path.join(os.curdir, file), shell=True)
            subprocess.run("sudo tar xpvf %s >> %s" % (os.path.join(os.curdir, file.replace(".rpm", ".tar.xz")), log_file), shell=True)
            subprocess.run("rm -f %s %s" %(os.path.join(os.curdir, file), os.path.join(os.curdir, file.replace(".rpm", ".tar.xz"))), shell=True)
            subprocess.run("mv %s %s" % (os.path.join(tmp_dir, "*"), root), shell=True)
            showinfo('Debrpm GUI', 'Package installed successfully')
        else:
            showerror('Debrpm GUI', 'Unknown file. Currently supported files are: .deb and .rpm')
    except:
        showerror('Debrpm GUI', 'An error occurred:\n%s' % sys.exc_info)

def uninstallFile(packet):
    try:
        packet = os.path.join(log_dir, packet)
        if not packet.endswith('.log'):
            packet += '.log'
        packet_log = open(packet)
        root = packet_log.readline().split('Root directory:')[1].replace('./','')
        dir = []
        if root != '/':
            for line in packet_log.readlines():
                remove = root.replace('\n', '') + line.replace('\n', '').replace('./', '/')
                if os.path.isdir(remove):
                    dir.append(remove)
                else:
                    subprocess.run('rm -f ' + line.replace('\n', ''), shell=True)
            dir.sort()
            dir.reverse()
            for directory in dir:
                subprocess.run('rmdir ' + directory, shell=True)
            subprocess.run("rm -f %s" % os.path.join(log_dir, packet), shell=True)
        showinfo('Debrpm GUI', 'Package uninstalled successfully')
    except:
        showerror('Debrpm GUI', 'An error occurred: \n%s' % sys.exc_info)

def listInstalled():
    packageDescription = [['Name:', 'Type:', 'Log file:']]
    listWindow = Toplevel()
    listWindow.tk.call('wm', 'iconphoto', listWindow._w, PhotoImage(file='/usr/share/pixmaps/debrpm-GUI.png'))
    listWindow.resizable(width=0, height=0)
    index = 0
    for file in os.listdir(log_dir):
        if file.endswith('.log'):
            index += 1
            packageDescription.append([file.replace('.deb.log', ''), "deb" if ".deb" in file else "rpm", os.path.join(log_dir, file)])
    ii = 0
    for i in packageDescription:
        jj = 0
        for j in i:
            Label(listWindow, text=j).grid(row=ii, column=jj)
            jj += 1
        ii += 1
    Label(listWindow, text='Number of installed packages: %s' % index).grid()
    listWindow.grab_set()
    listWindow.focus_set()
    listWindow.wait_window()

root = Tk()
root.title('Debrpm GUI')
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='/usr/share/pixmaps/debrpm-GUI.png'))

row = Frame(root)
Label(row, text='Select the file that you want to install:').pack(side=LEFT, fill=BOTH)
file = Entry(row)
file.pack(side=LEFT, expand=YES, fill=X)
Button(row, text='Browse file', command=(lambda: fillEntry(file, askopenfilename()))).pack(side=RIGHT, expand=YES, fill=BOTH)
row.pack(expand=YES, fill=BOTH)

row = Frame(root)
Label(row, text='Root directory:').pack(side=LEFT, fill=BOTH)
root_dir = Entry(row)
root_dir.insert(0, '/')
root_dir.pack(side=LEFT, expand=YES, fill=X)
Button(row, text='Browse directory', command=(lambda: fillEntry(root_dir, askdirectory()))).pack(side=RIGHT, expand=YES, fill=BOTH)
row.pack(expand=YES, fill=BOTH)

Button(root, text='List', command=listInstalled).pack(side=LEFT, expand=NO, fill=BOTH)
Button(root, text='Install', command=(lambda: installFile(file.get(), root_dir.get()))).pack(side=RIGHT, fill=BOTH)
Button(root, text='Uninstall', command=(lambda: uninstallFile(file.get()))).pack(side=RIGHT, fill=BOTH)

root.mainloop()
