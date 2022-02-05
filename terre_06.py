#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# ---- inverser une chaîne ----

import sys

for i in sys.argv[1:]:
   argument = i
   try:
      sys.argv[1:] == str(sys.argv[1:])
      length_arg = len(argument)
      sliced_arg = argument[length_arg::-1] 
      print (sliced_arg)
   except:
      print('erreur.')

# gérer carractère spéciaux en argument 
 