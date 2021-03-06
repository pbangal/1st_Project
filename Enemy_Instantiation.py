from classes.game import bcolors, Person

magic = [{"name": "Fire" , "cost": "10", "dmg": "60"},
         {"name": "Thunder", "cost": "10", "dmg": "80"},
         {"name": "Blizzard", "cost": "10", "dmg": "60"}]

player = Person(465, 40, 60, 70, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "An enemy attacks" + bcolors.ENDC)

while running:
    print("====================")
    player.choose_action()
    choice = input("Choose action")
    index = int(choice) - 1
    print("You choose", player.get_spell_name(int(index)))

    if index == 0:
        dmg = player.generate_damage()
            enemy.take_damage()
            print("You attacked for" , dmg, "points of damage. Enemy HP", enemy.get_hp())

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP", player.get_hp())
