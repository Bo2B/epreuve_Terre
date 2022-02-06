#!usr/bin/python
# -*- coding: Latin-1 -*-

# ---- trouver la Suisse ----

import sys

# récupérer argumet dans variable
for x in sys.argv[1:]:
    x = sys.argv[1:] 
    y = [int(i) for i in x]
    a = y[0]
    b = y[1]
    c = y[2]

# tester, afficher
if a == b == c:
    print("erreur.")
else:
    if min(y) < a < max(y):
        print(a)
    elif min(y) < b < max(y):
        print(b)
    else:
        print(c)
