import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, df, atk, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk -10
        self.atkh = atk +10
        self.df = df
        self.magic = magic
        self.actions = ["Attack, Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        ngl = self.magic[i]["dmg"] - 5
        ngh = self.magic[i]["dmg"] + 5
        return random.randrange(ngl, ngh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <0:
            self.hp =0
            return self.hp

