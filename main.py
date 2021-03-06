import time

# import call to player
from player import Player

from quests import *

# Just putting this here for now, if you call this
# print(Player())
# it prints out the stats for the player


def start():
    print("Welcome to Remicon.")
    time.sleep(2)
    print("The most fun and creative command line RPG.")
    time.sleep(2)
    # Each part of player has a set, that changes the part on a class level
    # name takes 2 object in, cls and name, cls is the calling class so
    # Player in this case and name is what we want to change the players name to
    Player.name = input("So what is your name?: ")
    time.sleep(2)
    print(Player.name, "is such a cool name!")
    time.sleep(2)
    introductionask()


def introductionask():
    print("So do you wanna check the introduction?")
    time.sleep(1)
    intro = input("Y/N: ")
    if intro.lower() == "y":
        print("Great")
        time.sleep(2)
        introduction()
    elif intro.lower() == "n":
        print("Oh ok")
        time.sleep(2)
        print("Are you sure? The introduction is pretty important.")
        time.sleep(2)
        ninput = input("Y/N: ")
        if ninput.lower() == "y":
            print("Okay.")
            time.sleep(2)
            mission1()
        elif ninput.lower() == "n":
            print("Okay.")
            time.sleep(2)
            introduction()
        else:
            print("Something went wrong. Let us try again.")
            time.sleep(2)
            introductionask()
    else:
        print("Something went wrong.")
        time.sleep(2)
        print("Let us start over again.")
        time.sleep(2)
        introductionask()


def introduction():
    print("Once upon a time, in 1845 at a small village in Austria, citizens were attacked by the great force of dragons.")
    time.sleep(2)
    print("There were 5 different dragons.")
    time.sleep(3)
    print("Fire, Ice, Water, Electricity and Dark.")
    time.sleep(3)
    print("Soldiers tried as hard as they could.")
    time.sleep(3)
    print("But all of them got killed.")
    time.sleep(3)
    print("Dragons ruled the whole village, and no one could take action.")
    time.sleep(3)
    print("Everyhing seems pointless. Life in general. No reason to live anymore.")
    time.sleep(2)
    print("Dragons often choose prays and eat them like the monsters they are.")
    time.sleep(3)
    mission1()


def mission1():
    print("MOM, MOM NO")
    time.sleep(3)
    print("Ice Dragon: Too late now. ")
    time.sleep(3)
    print("YOU WILL PAY FOR THAT YOU SICK MONSTER.")
    time.sleep(3)
    print("Ice Dragon: Your mother tastes great kid.")
    time.sleep(3)
    print("..........the ice dragon catches the kid..........")
    time.sleep(3)
    print("LEAVE ME ALONE YOU BASTARD.")
    time.sleep(3)
    print("Ice Dragon: How old are you?")
    time.sleep(3)
    print("I am a 12 year old that will soon be your killer.")
    time.sleep(3)
    print("Ice Dragon: You kiss your mother with that mouth?")
    time.sleep(3)
    print("Ice Dragon: Or used to anyway...")
    time.sleep(3)
    print("Ice Dragon: I will give you one last chance...")
    time.sleep(2)
    print("Ice Dragon: You better be grateful for that.")
    time.sleep(4)
    print("..........the ice dragon throws the 12 year old kid away and slowly leaves the place..........")
    time.sleep(3)
    print("I swear to my dead mother's corpse I will take revenge for that. You better be prepared.")
    time.sleep(3)
    tutorial()


def tutorial():
    print("In Remicon, you have to slay all 5 dragons in order to bring back peace in your village.")
    time.sleep(4)
    print("You will be able to form relationships with other heroes that may be able to help you.")
    time.sleep(4)
    print("Every single choice can be proven a mistake.")
    time.sleep(4)
    print("Be extremely careful with what you choose. This game heavily relies on correct choices.")
    time.sleep(4)
    print("You will also be able to earn money through special quests.")
    time.sleep(4)
    print("You will have the option to spend your money on better weapons or armor.")
    time.sleep(4)
    print("For now you only have one knife.")
    time.sleep(4)
    print("Killing dragons will also grant you money.")
    print("Enjoy!")

    time.sleep(3)
    quest1.quest1()
    time.sleep(2)
    quest2.quest2()
    time.sleep(2)
    quest3.quest3()
    time.sleep(2)
    # add the shop thing here


start()
