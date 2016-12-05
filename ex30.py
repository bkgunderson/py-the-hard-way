people = 30
cars = 30
trucks = 45


# If cars is greater than people, print "We should take the cars."
if cars > people:
    print "We should take the cars."
# If cars is less than people, print "We should not take the cars."
elif cars < people:
    print "We should not take the cars."
# If cars is neither greater than nor less than people, print "We can't decide."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if cars >= people or trucks >= people:
    print "No need for carpools! Pollute away!"
elif people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
