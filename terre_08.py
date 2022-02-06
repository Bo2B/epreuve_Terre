#!/usr/bin/python
# -*- coding: Latin-1 -*-

# ---- puissance d'un nombre ----

import sys

# récupérer argument dans variable
for v in sys.argv[1:]:
    v1 = sys.argv[1]
    v2 = sys.argv[2]
    arg = int (v1)
    xp = int (v2)

# tester et calculer
try:
    if xp < 0:
        print("L'exposant ne peut être négatif.")
    else:
        print(pow(arg,xp))
except:
    print("Aucune valeur définie.")
