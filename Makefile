debrpm: debrpm.py Docs/debrpm.1
	mkdir -p /var/log/debrpm /var/tmp/debrpm
	chmod +x debrpm.py
	cp debrpm.py /usr/bin/debrpm
	install -g 0 -o 0 -m 0644 Docs/debrpm.1 /usr/share/man/man1/
	gzip /usr/share/man/man1/debrpm.1
uninstall:
	rm -rf /var/log/debrpm /var/tmp/debrpm /usr/bin/debrpm
