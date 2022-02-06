#!/usr/bin/python
# -*- coding: Latin-1 -*-

# ---- nombre premier ----

import sys

# récupérer argument dans variable
for i in sys.argv[1:]:
    num = i
    num = int(num)

# tester et afficher   
if num < 2:
    print("Saisir un nombre supérieur ou égal à 2.")
elif num > 2 and num % 2 == 0:
    print("Non, " + str(num) + " n'est pas un nombre premier.")
else:
    print("Oui, " + str(num) + " est un nombre premier.")


