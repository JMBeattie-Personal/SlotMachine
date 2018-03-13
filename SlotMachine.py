#
# Slot Machine
#

slotsPossible = ["bar","bar","bar","cherry","crown"]

from random import *

slot1=choice(slotsPossible)
slot2=choice(slotsPossible)
slot3=choice(slotsPossible)

print(slot1+":"+slot2+":"+slot3)

if (slot1==slot2==slot3=="cherry"):
    print("You win $100")
if (slot1==slot2==slot3=="crown"):
    print("You win $50")
if (slot1==slot2==slot3=="bar"):
    print("You win $5")
