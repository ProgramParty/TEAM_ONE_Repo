import time
from player import Player


def quest3():
    print("This is third quest.")
    time.sleep(2)
    print("For this quest, you have to actuallly track the Ice Dragon.")
    time.sleep(3)
    print("You will have to fight him really soon, so you better be prepared.")
    time.sleep(4)
    print("The Ice Dragon was last seen on the north part of your village.")
    time.sleep(3)
    print("It is time to take your revenge", Player.name)
    time.sleep(3)
    print("You gotta go near the northen parts of your village and find him\nWhen you arrive there, you will have to shop some weapons.")
    time.sleep(5)
    print("There are actually 3 different shops there wich offer weapons.")
    time.sleep(2)
    print("However, you are 12 years old.They will not offer you any weapons.")
    time.sleep(4)
    print("Or will they?")
    time.sleep(2)
    print("You have to try, you got nothing to lose.")
    time.sleep(3)
    print("I suggest you steal a horse and move as quick as possible.")
    time.sleep(3)
    qu3part2()


def qu3part2():
    print("So, there is this stable near you.")
    time.sleep(2)
    print("You know the drill.")
    time.sleep(1)
    print("There is an old man outside the stable, most likely the owner.")
    time.sleep(3)
    print("You: He is really old. I am not sure I can do this.")
    time.sleep(3)
    print("The Ice Dragon killed your mother. The only way to get to him\nis to get this horse and the fuck out of here.")
    time.sleep(5)
    print("You: Okay, fine!")
    time.sleep(1)
    print("..........you approach the old man..........")
    time.sleep(2)
    qu3in = input(
        "You have two options\nPunch him and knock him out(P), or ask him for one of his horses(A)").lower()

    if qu3in == "p":
        time.sleep(1)
        print("You punched the man so hard he is bleeding right now.")
        time.sleep(2)
        print("Jeez that is disturbing\nanyway get one horse and run.")
        qu3part3()

    if qu3in == "a":
        time.sleep(1)
        print("You: Sorry for the interaption. I was wondering\nif you could actually lend me one of your horses sir.")
        time.sleep(3)
        print("Old man: Arr. You betwer be jokwing if ywou thwink mwy howrses can be lwent. Arr.")
        time.sleep(4)
        exit()


def qu3part3():
    time.sleep(4)
    print("..........you got the first horse you saw..........")
    time.sleep(2)
    print("You: Holy shit! How am I supposed to make that shit run slower?")
    time.sleep(3)
    print("After a good 15 minutes of you riding that piece of junk\nyou actually arrive to the norhten parts of the village.")
    time.sleep(5)
    print("You: I can smell fear.... Something terrible has happened here.")
    time.sleep(3)
    print("Out of nowhere, you actually spot a humongous white castle.")
    time.sleep(3)
    print("You: Yep, that is it.")
    time.sleep(1)
    print("You can not fight him without weapons or armor!")
    time.sleep(2)
    print("There is a shop nearby, they might as well\nprovide you with weapons if you are actually lucky.")
    time.sleep(2)
