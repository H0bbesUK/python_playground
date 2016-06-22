# -*- coding: utf-8 -*-

import time
from sys import exit
from random import randint, sample, choice
import random

timer = 0.6
fast_timer = 0.15
long_timer = timer * 3
super_long_timer = timer * 4
endgame = False
current_count = 0
done = False
name = []
#print "random! %i" % randint(0, 100)


def scroll_timer(num_lines, ticktock):
	for i in range(0, num_lines):
		print "\n"
		time.sleep(ticktock)


#############################################################
#					 questions function                     #
############################################################# 
"""
this function askes questions from the passed list, number of questions, 
the monster_dict (for death) and times played
grabs a random question, asks(key) and checcs against answer (value)
there was a bug initially, and question could be asked again - so now the asked questionsd is removed from the list
"""
def questions(question_list, number_questions, monster, current_count):
	i = 0
	#print question_list
	while i < number_questions: 
		x = random.choice(question_list.keys())
		quest_ask = raw_input(x + " ").lower()
		if quest_ask == question_list.get(x):
			if (i + 1) < number_questions:
				print "Correct, another question for you.."
			i += 1
			del question_list[x]
			#print question_list
		else:
			scroll_timer(3, fast_timer)
			print monster_dict.get(monster)
			dead(current_count)
	return


#############################################################
#					  rooms function                        #
############################################################# 

# intro writes to a list with single value (0) 
def intro(current_count):
	scroll_timer(32, fast_timer)
	the_name = raw_input("Your name is? ")
	name.append(the_name)
	scroll_timer(2, timer)
	start(current_count)
	#complete(current_count)


def dead(current_count):
	print "\nDo you wish to play again?"
	print "Type 'y' or 'n'?"
	chosing(dead_options, current_count)


def final(current_count):
	print "\nYou finally arrive in the treasure room,"
	time.sleep(timer)
	print "It is brightly lit with flaming torches."
	time.sleep(timer)
	print "In the middle of the room stands the tresure chest."
	chosing(chest_options, current_count)


def complete(current_count):
	n = random.randint(1,2)
	if n == 1:
		print "You open the chest, revealing riches beyond you wildest dreams..."
		time.sleep(super_long_timer)
		print "...and a " + u"\u00a3" + "1 scratch card."
	else:
		print "You open the chest, an adventurer has already beaten you to it, all that is left is..."
		time.sleep(super_long_timer)
		print "...a graze box voucher."
	time.sleep(long_timer)
	print "\nWell done %s, you have completed the game." % name[0]
	dead(current_count)

def quit(counter):
	if counter < 2:
		print "You only played the game %d time." % counter
	else:
		print "You played the game %d times." % counter
	print "Bye"
	exit(0)


# the start
def start(current_count):
	print("""\
       [][][] /""\ [][][]  
        |::| /____\ |::|
        |[]|_|::::|_|[]|
        |::::::__::::::|
        |:::::/||\:::::|
        |:#:::||||::#::|
       #%*###&*##&*&#*&##
      ##%%*####*%%%###*%*#
                    """)
	print """
Welcome to the treasure castle, %s.
you have played this game %d times.
You look around and see a large castle with big double oak doors..""" % (name[0], current_count)
	current_count += 1
	time.sleep(timer)
	print """
You open the doors and walk into the grand square hallway
Looking ahead you see a door to the left, and a door to the right"""
	time.sleep(timer)
	print "And a small door on the right hand wall..."
	chosing(start_options, current_count)


# back to the start
def mainhall(current_count):
	scroll_timer(2, long_timer)
	print "You are back in the main hallway, Looking ahead you see a door to the left, and a door to the right"
	print "And a small open door on the right hand wall..."
	chosing(start_options, current_count)


# octopus room, uses the questions() function
def octopus(current_count):
	scroll_timer(2, long_timer)
	print """
You step into the room, the door slams shut behind you.
A large Octopus dominates the room.
You are unsure how it is able to live outside of the ocean.
Stranger still it speaks to you\n"""
	time.sleep(timer)
	print """
	                    .---.         ,,
                 ,,        /     \       ;,,'
                ;, ;      (  o  o )      ; ;
                  ;,';,,,  \  \/ /      ,; ;
               ,,,  ;,,,,;;,`   '-,;'''',,,'
              ;,, ;,, ,,,,   ,;  ,,,'';;,,;''';
                 ;,,,;    ~~'  '';,,''',,;''''  
                                    '''
	"""
	print """
Hello there %s, I have been expecting you.
I have a few questions for you, get them right and you can live.
Get them wrong and I'll suck your brains out""" % name[0]
	questions(octopus_questions, 2, 'monster_octopus', current_count)
	time.sleep(timer)
	print "\nWell done %s, as promised I will let you live and be on your way" %  name[0]
	print "The speaking octopus shows you a door straight ahead and a door to the left."
	time.sleep(timer)
	print "Which door do you chose?"
	chosing(octopus_options, current_count)


