gentoodeb: gentoodeb.c
  gcc -O3 -march=native gentoodeb.c -o gentoodeb
install: gentoodeb
  mv gentoodeb /usr/bin/gentoodeb
