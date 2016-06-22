
def loop(limit, increment):
	i = 0
	numbers = []
	
	while i < limit:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i += increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	return numbers


def loop2(limit, increment):
	j = 0
	numbers = []
	
	for j in range(j, limit, increment):
		print "At the top j is %d" % j
		numbers.append(j)
		
		j += increment
		print "Numbers now: ", numbers
		print "At the bottom j is %d" % j

	return numbers
		
x = loop(9, 2)
y = loop2(9, 2)


print "The numbers: "

for num in x:
	print num