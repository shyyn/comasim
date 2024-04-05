from random import *

def crit(x):
    if randint(1, 15) == 1:
        print("Critical Hit! Double Damage!")
        x = x * 2
        if x <= 15:
            x = 15
    return x


def dodge(y):
    if randint(1,22) == 1:
        y = 0
    return y
