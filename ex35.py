from sys import exit
import logging


def gold_room():
    print "This room is full of gold. How much do you take?"
    choice = raw_input("> ")
    try:
        how_much = int(choice)
        if how_much < 50:
            print "Nice, you're not greedy, you win!"
            exit(0)
        else:
            dead("You greedy turd!")
    except Exception as e:
        logging.exception(e)
        dead("Man, learn to type a number.")


def bear_room():
    print """
    There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?
    """
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulu_room():
    print """
    Here you see the great evil Cthulu.
    He, it, whatever stares at you and you go insane.
    Do you flee for your life or eat you head?
    """

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


def start():
    print """
    You are in a dark room.
    There is a door to your right and left.
    Which one do you take?
    """

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
