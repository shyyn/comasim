from random import *

def crit(x):
    if randint(1, 10) == 1:
        print("Critical Hit! Double Damage!")
        return x * 2
    return x
    