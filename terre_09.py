#!/usr/bin/python
# -*- coding: Latin-1 -*-
# ---- racine carrée d'un nombre ----

import math
import sys

for i in sys.argv[1:]:
    i = math.sqrt(int(i))

print (int(i))

#gérer les arguments négatifs
# gérer argument vide