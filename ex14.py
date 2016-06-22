from sys import argv

script, user_name, season = argv
prompt = '----'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "Is the weather today nice for %s?" % season
weather = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %s. Not sure where that is.
But you said %r about if the weather is nice there today.
You have a %s computer. Nice.
""" % (likes, lives, weather, computer)