
#ASCII bell sound
#print '\a'

#ASCII backspace
#print "stuff.\b", "\b", "more stuff."

#ASCII formfeed
#print "stuff.", "\f", "more stuff."

#ASCII linefeed
#print "stuff.\nmore stuff."

#Unicode symbols
#print u"\N{BLACK SPADE SUIT}"

#Carriage return, no loop. Too fast to see first word
#print "fuck\rHello"

#ASCII vertical tab
#print "Hello,\vHow are you today?"

#testing %r and %s
#i = "I don't \"understand\"..."
#j = 'I can\'t "hear"...'
#print "%r what you're saying" % i
#print "%s what you're saying" % i
#print "%r what you're saying" % j
#print "%s what you're saying" % j

#creating my own "complex" series of escapes
print '\a'
x = "warning sound"
y = "\n\t* try turning off your speakers or\n\t* try not running this program."
print "You heard a %s." % x
print 'If you don\'t want to hear that again, you can: %s' % y