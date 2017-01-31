import random

class Character(object):
    """docstring for Goblin"""
    def __init__(self, health, creature_type):
        super(Character, self).__init__()
        self.health = int(health)
        self.creature_type = "Character"

    def lose_health(self):
        self.health -= 1
        print "{0}'s health is now {1}".format(self.creature_type, self.health)

    def critical_damage(self):
        damage = random.randint(2,100)
        self.health -= damage
        print "{0} takes {2} damage, health is now {1}".format(self.creature_type, self.health, damage  )

    def heal(self):
        self.health += 1
        print "{0}'s health is now {1}".format(self.creature_type, self.health)

    def show_health(self):
        print "{0}'s health is now {1}".format(self.creature_type, self.health)
        print "-" * 20

class Goblin(Character):
    def __init__(self, health, creature_type):
        super(Character, self).__init__()
        self.health = int(health)
        self.creature_type = creature_type
        self.attack = 5


class Hero(Character):
    def __init__(self, health, creature_type):
        super(Character, self).__init__()
        self.health = 100
        self.creature_type = creature_type 


if __name__ == "__main__":

    goblin_one = Goblin(10, "Goblin")
    goblin_two = Goblin(10, "Goblin")
    goblin_boss = Goblin(50, "Goblin Boss")
    my_hero = Hero(500, "Mike the Knight")


    print goblin_one.health 
    goblin_one.lose_health()

    my_hero.heal()

    goblin_boss.heal()

    my_hero.show_health()
        