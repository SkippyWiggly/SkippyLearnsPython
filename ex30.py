people = 25
cars = 25
trucks = 30


if cars > people or trucks > cars:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."
	
if people > trucks:
    print "Alright, let's just take the trucks."
else:
	print "Fine,let's stay home then."