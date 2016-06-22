from sys import argv

#takes an argument when starting the program,
#in the form of a txt file
script, input_file = argv

#defining a function print_all that prints the
#entire contents of the input 'f'
def print_all(f):
	print f.read()

#defining a function rewind that uses the seek
#function to return to the 0th byte (beginning)
def rewind(f):
	f.seek(0)

#defining a function print_a_line that prints
#what line you're on (line_count) and then prints
#the contents of that line (readline())	
def print_a_line(line_count, f):
	print line_count, f.readline(),

#sets current_file to open the file input at the
#start of the program	
current_file = open(input_file)

print "First let's print the whole file:\n"

#uses print_all to print the contents of the whole file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#uses rewind to go back to beginning of file
rewind(current_file)

print "Let's print three lines:"

#sets line to the first line in file
current_line = 1
#prints the line number that was set just before and
#then the contents of that line from current_file
print_a_line(current_line, current_file)

#sets current line to be the next line in the file
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
















