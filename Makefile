gentoodeb: gentoodeb.c
  gcc -O3 -march=native gentoodeb.c -o gentoodeb
install: gentoodeb
  sudo mv gentoodeb /bin/gentoodeb