def lion(current_count):
	scroll_timer(2, long_timer)
	print """
You walk into a brightly lit room,
There is a huge great lion in this room.
'Nice mane!' you exclaim.
'Thanks', says the lion, adjusting his monocle, 
'I am a hipster lion, and as this is a text adventure game I have questions.'"""
	questions(lion_questions, 2, 'monster_lion', current_count)
	print "'You may pass' speaks the lion, tipping his fedora."
	print "You must go straight through the door behind me."
	time.sleep(timer)
	print "\nYou follow his instructions"
	time.sleep(timer)
	skeleton(current_count)

# pit room, hidden trap door (random number)
def pit(current_count):
	scroll_timer(2, long_timer)
	dice_roll = randint(0, 100)
	print "Pit Room"
	if dice_roll > 75:
		print """
\nPhew, you walked into the room and just miss stepping
onto a trap door, it falls open revealing a bottomless pit."""
		chosing(pit_options, current_count)
	else:
		print """
\nYou walk into the room, 'CLICK!!' stepping onto a trap door
The last thing you are aware of is the long time it takes to hit the bottom...."""
		print "(You are dead)"
		dead(current_count)


def bats(current_count):
	scroll_timer(2, long_timer)
	num_bat_guesses = 4
	print """
\nWe are the bats that like to poo a-lot!
We will ask you to guess how many of us there are,
guess correctly within %i guesses and we will let you by,
guess wrong and we will poo on you.
"""	% num_bat_guesses
	bat_number = randint(2, 100)
	bat_guess = None
	bat_won = False
	# error handling, while true = infinate loop (break will exit)
	# check (try) if it is a number, break if is a number
	for counter in range(0, num_bat_guesses): # number of guesses allowed
		while True:
			try:
				bat_guess = raw_input("Guess away: ")
				bat_guess = int(bat_guess)
				break
			except ValueError:
				print "The bats squeak together 'Don't be silly, that isn't a number!'"
		if bat_guess == bat_number:
			bat_won = True
			break
		print "\nLots of poo falls on you..."
		print "You are %i bats away from our total\n." % abs(bat_guess - bat_number)

	if bat_won != True:
		print "Out of guesses - Poo'ed to death."
		dead(current_count)
	else:
		chosing(bat_options, current_count)


def dinosaur(current_count):
	print "\nYou walk into a dark room, the door closes behind you with a gentle click."
	scroll_timer(2, long_timer)
	print """
Torches light up. Two huge dinosaurs are somehow crammed into the modest hall.
The place seems to bend the laws of physics - like a child dreamt up this scenario.
The dinosaur on the left is a dark green, he looks nasty....and hungry.
The other, on the right hand side is bright pink."""
	COLOUR = ('pink', 'green')
	scroll_timer(1, super_long_timer)
	print "The %s dinosaur speaks, 'As you've guessed, we have questions.." % random.choice(COLOUR)
	print "'But first, which one of us would you like to ask the questions? - Pink or Green?'"
	while True:
		dino_asker = raw_input("> ").lower()
		if dino_asker == 'pink' or dino_asker == 'green':
			if dino_asker == 'pink':
				print "'Hello', says the pink dinosaur."
				questions(pink_dinosaur_questions, 2, 'monster_dino_pink', current_count)
			else:
				print "'Hello', says the green dinosaur."
				questions(green_dinosaur_questions, 4, 'monster_dino_green', current_count)
			scroll_timer(4, fast_timer)
			print "\n'Well done, you may pass' says the %s dinosaur." % dino_asker
			print "The dinosaurs show you the only exit, which was hidden behind the %s dinosaur." % dino_asker
			final(current_count)
			return
		else:
			print "Pink Dinosaur, or Green Dinosaur?"
	#one is green, the other bright pink

