from sys import argv

#script, first, second, third = argv

#print "This script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third


#script, number_of_ponies = argv
#print "This script is called:", script
#print "The variable concerning ponies is:", number_of_ponies


#script, first = argv
#print "This script is called:", script


#script, ponies, cows, horses, hens = argv
#print "This script is called:", script
#print "Variable for ponies:", ponies
#print "Variable for cows:", cows
#print "Variable for horses:", horses
#print "Variable for hens:", hens
#print "Variable for food:", hay_total


#script, ponies, horses = argv
	
#print "This script is called:", script
#ponies = raw_input('What would you like your variable for ponies to be called?  ')
#horses = int(raw_input('How many horses do you have?  '))
#print "This is variable you wanted for ponies:", ponies
#print "This is how many horses you have:", horses


script, fruit, candy = argv

print "This script is called:", script

#fruit = raw_input('What is your favorite fruit?  ')
#candy = raw_input('What is your favorite candy? ')
#print "Your favorite fruit is:", fruit
#print "Your favorite candy is:", candy

fruit = int(fruit) * 52
candy = int(candy) * 52
print """
If you ate like this every week,
In one year you'd eat:
\t %d pieces of fruit and
\t %d pieces of candy.
""" % (fruit, candy)

#fruit = int(raw_input('How many apples did you eat this week?  '))
#fruit = fruit * 11.4
#candy = int(raw_input('How many Hershey\'s bars did you eat this week?  '))
#candy = candy * 24
#print "You consumed approximately %d grams of sugar from apples this week." % fruit
#print "And you consumed approximately %d grams of sugar from Hershey's bars this week." % candy
