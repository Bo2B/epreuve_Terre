#!usr/bin/python
# -*- coding: Latin-1 -*-

# ---- 24 to 12 ----

import sys
from time import *

for i in sys.argv[1:]:
    h = i
    if int(h[:-3]) > 12:
        h = str(int(h[:-3])-12) + (h[-3:]) + "PM"
    else:
        h = i + "AM"
    
print (h)


