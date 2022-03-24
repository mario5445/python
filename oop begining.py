import random

class Cat:
    #konštruktor
    def __init__(self, name, vek):
        print("Vytvaram objekt mačky")
        self.name = name
        self.vek = vek
    def __str__(self):
        print("Meno mačky je: " + self.name)
        print("Vek mačky je: " + str(self.vek))
        return " "
    def zamnaukaj(self):
        print(self.name + " Mňau")
    def zjedz(self, jedlo):
        print(self.name + " zjedol " + jedlo)

class Auto:
    def __init__(self, znacka, farba, rok_vyroby, pocet_sedadiel, jeNastartovane):
        self.znacka = znacka
        self.farba = farba
        self.rok_vyroby = rok_vyroby
        self.pocet_sedadiel = pocet_sedadiel
        self.jenastartovane = jeNastartovane
    def __str__(self):
        print("Značka auta: " + self.znacka)
        print("Farba je: " + self.farba)
        print("Rok výroby: " + str(self.rok_vyroby))
        print("Počet sedadiel: " + str(self.pocet_sedadiel))
        return " "
    def chod_dopredu(self):
        print("Idem dopredu")
    def zatrub(self):
        print("tuuuuuuuuut")
    def nastartovane(self):
        if self.jenastartovane == True:
            print("Auto je naštartované")
        elif self.jenastartovane == False:
            print("Auto nie je naštartované")
        else:
            print("Incorrect status")




#vytvorenie inštanciew objektu mačka
cat = Cat("Mica", 4)
#cat.meno = "Muro"
#cat.zjedz("ryba")
#volanie metody
#cat.zamnaukaj()
#auto = Auto("Audi", "čierna", 2017, 5, True)
#print(auto)
#auto.chod_dopredu()
#auto.zatrub()
#auto.nastartovane()
#print(cat)
"""
while True:
    try:
        number_1 = float(input("Zadaj 1. číslo: "))
        number_2 = float(input("Zadaj 2. číslo: "))
        break
    except Exception:
        print("Zadal si string. Zadaj prosím int alebo float")
        continue

class Kalkulacka:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def plus(self):
        print("Súčet: ", self.first_number + self.second_number)

    def minus(self):
        print("Rozdiel: ", self.first_number - self.second_number)
    def krat(self):
        print("Súčin: ", self.first_number * self.second_number)
    def deleno(self):
        try:
            print("Podiel: ", self.first_number / self.second_number)
        except ZeroDivisionError:
            print("Nulou sa deliť nedá!")

#kalkulacka = Kalkulacka(number_1, number_2)
#kalkulacka.plus()
#kalkulacka.minus()
#kalkulacka.krat()
#kalkulacka.deleno()
"""
while True:
    try:
        pocet_stran_1 = int(input("Zadaj počet strán kocky: "))
        pocet_stran_2 =  int(input("Zadaj počet strán kocky: "))
        break
    except Exception:
        print("Zadal si float alebo string. Zadaj int prosím ")
        continue
class Kocka:
    def __init__(self, strany):
        self.strany = strany
    def hod(self):
        print("Hod:")
        for i in range(10):
            print(random.choice(range(1, self.strany)), end=",")
        print()

kocka_1 = Kocka(pocet_stran_1)
kocka_2 = Kocka(pocet_stran_2)
kocka_1.hod()
kocka_2.hod()