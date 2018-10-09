import time

def quest1():
    print("This is your first quest.")
    time.sleep(2)
    print("You only have a knife which is definitely not going to kill dragons.")
    time.sleep(3)
    print("You also do not have enough money to buy better gear.")
    time.sleep(3)
    print("This is odd but...")
    time.sleep(3)
    print("You could actually rob the house of Gary")
    time.sleep(3)
    print("He used to make fun of you a lot when you were younger...")
    time.sleep(3)
    print("So, are you going to rob him or what?")
    time.sleep(3)
    quest1in = input("Y/N: ").lower()
    time.sleep(2)
    if quest1in == "y":
        print("Fine.")
        quest1part2()

    elif quest1in == "n":
        print("You do not have any money left.")
        time.sleep(2)
        print("You can not even buy food. Think about it... You have got nothing to lose.")
        time.sleep(3)
        print("So, do you wanna rob Garry or no?")
        time.sleep(2)
        quest1input2 = input("Y/N: ").lower
        if quest1input2 == "y":
            print("Nice. You made the right choice.")
            quest1quest1part2()

        else:
            print("You did not have any money and died to starvation.")
            time.sleep(2)
            exit()

    else:
        print("Something went wrong.")
        time.sleep(1)
        quest1()

def quest1part2():
    print("Okay, you are inside the house. You need to be quick.")
    time.sleep(2)
    print("Gary will arrive from time to time with his horses.")
    time.sleep(2)
    print("Okay, he hid the money in his baclon.")
    time.sleep(2)
    print("OH SHIT. There are horse noises being heard.. Gary has arrived.")
    time.sleep(2)
    print("He sees you.. He is attacking you...")
    time.sleep(2)
    print("You can either 1.Kill him or 2.Tell him that it is a misunderstanding")
    time.sleep(3)
    quest1input3 = input("1/2: ")
    if quest1input3 == "1":
        print("You put your knife in his brain.")
        time.sleep(2)
        print("There is blood in your hands.")
        time.sleep(2)
        print("You burried him inside a cave.")
        time.sleep(2)
        print("You have 1000$")
        time.sleep(2)
        print("You did the right thing.")
        time.sleep(2)
        exit()

    elif quest1input3 == "2":
        print("He did not believe you. He killed you.")
        time.sleep(2)
        exit()

    else:
        print("Something went wrong.")
        time.sleep(2)
        quest1part2()
