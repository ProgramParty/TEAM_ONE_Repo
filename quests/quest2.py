import time
from player import Player


def quest2():
    print("This is your second quest.")
    time.sleep(2)
    print("So let me explain things very quick.")
    time.sleep(3)
    print("Right now your village is suffering from extreme poverty.")
    time.sleep(4)
    print("Most citizens are starving every single day.")
    time.sleep(3)
    print("Dragons have stolen everything.")
    time.sleep(3)
    print("But no, it is not the dragons fault...")
    time.sleep(3)
    print("King Johnson is responsible for that..")
    time.sleep(3)
    print("Had he wanted, he could have slain all five dragons.")
    time.sleep(3)
    print("But as long as they do not touch his property, he does not give a fuck.")
    time.sleep(5)
    print("He has a field full of tasty fruit and vegetables.")
    time.sleep(2)
    print("While most citizens do not even have access to clean, drinkable water.")
    time.sleep(4)
    print("He has guards in front of the yard.")
    time.sleep(3)
    print("This could be extremely difficult.")
    time.sleep(2)
    print("So here is the plan. You will have to kill both of the guards...")
    print("Then go inside the field and steal as much food as humanly possible.")
    time.sleep(6)
    print("But there is a drawback.")
    time.sleep(3)
    print("You do not have a weapon right now and you can not kill two guards on your own.")
    time.sleep(5)
    print("You could of course tell Nicola to help you.")
    time.sleep(3)
    print("He is your best friend and he is really good at killing people.")
    time.sleep(2)
    qu2part2()


def qu2part2():
    print("Do you want him to help you?")
    quest2input = input("Y/N:").lower()
    time.sleep(2)
    if quest2input == "y":
        print("Nice. He will be proven helpful.")
        qu2part3()

    elif quest2input == "n":
        print("You can not fight alone...")
        qu2part2()

    else:
        print("Something went wrong.")
        qu2part2()


def qu2part3():
    time.sleep(2)
    print("Okay, Nicola has your back.")
    time.sleep(2)
    print("None of you actually has a gun, so this might be tricky.")
    time.sleep(3)
    print("Okay, you are approcahing the field.")
    time.sleep(2)
    print("You can clearly see both men, holding swords.")
    time.sleep(3)
    print("You have two options. Either punch one in the face, or kick his guts.")
    time.sleep(3)
    print("Nicola will take care of the other guy.")
    time.sleep(2)
    print("1:Punch/2:Kick.")
    quest2input2 = input("1/2: ")
    if quest2input2 == "1":
        print("Your punch was really weak and he put his sword up your throat.")
        time.sleep(3)
        print("You are dead.")
        time.sleep(2)
        exit()

    elif quest2input2 == "2":
        print("You both kicked the men in the guts and they are struggling to breath.")
        qu2part4()

    else:
        print("Something went wrong.")
        time.sleep(2)


def qu2part4():
    time.sleep(2)
    print("You take his sword and put it up in his stomach.")
    time.sleep(2)
    print("So did Nicola.")
    time.sleep(2)
    print("You take as much food as possible and run before anyone sees you.")
    time.sleep(4)
    print("You share the food with the other citizens.")
    time.sleep(3)
    print("You have gained their respect.")
    time.sleep(3)
    print("Here are your current stats: ")
    print(Player())
    time.sleep(5)
