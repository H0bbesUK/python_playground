weapon_dict = {'Mace': 3, 'Sword': 5, 'Spear': 2, 'Axe': 3, }
character_dict = {}
import characters
import random


class Arena(object):
    """docstring for Arena
    in here I need:
    - character
    - character weapon
    - enemy/random
    - enemy attack
    - character takes damage
    - enemy takes damage
    - someone is victorious
    - use dice """
    def __init__(self, player, enemy, weapon):
        super(Arena, self).__init__()
        self.player = player
        self.enemy = enemy
        self.weapon = weapon

    def update(self):
        """keep track of what I'm doing"""
        print characters.Character.show_health(self.player)
        print "{0} is carrying a {1}".format(self.player.creature_type, self.weapon)
        print characters.Character.show_health(self.enemy)



def attack(weapon, plus_damage):
    pass


def is_dead(character, remaining_health):
    """checking if health is zero, how to include in each turn?"""
    if remaining_health <= 0:
        dead()
    else:   
        print "Still alive!"

def each_turn():
    """this is a turn, use weapon, take health or heal?"""
    pass


def dead():
    print "you be dead"
    quit()


def dice_roll(number):
    dice_value = random.randint(1, int(number))
    return dice_value





if __name__ == "__main__":

    my_hero = characters.Hero(500, "Mike the Knight")
    #my_hero.heal()
    #my_hero.show_health()
    #my_hero.critical_damage()
    #my_hero.critical_damage()
    goblin_boss = characters.Goblin(50, "Goblin Boss")

    battle1 = Arena(my_hero, goblin_boss, "mace")
    battle1.update()


    #is_dead(my_hero, my_hero.health)