#!/usr/bin/python
# -*- coding: Latin-1 -*
# ---- taille d'une chaîne ----

import sys 

for i in sys.argv[1:]:
    argument = i
    try:
        print(len(argument))
    except:
        print('erreur.')


""""
for i in sys.argv[1:]:
    string = i

print(len(string))

"""
# gérer carractère spéciaux en argument 