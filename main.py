from random import randint

from critical import *

def battle():
    dead = 0
    hp1 = 100
    hp2 = 100
    J1 = input("P1 name: ")
    J2 = input("P2 name: ")

    while dead == 0:
        turn = randint(1, 2)
        input("Press enter to continue")

        if turn == 1:
            print(J1, "turn")
            att1 = crit(randint(1, 15))
            print("DMG: ", att1)
            hp2 = hp2 - att1
            print("HP", J2, ":", hp2)

            if hp2 <= 0:
                dead = 1
                print(J2, "is dead")
                print(J1, "won")
                break

        elif turn == 2:
            print(J2, "turn")
            att2 = crit(randint(1, 15))
            print("DMG: ", att2)
            hp1 = hp1 - att2
            print("HP", J1, ":", hp1)

            if hp1 <= 0:
                dead = 2
                print(J1, "is dead")
                print(J2, "won")
                break

battle()