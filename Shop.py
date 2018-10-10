import time
try:
    name = player.name
    coins = player.coins
    drgnskilled = player.drgnskilled
except NameError:
    name = "edge"
    coins = 1000
    drgnskilled = 0

#apologies for the bad var names- feel free to change them

def mainshop():
    print("Welcome mighty " + name + " to Alfonso's shop- the finest shop in the realm! Haha!")
    time.sleep(2)
    print("First, we must see how many coins you have.")
    time.sleep(2)


    if coins > 999:
        print("Remarkable! You have enough to survive! Or do you? Haha! ")
        time.sleep(2)
        print("You now have the option to purchase weapons, armour or leave the shop.")
        time.sleep(2)
        print("Weapons are vital to destroy the dragons! ")
        time.sleep(2)
        print("...But if you want to protect yourself, you need armour!")
        time.sleep(2)
        print("So warrior "+ name + " what shall you choose?")
        time.sleep(2)
        wachoice = input("Weapons?(W) Armour?(A) Or would you like to leave?(E) ").lower()
        time.sleep(2)

        if wachoice == "w":
            print("Haha! I would have chosen this myself! For I was once the bravest warrior in our realm! Haha! ")
            time.sleep(2)
            if drgnskilled == 0:
                print("I see this shall be your first weapon!")
                time.sleep(2)
                print("Well then, you must know that there are two classes: Light and Heavy")
                time.sleep(2)
                print("The light class contains the stealth blade and mini crossbow-the most revered light weapons for an assassin. Haha!")
                time.sleep(2)
                print("While, the heavy class contains the sword and longbow- perfect for a warrior such as yourself. Haha!")
                time.sleep(2)
                print("So then, what shall it be? Light or Heavy? Assassin or Warrior ?")
                time.sleep(2)
                weapon = input("Light?(L) or Heavy?(H)").lower()
                if weapon == "l":
                    print("I knew from the moment you shoved that blade in Gary's brain that you were an assassin. Haha!")
                    time.sleep(2)
                    print("Here you are then...")
                    time.sleep(2)
                    print("...Assassin!")
                    time.sleep(2)
                    print("(You receive the fire stealth blade and mini crossbow- perfect for defeating the ice dragon)")
                    time.sleep(2)
                    altcoins = coins - 1000
                    print("(You now have " + str(altcoins) + " coins...")
                    weapon = "light"
                    print("Goodbye...")
            
            elif drgnskilled >= 1:
                print("Back again are you?")
                time.sleep(2)
                print("I thought you'd be dead by now. Haha!")
                time.sleep(2)
                print("Well then I see you require a weapon to defeat the next dragon.")
                time.sleep(2)
                if drgnskilled == 1:
                    print("Here is the ice knife and mini-crossbow to defeat the fire dragon! Haha ")
                    time.sleep(2)
                    altcoins = coins - 1000
                    weapon = "ice"
                elif drgnskilled == 2:
                    print("Here is the electric knife and mini-crossbow to defeat the water dragon! Haha ")
                    time.sleep(2)
                    altcoins = coins - 1000
                    weapon = "electric"
                elif drgnskilled == 3:
                    print("Here is the water knife and mini-crossbow to defeat the electric dragon! Haha ")
                    time.sleep(2)
                    altcoins = coins - 1000
                    weapon = "water"
                elif drgnskilled == 4:
                    print("Here is the light knife and mini-crossbow to defeat the dark dragon! Good luck... ")
                    time.sleep(2)
                    print("You'll need it...")
                    time.sleep(2)
                    altcoins = coins - 1000
                    weapon = "light"
                



        
        elif wachoice == "a":
            print("Hmm... Worried about protection are you? I knew you were weak from the moment you entered my prestigious store! Haha!")
            time.sleep(2)
            print("Very well, it seems I must give it to you.")
            time.sleep(2)
            print("Just take it. I will give it to you for free. ")
            time.sleep(2)
            print("(You receive a set of mysterious armour - it shines with power!) ")
            time.sleep(2)
            armour = "fire"
            

        elif wachoice == "e":
            print("Imbecile! Remove yourself at once from my esteemed shop before I have you murdered!")
            time.sleep(2)
            exit()
        else:
            print("Something went wrong try again!")
            time.sleep(2)
            mainshop()


mainshop()