# would like a list, if you die, you get added to list 
def skeleton(current_count):
	skel_picked = False
	# some_list[start:stop:step]
	good_list = skeleton_list[1::2]
	bad_list = skeleton_list[0::2]
	scroll_timer(2, long_timer)
	print """
You emerge into a dank cold dungeon.
You are aware you are not alone.
Four undead join you in the dungeon.
Well, %i colourful skeletons to be exact.
\n(Press enter to continue)""" % len(skeleton_list)
	raw_input(">")
	#print "good: %r" % good_list
	#print "bad: %r" % bad_list
	print "Which of us is good, which of is bad?"
	scroll_timer(1, timer)
	print "The only clue you have is our colours: "
	time.sleep(timer)
	for colour in skeleton_list:
		print colour + " skeleton"

	while skel_picked != True:
		skel_choice = raw_input("Pick one of us..").lower()
		if skel_choice in good_list:
			print "You picked well."
			skel_picked = True
			print"The skeletons kindly show you the exit."
			final(current_count)
		else:
			if skel_choice in bad_list:
				print "You made a poor choice."
				scroll_timer(1, long_timer)
				print "The skeletons surround you and rip your skin off. You are one of them now."
				skeleton_list.append(other_skel_colours.pop(0))
				scroll_timer(2, long_timer)
				dead(current_count)
			else:
				print "You picked none of us."
	return
	print "This is the escape"
	# pass





def generic(current_count):
	print "Placeholder."
	print "played %d times." % current_count
	# pass

# these are all the rooms
start_options = {'left': octopus, 'right': lion, 'small': pit, 'small door': pit, 'quit': quit}
octopus_options = {'left': dinosaur, 'left door': dinosaur, 'forward': bats, 'straight ahead': bats, 'ahead': bats, 'quit': quit}
skeleton_options = {'cat': generic, 'up': generic, 'forward': generic, 'small door': generic, 'quit': quit}
bat_options = {'forward': final, 'straight ahead': final, 'ahead': final, 'quit': quit}
dinosaur_options = {'forward': final, 'straight ahead': final, 'ahead': final, 'quit': quit}
final_options = {'cat': generic, 'up': generic, 'forward': generic, 'small door': generic, 'quit': quit}
pit_options = {'exit': mainhall, 'back': mainhall, 'go back': mainhall, 'quit': quit}
dead_options = {'yes': start, 'y': start, 'no': quit, 'n': quit, 'quit': quit}
chest_options = {'open': complete, 'open chest': complete, 'quit': quit}

# these are the questions and answers
octopus_questions = {'What is 4 + 5?': '9', 'What colour do you get if you mix blue and yellow?': 'green', 'What is 12 - 3?': '9', 
'If you mix red and white, what colour do you get?': 'pink', 'What is 3 + 6?': '9', 'What is 15 - 6': '9',  }
green_dinosaur_questions = {'What is 7 + 5?': '12', 'What is 3 + 12?': '15', 'What is 4 + 10?': '14', 'What is 10 + 10?': '20', 
'What is 6 + 6?': '12', 'What is 7 + 7?': '14', 'What is 5 + 5?': '10', 'What is 4 + 4?': '8'   }
pink_dinosaur_questions = {'What is 10 - 5?': '5', 'What is 12 - 3?': '9', 'What is 7 - 4?': '3', 'What is 14 - 5?': '9' }
lion_questions = {'What is 20 - 10?': '10', 'What is 20 + 5?': '25', 'As well as sunlight, what do plants need to grow?': 'water',
'What is the opposite of left?': 'right', 'Which animals live in the sea?': 'fish', 'What animals fly in the sky?': 'birds' }
# these are the ways of death
monster_dict = {'monster_octopus': 'SLURP!! The octopus delivers on his promise and sucks your brains out!', 
'monster_dino_green': 'CRUNCH!! The green dinosaur gobbles you head off!', 
'monster_dino_pink': 'MUNCH!! The pink dinosaur swallows you up!',
'monster_lion': 'ROAR!! The lion rips you to bits!'}

skeleton_list = ['green', 'red', 'yellow', 'black']
other_skel_colours = ['pink', 'brown', 'white', 'purple' ]


#############################################################
#					Main option choosing                    #
############################################################# 

def chosing(dictionary, current_count):

	while done !=True:
		choice = raw_input("\nWhat do you want to do? ").lower()
		if choice in dictionary:
			print "\nYou chose " + choice
			dictionary[choice](current_count)
			done == True
		else:
			print "Sorry, you can't do '%s'.\n" % choice
			last_item = len(dictionary)
			j = 0
			print "Try: "
			for i in dictionary:
				j += 1
				time.sleep(0.35)
				if j != last_item:
					print i + " or.."
				else:
					print i+".\n"




intro(current_count)
exit(0)

