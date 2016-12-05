def append_to_numbers(the_list):
    i = 0
    print "What's the upper limit?"
    limit = raw_input("> ")
    print limit
    while i < int(limit):
        print "At the top i is %d" % i
        the_list.append(i)
        i += 1
        print "Numbers now: ", the_list
        print "At the bottom i is %d" % i
    return the_list

numbers = []
numbers = append_to_numbers(numbers)
print "The numbers: "

for num in numbers:
    print num
