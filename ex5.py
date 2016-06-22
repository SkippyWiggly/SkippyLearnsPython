name = 'Zed A. Shaw'
age = 35
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about {}.".format(name)
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He has {} eyes and {} hair.".format(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#paying attention to detail on typing the next line
print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)