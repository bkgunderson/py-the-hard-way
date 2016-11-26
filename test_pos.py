import food_items
MO_FOODTAX = 0.05257


def receipt(food, nonfood):
    food_sub_total = food_items.food_sub(food)
    nonfood_sub = float(nonfood * 3.99)
    sub_total = nonfood_sub + food_sub_total
    nonfood_tax = float(nonfood_sub * 0.1278)
    food_tax = float(food_sub_total * MO_FOODTAX)
    total = sub_total + nonfood_tax + food_tax
    print "   Sub Total     $%s" % sub_total
    print "Non Food Tax     $%s" % nonfood_tax
    print "    Food Tax     $%s" % food_tax
    print "       Total     $%s" % total

print "How many 4-packs of Boulevard Breakfast Stout are you buying?"
stout = int(raw_input("> "))

print "How many bottles of Chilean Cabernet Sauvignon are you buying?"
cab_sauv = int(raw_input("> "))

print "How many 34 oz bottles of Olive Oil are you buying?"
evoo = int(raw_input("> "))

print "How many pounds of dry green lentils are you buying?"
grn_lent = float(raw_input("> "))

print "How many non-food items are you buying?"
non_food_qty = int(raw_input("> "))

receipt((stout, cab_sauv, evoo, grn_lent), non_food_qty)
