from sys import argv

#defines the arguments given in the opening of the file
#the first is the program (or script), the second is
#called filename, and it's the variable given to what is
#entered when you're opening the file
#example of opening file: "python ex16.py test.txt"
script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)\nIf you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

#apparently target.truncate is not needed since the file was opened in 'write'
#mode (above: target = open(filename, 'w')). Opening in 'write' mode automatically
#truncates (erases) the file.
print "Truncating file. Goodbye!"
target.truncate

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()