import random

def play_again():
	answer = raw_input("Play again? Y/N: ")
	return answer
	
def dice_roll():
	roll = random.randint(1, 20)
	return roll

play = "Y"

while play == "Y" or play == "y":
	impressed = False
	
	print "You are a warrior of which race?"

	race = raw_input("dwarf/elf/human: ")

	print 
	"""
You find yourself in a tavern about half full with a mix of clients.
You are sipping from a tankard of mediocre ale...
	"""

	if race == "dwarf":
		str = 18
		dex = 12
		con = 18
		int = 10
		wis = 14
		cha = 10
		print """
You drain your tankard and burp noisily.
You wipe the liquid from your beard and waddle to the bartender.
When you get to the bar and up on a stool, you:
* LOOK around because the bartender is busy
* ORDER another ale after getting the bartender's attention
		"""
	
		firstchoice = raw_input("> ")
	
		if firstchoice == "LOOK" or firstchoice == "look":
			print "."
		elif firstchoice == "ORDER" or firstchoice == "order":
			print "."
		else:
			print "Choose from LOOK and ORDER."
			play = play_again()
	
	elif race == "elf":
		str = 16
		dex = 15
		con = 13
		int = 15
		wis = 16
		cha = 10
		print """
You look into your tankard and see your beautiful reflection.
As you take another sip, your excellent hearing allows you to
overhear a conversation from a nearby table of humans.
They seem to be talking about news from the nearby town.
You decide to:
* JOIN them
* IGNORE them and finish your ale
		"""
	
		firstchoice = raw_input("> ")
	
		if firstchoice == "JOIN" or firstchoice == "join":
			print "."
		elif firstchoice == "IGNORE" or firstchoice == "ignore":
			print "."
		else:
			print "Choose from JOIN and IGNORE."
			play = play_again()
	
	elif race == "human":
		str = 18
		dex = 16
		con = 15
		int = 11
		wis = 12
		cha = 17
		print """
You drink heartily and laugh with your friends.
The talk turns to your recent excursion in the nearby town.
A roving band of thieves were involved, and you suffered a painful
wound to your arm. You'd rather not remember that embarassing
fight.
You decide to:
* YELL about the bartender's beautiful daughter
* JOKE about how your buddy missed five shots in a row
		"""
		
		firstchoice = raw_input("> ")
	
		if firstchoice == "YELL" or firstchoice == "yell":
			print "."
		elif firstchoice == "JOKE" or firstchoice == "joke":
			print "."
		else:
			print "Choose from YELL or JOKE."
			play = play_again()

	else:
		print "Select from dwarf, elf, or human."
		play = play_again()