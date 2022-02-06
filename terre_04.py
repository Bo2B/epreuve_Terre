#!/usr/bin/python
# -*-coding: Latin-1 -*

# ---- pair ou impair ----

import sys

for i in sys.argv[1:]:
    nombre = i

# tester argument et afficher resultat
try:
    arg = int (nombre) 
    if (arg%2) == 0:
        print("pair")
    elif (arg%2) == 1:
        print("impair")   
except:
    print("Tu ne me la mettras pas à l'envers.")