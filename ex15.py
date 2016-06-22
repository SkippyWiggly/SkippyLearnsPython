#imports argv to use for user input
from sys import argv

#outlines the two inputs we need from user
#(the script to load and the filename we'll load)
script, filename = argv

#defining variable txt as a file object that is opened via the open function.
#not necessary to define txt variable, can simply do open(filename).read()
#later when I want to read the file
txt = open(filename)

#print out filename that is typed in before running
print "Here's your file %r" % filename
#commanding the file that was opened in the txt variable to be "read" (printed)
print txt.read()

#asking for input, presumably the same filename as before
print "Type the filename again:"
#set new variable file_again to that filename
file_again = raw_input("> ")

#defining new variable txt_again to the open the file inputted by user
txt_again = open(file_again)

#commanding the file opened in txt_again definition to be read
print txt_again.read()

txt.close()
txt_again.close()