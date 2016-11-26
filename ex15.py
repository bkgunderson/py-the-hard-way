from sys import argv

script, filename = argv

# If an invalid filename is entered (for example: NOT_A_FILE,
# the following error will result when running open():
# IOError: [Errno 2] No such file or directory: 'NOT_A_FILE'
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

# If an invalid file_again is entered (for example: NOT_A_FILE,
# the following error will result when running open():
# IOError: [Errno 2] No such file or directory: 'NOT_A_FILE'
txt_again = open(file_again)

print txt_again.read()
txt_again.close()