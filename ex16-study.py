from sys import argv

script, filename = argv

print "Let's open and read %r" % filename
target = open(filename, 'r')
print target.read()

print "Now we close the file."
target.close()