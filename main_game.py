import characters
import random
import time
import os

super_short = 0.1
short = 1
med = 2
longer = 3
short = 0.1 # test timings
med = 0.2 # test timings
longer = 0.3 # test timings

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

    def random_encounter(self):
        is_random = dice_roll(64)
        is_random_funny = dice_roll(6)
        #is_random_funny = 1 # testing
        #is_random = 51 # testing
        if is_random > 50:
            time.sleep(longer)
            print "***** Random Encounter!! ******"
            print "***** Hit enter to discover your fate ******"
            blah = raw_input("> ")
            time.sleep(longer)
            print "A D{0} seals your fate...".format(6)
            time.sleep(longer)
            if is_random_funny == 6:
                print "You hear a strange wailing noise above"
                time.sleep(med)
                print "You look up, a whale flattens you causing...."
                time.sleep(med)
                print "Dice roll...."
                time.sleep(med)
                whale_damage = dice_roll(32)
                print "A D{0} is thrown".format(32)
                time.sleep(med)
                print "{0}hp damage is inflicted on you".format(whale_damage)
                self.player.health -= whale_damage
            elif is_random_funny == 5:
                print "Randomly, a unicorn appears"
                time.sleep(med)
                print "unfortunately for you he's having a bad day and charges you with his horn"
                time.sleep(med)
                print "Dice roll...."
                time.sleep(med)
                unicorn_damage = dice_roll(20)
                print "A D{0} is thrown".format(20)
                time.sleep(med)
                print "{0}hp damage".format(unicorn_damage)
                self.player.health -= unicorn_damage
            elif is_random_funny == 4:
                print "Out of the blue..."
                time.sleep(med)
                print "the boyband Blue appear and sing an impromptu rendition of 'One Love'"
                time.sleep(med)
                print "Dice roll...."
                time.sleep(med)
                blue_damage = dice_roll(6)
                print "A D{0} is thrown".format(6)
                time.sleep(med)
                print "The enemy fortunately hacks them to bits silencing the awful melody, although Antony Costa caused {0}hp damage to {1}".format(
                    blue_damage, self.enemy.creature_type)
                self.enemy.health -= blue_damage
            elif is_random_funny == 3:
                print "The {0} call for a medic, and duly a doctor arrives for them...".format(self.enemy.creature_type)
                time.sleep(med)
                print "lukily for you, its famous serial killer Harold Shipman and he works his magic on your enemy"
                time.sleep(med)
                print "Dice roll...."
                time.sleep(med)
                DR_damage = dice_roll(30)
                print "A D{0} is thrown".format(30)
                time.sleep(med)
                print "Dr Shipman performs {0}hp of damage with his loveable bedside manner".format(DR_damage)
                self.enemy.health -= DR_damage
            elif is_random_funny == 2:
                burger_heal = dice_roll(6)
                print "Wow, the Newark burger van pulls up, you order a famous 'dirty burger'"
                time.sleep(med)
                print "Thankfully this one doesn't give you E. coli but heals you by {}hp".format(burger_heal)
            elif is_random_funny == 1:
                print "Something something healing..."
                print "You both get some heals."
                time.sleep(med)
                friendly_heal = dice_roll(14)
                enemy_heal = dice_roll(14)
                print "You gain {0}hp and the {1} restores {2}hp.".format(
                    friendly_heal, self.enemy.creature_type, enemy_heal)
                self.player.health += friendly_heal
                self.enemy.health += enemy_heal
            battle1.update("Random")
        #so.. random stuff
        # get user to pick a dice to roll?
        # a unicorn appears, heals
        # a enemy something happens does extra damage
        # upgrade to weapon?
        # extra armour?
        # reduce armour?
        # upgrade enemy weapon
        # inconsiquential events
        pass

    def update(self, count_round):
        """keep track of what I'm doing"""
        if self.player.health <= 0:
            self.player.health = 0
        if self.enemy.health <= 0:
            self.enemy.health = 0
        print "\n"
        time.sleep(short)
        if count_round == "Random":
            print "------------ Status after random encounter --------------".format(count_round)
        else:
            print "------------------ Status of Round {} -------------------".format(count_round)
        print ("{0} is carrying a {1} with a damage of {3}, health is currently {2}").format(
            self.player.creature_type, self.player.weapon, self.player.health, self.player.weapon_damage)
        print "{0} is carrying a {1} with a damage of {3}, health is currently {2}".format(
            self.enemy.creature_type, self.enemy.weapon, self.enemy.health, self.enemy.weapon_damage)
        print "-" * 55
        time.sleep(short)


    def who_is_first(self):
        print "\nA D64 is rolled..."
        time.sleep(short)
        hero_start_dice = dice_roll(64)
        enemy_start_dice = dice_roll(64)
        print  "{0} rolls a {1}".format(self.player.creature_type, hero_start_dice)
        time.sleep(short)
        print  "{0} rolls a {1}".format(self.enemy.creature_type, enemy_start_dice)
        time.sleep(short)
        print "\n"

        if hero_start_dice < enemy_start_dice:
            print "Hero goes first"
            first_attacker = self.player
            second_attacker = self.enemy
        else:
            print "Enemy goes first"
            first_attacker = self.enemy
            second_attacker = self.player

        print "First attack by {0}".format(first_attacker.creature_type)
        time.sleep(med)
        return first_attacker, second_attacker


    def fight(self):
        any_death = False
        """this is a turn, 
        random heal? """
        # who goes first funct split out as recommended by Marcin
        first_attacker, second_attacker = self.who_is_first()
        #this is the actual fight
        count_round = 1
        print "\n-------------- Round {0} ----------------".format(count_round)
        while any_death != True:
            if count_round > 1:
                battle1.random_encounter()
            time.sleep(short)
            pause = raw_input("Hit enter to roll the dice.")
            print "------- many dice being thrown --------\n"
            time.sleep(med)
            damamge = (first_attacker.weapon_damage + dice_roll(6))
            second_attacker.health -= damamge
            print "{0} does {1}hp of damage to {2}".format(first_attacker.creature_type, damamge, second_attacker.creature_type)
            time.sleep(short)
            damamge = (second_attacker.weapon_damage + dice_roll(6))
            first_attacker.health -= damamge
            print "{0} does {1}hp of damage to {2}".format(second_attacker.creature_type, damamge, first_attacker.creature_type)
            battle1.update(count_round)
            count_round +=1
            any_death = is_dead(first_attacker.health, second_attacker.health, count_round)
            #any_death = True
        dead(first_attacker.health, second_attacker.health)

