# Assigns a string to the following four variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know {0:s} and those who {1:s}.".format(binary, do_not)

# prints two string variables on two lines
print x
print y

# prints two strings with variables inside them using formatting
print "I said: %r." % x
print "I also said: '%s'." % y

# assigns a value to bool variable hilarious and string variable joke_evaluation
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the two variables using the formatting in joke_evaluation to display hilarious as well
# I can't fully articulate what this line is doing
print joke_evaluation % hilarious

# assigns string values to two variables
w = "This is the left side of..."
e = "a string with a right side."

# prints the concatenation of two string variables
print w + e

# prints the result of the __builtin__ function callable
print callable(hilarious)
