zoznam = []
while(True):
    zadaj = input("Zadaj jedno číslo:")
    zoznam.append(zadaj)
    if zadaj == "":
        zoznam.sort()
        dlzka = len(zoznam)
        if dlzka%2 == 0:
            vypocet_1 = round(dlzka/2) - 1
            print("Medián zoznamu je:", zoznam[vypocet_1])
        else:
            vypocet_2 = round(dlzka/2)
            print("Medián zoznamu je:", zoznam[vypocet_2])

