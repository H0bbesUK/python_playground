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
    def __init__(self, player, enemy):
        super(Arena, self).__init__()
        self.player = player
        self.enemy = enemy

    def update(self):
        """keep track of what I'm doing"""
        print "-" * 20
        print ("{0} is carrying a {1} with a damage of {3}, health is currently {2}").format(
            self.player.creature_type, self.player.weapon, self.player.health, self.player.weapon_damage)
        print "{0} is carrying a {1} with a damage of {3}, health is currently {2}".format(
            self.enemy.creature_type, self.enemy.weapon, self.enemy.health, self.enemy.weapon_damage)
        print "-" * 20


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
    """Gather facts to create player"""
    player_choose = False
    print "Welcome to the awsome DR battle arena"
    print "Please choose a character from the following"
    x = 0
    for i in characters.character_dict:
        x += 1
        print "{0}. {1}".format(x, i)
    while player_choose != True:
        player_class = raw_input("> ").title() 
        if player_class in characters.character_dict:
            print "\nYou chose {0}\n".format(player_class)
            player_choose = True
        else: 
            print "Incorrect choice, try again\n"
    """now choose the weapon"""
    weapon_choose = False
    print "Please choose a weapon for your {0}:".format(player_class)
    x = 0
    for i in characters.weapon_dict:
        x += 1
        print "{0}. {1}".format(x, i)
    while weapon_choose != True:
        player_weapon = raw_input("3==D ").title()
        if player_weapon in characters.weapon_dict:
            print "Your {0} is now armed with a {1}".format(player_class, player_weapon)
            weapon_choose = True
        else:
            print "Incorrect choice, try again\n"
    return player_class, player_weapon


if __name__ == "__main__":


    player_class, player_weapon = player_start()
    print player_class, player_weapon
    """alternative ways to extract the variables"""
    #foo = player_start()
    #print foo[0], foo[1]

    my_hero = characters.Hero(characters.character_dict[player_class], player_class, player_weapon)

    goblin_boss = characters.Enemy(100, "Goblin Boss", "Spear")

    battle1 = Arena(my_hero, goblin_boss)
    battle1.update()


    #is_dead(my_hero, my_hero.health)