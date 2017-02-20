import characters
import random
import time


def dice_roll(number):
    dice_value = random.randint(1, int(number))
    return dice_value

class Arena(object):
    """docstring for Arena
    in here I need:
    - character - done
    - character weapon - done
    - enemy/random
    - enemy attack - done
    - character takes damage - done
    - enemy takes damage - done
    - someone is victorious
    - use dice - done """
    def __init__(self, player, enemy):
        super(Arena, self).__init__()
        self.player = player
        self.enemy = enemy

    def update(self):
        """keep track of what I'm doing"""
        if self.player.health <= 0:
            self.player.health = 0
        if self.enemy.health <= 0:
            self.enemy.health = 0
        print "-" * 20
        print ("{0} is carrying a {1} with a damage of {3}, health is currently {2}").format(
            self.player.creature_type, self.player.weapon, self.player.health, self.player.weapon_damage)
        print "{0} is carrying a {1} with a damage of {3}, health is currently {2}".format(
            self.enemy.creature_type, self.enemy.weapon, self.enemy.health, self.enemy.weapon_damage)
        print "-" * 20

    def who_is_first(self):
        print "A D64 is rolled..."
        hero_start_dice = dice_roll(64)
        enemy_start_dice = dice_roll(64)
        print  "{0} rolls a {1}".format(self.player.creature_type, hero_start_dice)
        print  "{0} rolls a {1}".format(self.enemy.creature_type, enemy_start_dice)

        if hero_start_dice < enemy_start_dice:
            print "Hero goes first"
            first_attacker = self.player
            second_attacker = self.enemy
        else:
            print "Enemy goes first"
            first_attacker = self.enemy
            second_attacker = self.player

        print "First attack by {0}".format(first_attacker.creature_type)
        return first_attacker, second_attacker


    def fight(self):
        any_death = False
        """this is a turn, 
        random heal? """

        # who goes first funct split out as recommended by Marcin
        first_attacker, second_attacker = self.who_is_first()

        #this is the actual fight
        while any_death != True:
            damamge = (first_attacker.weapon_damage + dice_roll(6))
            second_attacker.health -= damamge
            print "{0} does {1} damage to {2}".format(first_attacker.creature_type, damamge, second_attacker.creature_type)
            damamge = (second_attacker.weapon_damage + dice_roll(6))
            first_attacker.health -= damamge
            print "{0} does {1} damage to {2}".format(second_attacker.creature_type, damamge, first_attacker.creature_type)
            battle1.update()
            time.sleep(1)
            any_death = is_dead(first_attacker.health, second_attacker.health)
            print "rtrtr" * 10
            #any_death = True

def attack(weapon, plus_damage):
    pass


def is_dead(hero, enemy):
    """checking if health is zero, how to include in each turn?"""
    if hero <= 0 or enemy <= 0:
        any_death = True
        return any_death
    else:   
        print "All still alive!"

def dead():
    print "you be dead"
    quit()




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
    battle1.fight()


    #is_dead(my_hero, my_hero.health)