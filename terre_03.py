#!/usr/bin/python

# ---- l'alphabet a partir de ----

import sys

# recuperer argument
for i in sys.argv[1:]:
    argument = i

# variable
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# boucler et afficher resultat
debut = 0
for arg in alphabet:
    debut = debut+1
    if argument == arg:
        argument = debut
        print(alphabet[argument-1:len(alphabet)])
