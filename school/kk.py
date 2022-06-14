import random
list1 = []
list2 = []
list3 = []

while True:
    nick = input("Zadaj svoj nick, a ak chceš skončiť napíš 'stop' : ")
    if nick == "stop":
        print("TÍMY SÚ HOTOVÉ")
        print("V tíme 1 sú títo súťažiaci:\n", list1)
        print("V tíme 2 sú títo súťažiaci:\n", list2)
        print("V tíme 3 sú títo súťažiaci:\n", list3)
        print("\n LET'S PLAY!!!")
        break
    cislo = random.randint(0, 2)
    if cislo == 0:
        list1.append(nick)
    elif cislo == 1:
        list2.append(nick)
    else:
        list3.append(nick)
