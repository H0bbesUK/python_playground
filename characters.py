import random
weapon_dict = {'Mace': 3, 'Sword': 5, 'Spear': 2, 'Axe': 3, 'Stick Of Truth': 6, 'Pike': 4, 'Knife': 1, }
character_dict = {'Wizard': 180, 'Knight': 450, 'Paladin': 575, 'Thief': 350, }

class Character(object):
    """docstring for Goblin"""
    def __init__(self, health, creature_type, weapon):
        super(Character, self).__init__()
        self.health = int(health)
        self.weapon = weapon
        self.creature_type = "Character"

    def lose_health(self):
        self.health -= 1
        print "{0}'s health is now {1}, the weapon being held is a{2}".format(self.creature_type, self.health, self.weapon)

    def critical_damage(self):
        damage = random.randint(2,100)
        self.health -= damage
        print "{0} takes {2} damage, health is now {1}".format(self.creature_type, self.health, damage)

    def heal(self):
        self.health += 1
        print "{0}'s health is now {1}".format(self.creature_type, self.health)

    def show_health(self):
       print "{0}'s health is now {1}".format(self.creature_type, self.health)


class Enemy(Character):
    def __init__(self, health, creature_type, weapon):
        super(Character, self).__init__()
        self.health = int(health)
        self.weapon = weapon
        self.weapon_damage = weapon_dict[weapon]
        self.creature_type = creature_type

class Hero(Character):
    def __init__(self, health, creature_type, weapon):
        super(Character, self).__init__()
        self.health = int(health)
        self.weapon = weapon
        self.weapon_damage = weapon_dict[weapon]
        self.creature_type = creature_type 


if __name__ == "__main__":

    goblin_one = Enemy(50, "Goblin", "Knife")
    goblin_two = Enemy(50, "Goblin", "Knife")
    goblin_boss = Enemy(200, "Goblin Boss", "Sword")
    my_hero = Hero(500, "Mike the Knight", "Mace")


    print goblin_one.health 
    goblin_one.lose_health()

    my_hero.heal()

    goblin_boss.heal()

    my_hero.show_health()
        