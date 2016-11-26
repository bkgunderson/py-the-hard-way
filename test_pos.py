import food_items


def receipt(food, nonfood):
    food_sub_total = food_items.food_sub(food)
    nonfood_sub = float(nonfood * 3.99)
    sub_total = nonfood_sub + food_sub_total
    nonfood_tax = float(nonfood_sub * 0.1278)
    food_tax = float(food_sub_total * 0.05257)
    total = nonfood_sub + nonfood_tax + food_sub_total + food_tax
    print "   Sub Total     $%s" % sub_total
    print "Non Food Tax     $%s" % nonfood_tax
    print "    Food Tax     $%s" % food_tax
    print "       Total     $%s" % total

print "How many 4-packs of Boulevard Breakfast Stout are you buying?"
stout = int(raw_input("> "))

print "How many non-food items are you buying?"
non_food_qty = int(raw_input("> "))

receipt((stout, 1, 1, 1), non_food_qty)
