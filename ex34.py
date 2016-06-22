
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
"""
print "The animal at 1: " + animals[1]

print "The third animal: " + animals[2]

print "The first animal: " + animals[0]

print "The animal at 3: " + animals[3]

print "The fifth animal: " + animals[4]

print "The animal at 2: " + animals[2]

print "The sixth animal: " + animals[5]

print "The animal at 4: " + animals[4]
"""
number = 1

print "\n\nHere are the wonderful animals in our zoo:"

for x in animals:
	print number, "\b.  %s" % x
	number +=1

employees = ['Jim', 'Joe', 'Marcus', 'Mark', 'Oliver', 'Oscar', 'Stan', 'Steve']

print "\nHere are the employees at the company,"
print "listed in order of when they were hired:\n"
"""

for i in employees:
	print number, "\b.  %s" % i
	number += 1

print "\n\nThe previous list was incorrectly ordered (alphabetically)."
print "Here is the revised list:\n"	
"""
print "1.  " + employees[3]
print "2.  " + employees[5]
print "3.  " + employees[7]
print "4.  " + employees[0]
print "5.  " + employees[1]
print "6.  " + employees[6]
print "7.  " + employees[2]
print "8.  " + employees[4]


jobs = ['zoo keeper', 'janitor', 'veterinarian', 'mechanic']

e = len(employees)
j = len(jobs)
a = len(animals)

print "\nThere are %d animals at our zoo!" % a
print "Currently, %d employees fill the %d jobs, where" % (e, j)
print "they care for the animals and maintain the park!\n\n"

print employees[1], "is the head", jobs[0], "\b."
print "He primarily looks after the", animals[0], "\b,", animals[3], "\b, and the", animals[5], "\b.\n"

print employees[6], "helps", employees[1], "with the", animals[3], "as an assistant", jobs[0], "\b.\n"

print employees[7], "is also an assistant", jobs[0], "\b. He works in the reptile house with the", animals[1], "\b.\n"

print "Every good park needs a", jobs[3], "to keep the operation running smoothly."
print "We can always count on", employees[2], "to keep the zoo in top shape!\n"

print "Don't get", employees[2], "confused with", employees[3], "\b!"
print employees[3], "is our head", jobs[2], "\b."
print "He works primarily with the", animals[0], "\b,", animals[2], "\b,", animals[3], "\b, and", animals[5], "\b.\n"

print employees[0], "is the special", jobs[2], "\b. He works with the", animals[1], "and", animals[4], "\b.\n"

print "To keep the park clean, we have", employees[5], "as our", jobs[1], "\b.\n"

print "And our newest hire is", employees[4], "\b, who is also an assistant", jobs[0], "\b."
print "He works with our newest animal: the", animals[4], "\b.\n"