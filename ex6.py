#variables with the string formats and regular
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#printing the variables containing the string formats
print x
print y

#printing the variables as string formats
print "I said: %r." % x
print "I also said: '%s'." % y

#defining a true/false variable and
#having a variable with string format with no definition thing
#after it
not_hilarious = False
hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

#printing the string variable and choosing the answer
#by selecting which format now
print joke_evaluation % not_hilarious

#defining two string variables
w= "This is the left side of..."
e = "a string with a right side."

#printing the two strings as variables.
print w + e