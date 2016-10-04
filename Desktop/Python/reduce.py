#!/usr/bin/env python
#on import ces modules
import re, string

f = open('Map2.txt','a')
f2 = open('Map.txt','r')
# increase counters
tabl=[]
for line in f2:
    f.write(line)

f2.close()
f.close()

f3 = open('Map2.txt','r')
for line in f3:
    tabl += line.split()
f3.close()

tabl.sort()
mot =''
nombre = int('0')
for valeur in tabl:
    tabl2 = valeur.split(',')
    if mot != tabl2[0]:
        print (mot + ',' + str(nombre))
        mot = tabl2[0]
        nombre = int(tabl2[1])
    elif mot== tabl2[0]:
        nombre += int(tabl2[1])

