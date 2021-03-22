CC=gcc
CFLAGS=-I.
SRC=$(wildcard *.c)
OBJ=$(gentoodeb.c)

PREFIX=/usr/bin

%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

ebuildexample: $(OBJ)
	$(CC) $(OBJ) -o gentoodeb

.PHONY: clean
clean:
	rm -f $(OBJ) gentoodeb

.PHONY: install
install: gentoodeb
	mkdir -p $(DESTDIR)$(PREFIX)
	cp $< $(DESTDIR)$(PREFIX)/gentoodeb

.PHONY: uninstall
uninstall:
	rm -f $(DESTDIR)$(PREFIX)/gentoodeb
