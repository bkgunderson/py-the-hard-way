def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def local_grocery_receipt(craft_beer, chilean_wine, olive_oil, paper_towels, grocery, nonfood, coffee, eggs, lentils):
    food_sub = float((craft_beer * 12.09) + (chilean_wine * 9.89) + (olive_oil * 23.09) + (paper_towels * 1.89) +
                     (grocery * 8.50) + (coffee * 11.89) + (eggs * 4.69) + lentils * 2.19)
    nonfood_sub = float(nonfood * 3.99)
    sub_total = nonfood_sub + food_sub
    nonfood_tax = float(nonfood_sub * 0.1278)
    food_tax = float(food_sub * 0.05257)
    total = nonfood_sub + nonfood_tax + food_sub + food_tax
    print "   Sub Total     $%s" % sub_total
    print "Non Food Tax     $%s" % nonfood_tax
    print "    Food Tax     $%s" % food_tax
    print "       Total     $%s" % total


print "By the way, here is a sample local grocery receipt: "
local_grocery_receipt(1, 1, 1, 1, 1, 1, 1, 1, 2.37)

print """
Let's see how much you might spend at this grocery today.
We'll start by running through each item you intend to purchase.
"""

print "How many four-packs of Founder's Breakfast Stout are you going to buy?"
stout = int(raw_input("> "))

print "How many bottles of Galan Cabernet Sauvignon are you going to buy?"
cab_sauv = int(raw_input("> "))

print "How many 34 oz bottles of olive oil are you going to buy?"
evoo = int(raw_input("> "))

print "Okay, here's a projected receipt for what you intend to buy:"
local_grocery_receipt(stout, cab_sauv, evoo, 0, 0, 0, 0, 0, 0)
