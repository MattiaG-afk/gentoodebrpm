debrpm: debrpm.py
	mkdir -p /var/log/debrpm
	mkdir -p /var/tmp/debrpm
	chmod +x debrpm.py
	mv debrpm.py /usr/bin/debrpm
	debrpm -u
uninstall:
	rm -rf /var/log/debrpm /usr/bin/debrpm
