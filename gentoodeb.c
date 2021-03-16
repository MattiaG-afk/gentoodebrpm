#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argn, char *argv[]) {
    if((argv[1][0] == '-' && argv[1][1] == 'h')||(argv[1][0] == '-' && argv[1][1] == '-' && argv[1][2] == 'h' && argv[1][3] == 'e' && argv[1][4] == 'l' && argv[1][5] == 'p')) {
        printf("\033[;32mUsage\033[0m: gentoodeb [OPTIONS]\n");
        printf("\n\t-h, --help\t\tPrint this help message\n");
        printf("\t-i, --install [FILE]\tInstall the [FILE] packet\n\n");
        printf("\033[;33mExample\033[0m:\n");
        printf("\tgentoodeb -i google-chrome-stable*.deb\tInstall the google-chrome-stable*.deb packet.\n");
    }
    if((argv[1][0] == '-' && argv[1][1] == 'i')||(argv[1][0] == '-' && argv[1][1] == '-' && argv[1][2] == 'i' && argv[1][3] == 'n' && argv[1][4] == 's' && argv[1][5] == 't' && argv[1][6] == 'a' && argv[1][7] == 'l' && argv[1][8] == 'l')) {
        printf("Installing the \033[1;31m%s\033[0m file.\n", argv[2]);
        char command[100];
        strcpy(command, "sudo ar x ");
        strcat(command, argv[2]);
        system(command);
        system("sudo rm debian-binary control.tar.xz");
        system("sudo mv data.tar.xz /");
        system("sudo tar xpf /data.tar.xz");
    }
    return 0;
}
