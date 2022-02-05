#!usr/bin/python
# -*- coding: Latin-1 -*-

# ---- 12 to 24 ----

import sys

for i in sys.argv[1:]:
    h = i
    if h[5:] == 'PM':
        h = str(int(h[:-5])+12) + h[2:-2]
    else:
        h = h[:-2]

print(h)
