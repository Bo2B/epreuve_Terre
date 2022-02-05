#!usr/bin/python
# -*- coding: Latin-1 -*-

# ---- trié ou pas ----

import sys

for x in sys.argv[1:]:
    x = sys.argv[1:]

    y = [int(i) for i in x]
    a = y[0]
    z = y[::]

if min(y) == a:
    if max(y) != a:
        print("Triée !")
elif min(y) != a:
    print("Pas triée !")

# Gérer les strings en argument 