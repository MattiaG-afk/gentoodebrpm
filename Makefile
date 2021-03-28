 gentoodebrpm: gentoodebrpm.c
     gcc -O3 -march=native gentoodebrpm.c -o /bin/gentoodebrpm
     mkdir $HOME/.gentoodebrpm
 
 install: gentoodebrpm
     sudo mv gentoodebrpm /bin/gentoodebrpm
