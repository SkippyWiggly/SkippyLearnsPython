print """
You enter a dark room with two doors.
Do you go through door #1 or door #2?
"""

door = raw_input(">  ")

if door == "1" or door == "#1":
	print """
	There's a giant bear here eating a cheese cake.  What do you do?
	1. Take the cake.
	2. Scream at the bear.
	"""
	
	bear = raw_input(">  ")
	
	if bear == "1" or bear == "1.":
		print "The bear eats your face off.  Good job!"
	elif bear == "2" or bear == "2.":
		print """
		The bear stops eating and turns to face you.
		He wipes the crumbs from his mouth and says "What do you want?"
		You respond with:
		1. "I didn't know bears could talk!"
		2. "I would like to eat some cheesecake."
		"""
		
		response = raw_input(">  ")
		
		if response == "1" or response == "1.":
			print "The bears scoffs and returns to his cheesecake.  Good job!"
		elif response == "2" or response == "2.":
			print "The bear roars and swipes at your face. You barely escape.  Good job!"
	else:
		print "Well, doing %s is probably better. Bear lumbers away." % bear
elif door == "2" or door == "#2":
	print """
	You stare into the endless abyss at Cthulhu's retina.  What do you see?
	1. Blueberries.
	2. Yellow jacket clothespins.
	3. Understanding revolvers yelling melodies.
	"""
	
	insanity = raw_input(">  ")
	
	if insanity == "1" or insanity == "2" or insanity == "1." or insanity == "2.":
		print "Your body survives powered by a mind of jello.  Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.  Good job!"
		
else:
	print "You stumble around and fall on a knife and die.  Good job!"