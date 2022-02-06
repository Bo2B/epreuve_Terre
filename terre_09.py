#!/usr/bin/python
# -*- coding: Latin-1 -*-

# ---- racine carrée d'un nombre ----

import sys

# Tester, calculer, afficher
try:
    for i in sys.argv[1:]:
        x = [int(v) for v in i]
        r = x[0]**(0.5)
        print(int(r))
except ValueError:
    print("Je ne calcul que les entiers positifs.")
