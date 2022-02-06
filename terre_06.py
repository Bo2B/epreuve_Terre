#!/usr/bin/python3
# -*- coding: Latin-1 -*-
 
# ---- inverser une chaîne ----

import sys

# découper la liste et afficher
for i in sys.argv[1:]:
   argument = i
   length_arg = len(argument)
   sliced_arg = argument[length_arg::-1] 

print (sliced_arg)

