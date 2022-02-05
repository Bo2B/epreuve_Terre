#!/usr/bin/python
# ---- puissance d'un nombre ----

import sys

v1 = sys.argv[1]
v2 = sys.argv[2]

argument = int (v1)
exposant = int (v2)

print (pow(argument,exposant))


# faire en sorte de ne rien afficher si pas d'argument
# gérer les entiers négatifs   
