from random import *

dead = 0
hp1 = 100
hp2 = 100

while dead == 0:
    turn = randint(1, 2)
    input("Press enter to continue")
    if turn == 1:
        print("P1 starts")
        att1 = randint(1, 15)
        print("DMG: ", att1)
        hp2 = hp2 - att1
        print("HP P2: ", hp2)
        if hp2 <= 0:
            dead = 2
            print("P2 is dead")
        else:
            print("P2 starts")
            att2 = randint(1, 15)
            print("DMG: ", att2)
            hp1 = hp1 - att2
            print("HP P1: ", hp1)
            if hp1 <= 0:
                dead = 1
                print("P1 is dead")
                
if dead == 1:
    print("P2 Won")
elif dead == 2:
    print("P1 Won")
