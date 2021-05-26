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
        subprocess.run('sudo debrpm -i %s -/ %s' % (file, root), shell=True)
        showinfo('Debrpm GUI', 'Package installed successfully')
    except:
        showerror('Debrpm GUI', 'An error occurred:\n%s' % sys.exc_info)

def uninstallFile(packet):
    try:
        print(packet)
        subprocess.run('sudo debrpm -u %s' % file, shell=True)
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
Button(root, text='Uninstall', command=(lambda: uninstallFile(file.get().split('/')[-1]))).pack(side=RIGHT, fill=BOTH)

root.mainloop()
