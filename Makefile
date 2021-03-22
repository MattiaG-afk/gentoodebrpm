CC=gcc
CFLAGS=-I.
SRC=$(wildcard gentoodeb.c)
OBJ=$(SRC:.c=.o)

PREFIX=/bin

%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

ebuildexample: $(OBJ)
	$(CC) -o gentoodeb $(OBJ)

.PHONY: clean
clean:
	rm -f $(OBJ) gentoodeb

.PHONY: install
install: ebuildexample
	mkdir -p $(DESTDIR)$(PREFIX)
	cp $< $(DESTDIR)$(PREFIX)/gentoodeb

.PHONY: uninstall
uninstall:
	rm -f $(DESTDIR)$(PREFIX)/gentoodeb
