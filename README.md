# DEBRPM
<p align="center"><a href="https://github.com/MattiaG-afk/debrpm"><img src="https://github.com/MattiaG-afk/debrpm/blob/test/Images/debrpm_small.png" alt='DEBRPM'></a></p>

An easy to use installer for .deb and .rpm packet on Gentoo, Slackware and other distros.
## Installation
You can install this progam by running:
```shell
git clone https://github.com/MattiaG-afk/debrpm.git
cd debrpm
sudo make
```
## Uninstall packages
You have to insert the name of the log file. If you don't write the absolute path (without the '/var/log/debrpm/') or without the .log extension will be added automatically.
## Wait, wait, wait...
* Use debrpm only if the package you need is not present in the repositories of the package manager of your GNU/Linux operating system;
* Installing a package with debrpm when it has already been installed with the package manager of your GNU/Linux operating system may harm your system
