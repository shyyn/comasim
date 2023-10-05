from random import *

att = 5
deg = att
crit = randint(14,15)
if crit == 14:
    deg = att * 2
    print(deg, "Coup critique dans ta mere")
else:
    print(att)    