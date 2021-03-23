gentoodeb: gentoodeb.c
  gcc -O3 -march=native gentoodeb.c -o gentoodeb
endef

install: gentoodeb
  sudo mv gentoodeb /bin/gentoodeb
endef
