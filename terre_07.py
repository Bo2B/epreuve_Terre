#!/usr/bin/python
# -*- coding: Latin-1 -*

# ---- taille d'une chaîne ----

import sys 

# n'afficher le nombre de caractère que d'une seul chaîne
# tester argument
if sys.argv[1:] == []:
    print("erreur.")

try:
    for x in sys.argv[1:]:
        y = [int(i) for i in x]
        print("erreur.")
except ValueError:
    if sys.argv[2:] != sys.argv[-1:]:
        a = sys.argv[1:]
        str_a = "".join(a)
        print(len(str_a)) 
    else:
        print("erreur.")
