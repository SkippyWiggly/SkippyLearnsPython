#print "How old are you?",
#age = raw_input()
#print "How tall are you?",
#height = raw_input()
#print "How much do you weigh?",
#weight = raw_input()

#print "So, you're %s old, %s tall, and %s heavy." % (age, height, weight)

#my own input program
#print "What's your name?",
name = raw_input('What\'s your name? --> ')
#print "How old are you, %s?" % name,
age = int(raw_input('How old are you, %s? --> ' % name))
#print "How tall are you now? (in.)",
height = int(raw_input('How tall are you now? (in.)--> '))
young_age = age - 10
#print "How tall were you when you were %d? (in.)" % young_age,
young_height = int(raw_input('How tall were you when you were %d? (in.)--> '
	% young_age))
height_diff = height - young_height

print 'So, you\'ve grown %d inch(es) since you were %d years old!' % (height_diff, young_age)