def is_dead(hero, enemy, count_round):
    """checking if health is zero, how to include in each turn?"""
    if hero <= 0 or enemy <= 0:
        any_death = True
        return any_death
    else:   
        print "\n-------------- Round {0} --------------".format(count_round)

def dead(hero, enemy):
    if hero <= 0:
        print "you be dead"
    elif enemy <= 0:
        print "he be dead, kicked his ass"
    else:
        print "Well, there seems to be issues"
    quit()




def player_start():
    """Gather facts to create player"""
    absolutely_unused_variable = os.system("clear")
    player_choose = False
    print "Welcome to the awsome DR battle arena"
    print "Please choose a character from the following"
    x = 0
    for i in characters.character_dict:
        x += 1
        print "- {0}".format(i)
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
        print "- {0}".format(i)
    while weapon_choose != True:
        player_weapon = raw_input("> ").title()
        if player_weapon in characters.weapon_dict:
            absolutely_unused_variable = os.system("clear")
            print "Your {0} is now armed with a {1}".format(player_class, player_weapon)
            weapon_choose = True
        else:
            print "Incorrect choice, try again\n"
    for x in range(0, 10):
        print "\n"
        time.sleep(super_short)
    return player_class, player_weapon


if __name__ == "__main__":


    player_class, player_weapon = player_start()
    """alternative ways to extract the variables"""
    #foo = player_start()
    #print foo[0], foo[1]

    my_hero = characters.Hero(characters.character_dict[player_class], player_class, player_weapon)

    goblin_boss = characters.Enemy(100, "Goblin Boss", "Spear")
    print "Enemy list: {0}".format(len(characters.enemy_dict))
    print "Enemy weapons: {0}".format(len(characters.enemy_weapon_dict))
    for k, v in characters.enemy_weapon_dict.iteritems():
        print k, v

    # this is my way to randomly pick a character from the enemy dictionary
    x = random.randint(1, (len(characters.enemy_dict) - 1))
    print "X = {0}".format(x)
    for p, (k, v) in enumerate(characters.enemy_dict.iteritems()):
        # if the counter number equals the random number then pick this enemy
        if p == x:
            rand_enemy = k
    random_enemy = characters.Enemy(characters.enemy_dict.get(rand_enemy), rand_enemy, "Spear")
    battle1 = Arena(my_hero, random_enemy)
    battle1.fight()


    #is_dead(my_hero, my_hero.health)