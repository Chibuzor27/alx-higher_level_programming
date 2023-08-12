#!/usr/bin/python3
for i in range(65, 65+26):
    print('{:c}{:s}'.format(i, "\n" if i == 65+26-1 else ""), end='')
