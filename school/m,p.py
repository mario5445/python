import random

privlastky = ["maly", "pekny", "škaredy", "velky", "zaujimavy", "nudny", "vtipny", "tucny", "chudy", "zlaty"]

zoznamMien = []

while True:
    meno = input("Zadaj meno: ")
    if meno == "koniec":
        break
    priezvisko = input("Zadaj priezvisko: ")
    mix = meno + " " + privlastky[ random.randint(0, 9) ] + " " + priezvisko
    zoznamMien.append(mix)



    for i in range(0, len(zoznamMien)):
        print(str(i+1) + ".\t" + zoznamMien[i])
