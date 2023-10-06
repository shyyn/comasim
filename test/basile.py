from random import *
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
        att1 = randint(1, 15)
        print("DMG: ", att1)
        hp2 = hp2 - att1
        print("HP", J2, ":", hp2)
    elif hp1 <= 0:
         dead = 1
         print(J1, "is dead")
         print(J2, "won")
         break
    elif hp2 <= 0:
       dead = 2
       print(J2, "is dead")
       print(J1, "won")
       break
    if turn == 2:
            print(J2,"turn")
            att2 = randint(1, 15)
            print("DMG: ", att2)
            hp1 = hp1 - att2
            print("HP", J1, ":", hp1)
    elif hp2 <= 0:
        dead = 1
        print(J2, "is dead")
        print(J1, "won")
        break
    elif hp1 <= 0:
         dead = 1
         print(J1, "is dead")
         print(J2, "won")
         break