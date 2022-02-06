#!usr/bin/python
# -*- coding: Latin-1 -*-

# ---- trié ou pas ----

import sys

# tester, afficher
try:
    for x in sys.argv[1:]:    # récupérer argument dans variable
        x = sys.argv[1:] 
        y = [int(i) for i in x]
        a = y[0]
        z = y[::]

    if min(y) == a:
        if max(y) != a:
            print("Triée !")
    elif min(y) != a:
        print("Pas triée !")

except ValueError:
    print("erreur.")
