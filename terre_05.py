#!/usr/bin/python
# -*-coding: Latin-1 -*

# ---- divisions ----

# recuperer arguments 
import sys

for i in sys.argv[1:]: 
    dividende = int(sys.argv[1])
    diviseur = int(sys.argv[2])

# tester arguments et afficher resultat
try:
    if dividende >= diviseur:
        quotien = dividende // diviseur
        reste = dividende % diviseur
        print("résultat: " + str(quotien))
        print("reste: " + str(reste))
    else:
        print("erreur.")
except:
    print ("erreur.")