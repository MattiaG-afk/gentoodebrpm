debrpm: debrpm.c
	gcc -O3 -march=native debrpm.c -o /usr/bin/debrpm
	mkdir /var/log/debrpm
