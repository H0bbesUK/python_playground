weapon_dict = {'Mace': 3, 'Sword': 5, 'Spear': 2, 'Axe': 3, 'Stick of truth': 4 }
character_dict = {'Wizard': 100, 'Knight': 300, 'Paladin': 500, 'Thief': 300}
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
        self.player.show_health()
        print "{0} is carrying a {1}".format(self.player.creature_type, self.weapon)
        self.enemy.show_health()


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


def player_start():
    player_choose = False
    print "Welcome to the awsome DR battle arena"
    print "Please choose a character from the following"
    x = 0
    for i in character_dict:
        x += 1
        print "{0}. {1}".format(x, i)
    while player_choose !=True:
        player_class = raw_input("> ").title() 
        if player_class in character_dict:
            print "\nYou chose {0}\n".format(player_class)
            player_choose = True
        else: 
            print "Incorrect choice, try again\n"
    print "Please choose a weapon for your {0}:".format(player_class)
    x = 0
    for i in weapon_dict:
        x += 1
        print "{0}. {1}".format(x, i)
    player_weapon = raw_input("3==D ")


if __name__ == "__main__":

    player_start()

    my_hero = characters.Hero(500, "Mike the Knight")
    #my_hero.heal()
    #my_hero.show_health()
    #my_hero.critical_damage()
    #my_hero.critical_damage()
    goblin_boss = characters.Goblin(50, "Goblin Boss")

    battle1 = Arena(my_hero, goblin_boss, "mace")
    battle1.update()


    #is_dead(my_hero, my_hero.health)