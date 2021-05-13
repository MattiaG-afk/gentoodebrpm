debrpm: debrpm.py
	mkdir -p /var/log/debrpm /var/tmp/debrpm
	chmod +x debrpm.py
	cp debrpm.py /usr/bin/debrpm
uninstall:
	rm -rf /var/log/debrpm /var/db/debrpm /usr/bin/debrpm
