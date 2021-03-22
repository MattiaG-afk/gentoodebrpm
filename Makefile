install: gentoodeb.c
	gcc -O3 -march=native gentoodeb.c -o gentoodeb
	mv gentoodeb /usr/bin/gentoodeb
