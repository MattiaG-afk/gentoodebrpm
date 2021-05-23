debrpm: debrpm.py
	mkdir -p /var/log/debrpm /var/tmp/debrpm
	chmod +x debrpm.py
	cp debrpm.py /usr/bin/debrpm
	install -g 0 -o 0 -m 0644 Docs/debrpm.1 /usr/local/man/man8/
	gzip /usr/local/man/man8/debrpm.1
uninstall:
	rm -rf /var/log/debrpm /var/tmp/debrpm /usr/bin/debrpm
