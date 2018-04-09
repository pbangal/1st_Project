import random

playerhp = 260
atklw = 60
atkhigh = 80

while playerhp > 0:
    dmg = random.randrange(atklw, atkhigh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)

    if playerhp == 30:
        print("You have low health. Shifted to hospital.")
        break
