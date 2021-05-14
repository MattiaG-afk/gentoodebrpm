#!/usr/bin/python3
import os, sys, subprocess

options = {}
log_dir = '/var/log/debrpm'
tmp_dir = '/var/tmp/debrpm'

i = 0
for option in sys.argv:
    if option.startswith('-'):
        if not('help' in option or 'h' in option) and not('list' in option or 'l' in option):
            options[option] = sys.argv[i+1]
        else:
            options[option] = ''
    i += 1

if '-i' in options or '--install' in options:
    try:
        file = options['-i']
    except:
        file = options['--install']
    if '-/' in options or '--root' in options:
        try:
            root = options['-/']
        except:
            root = options['--root']
    else:
        root = '/'
    log_file = os.path.join(log_dir, file + '.log')
    open(log_file, 'w').write('Root directory:' + root)
    if file.find('.deb') != -1:
        print("Installing the file: ", file)
        subprocess.run("sudo cp %s %s" % (file, tmp_dir), shell=True)
        subprocess.run("sudo ar x %s" % os.path.join(tmp_dir, file), shell=True)
        subprocess.run("rm -f %s %s" % (os.path.join(tmp_dir, "debian-binary"), os.path.join(tmp_dir, "control.tar.xz")), shell=True)
        subprocess.run("sudo tar xpvf %s >> %s" % (os.path.join(tmp_dir, "data.tar.xz"), os.path.join(log_dir, log_file)), shell=True)
        subprocess.run("rm -f %s" % os.path.join(tmp_dir, "data.tar.xz"), shell=True)
        subprocess.run("mv %s %s" % (os.path.join(tmp_dir, "*"), root), shell=True)
    elif file.find('.rpm') != -1:
        print("Installing the file: ", file)
        subprocess.run("rpm2tarxz " + file, shell=True)
        subprocess.run("rm -f %s" % file, shell=True)
        subprocess.run("mv " + file.replace(".rpm", ".tar.xz") + " " + root, shell=True)
        os.chdir(root)
        subprocess.run("sudo tar xpvf " + file.replace(".rpm", ".tar.xz") + " >> " + log_file, shell=True)
        subprocess.run("rm " + file.replace(".rpm", ".tar.xz"), shell=True)
    else:
        print('\u001b[31;1mUnknown file. Currently supported files are: .deb and .rpm\u001b[00;0m')
elif '-u' in options or '--uninstall' in options:
    try:
        packet = options['-u']
    except:
        packet = options['--uninstall']
    packet = os.path.join(log_dir, packet)
    if not packet.endswith('.log'):
        packet += '.log'
    try:
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
    except:
        print('Package not installed')
elif '-l' in options or '--list' in options:
    index = 0
    for file in os.listdir(log_dir):
        if file.endswith('.log'):
            index += 1
            if '.deb' in file:
                print('\u001b[33;1mName\u001b[00;0m: %s, \u001b[33;1mtype\u001b[00;0m: deb, \u001b[33;1mlog file\u001b[00;0m: %s' % (file.replace('.deb.log', ''), os.path.join(log_dir, file)))
            elif '.rpm' in file:
                print('\u001b[33;1mName\u001b[00;0m: %s, \u001b[33;1mtype\u001b[00;0m: rpm, \u001b[33;1mlog file\u001b[00;0m: %s' % (file.replace('.rpm.log', ''), os.path.join(log_dir, file)))
    print('\u001b[36;1mNumber of installed packages\u001b[00;0m: %s' % index)

else:
    print("\033[1;31mUsage\033[0m: debrpm [OPTIONS] [FILE]\n")
    print("OPTIONS:")
    print("-h, --help\t\tShow this help message")
    print("-i, --install\t\tInstall a packet from a file .deb or .rpm")
    print("-u, --uninstall\t\tUninstall a packet from a log file of a .deb or .rpm installed packet")
    print("-l, --list\t\tList all installed packages\n")
    print('\033[1;00mINSTALL OPTIONS\033[0m:')
    print('-/, --root\t\tChoose the directory where to extract the package')
