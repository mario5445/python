import random
"""
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
                                                                                                                
"""

"""                                                                                                             
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
"""
"""
class Person:
    def __init__(self, name, priezvisko):
        self.name = name
        self.priezvisko = priezvisko
        self.stamina = 0
    def kontrola(self):
        while True:
            print(self.name, self.priezvisko, "(", self.stamina, ")")
            vstup = input("Čo chceš robiť?")
            if vstup == "spať" or vstup == "Spať":
                Person.spanok(self)
            elif vstup == "behať" or vstup == "Behať":
                Person.beh(self)
            else:
                continue
    def beh(self):
        print(self.name, self.priezvisko, "(", self.stamina, ")")
        while True:
            try:
                vzdialenost = float(input("Koľko mám behať?"))
                break
            except Exception:
                print("Zadal si string")
                continue
        if self.stamina >= vzdialenost:
            print(f"Zabehol som {vzdialenost} kilometrov")
            self.stamina -= vzdialenost
        else:
            print("Som príliš unavený, daj ma spať")
    def spanok(self):
        print(self.name, self.priezvisko, "(", self.stamina, ")")
        while True:
            try:
                sleep_time = float(input("Koľko mám spať?"))
                break
            except Exception:
                print("Zadal si string")
                continue
        if (self.stamina + sleep_time) <= 20:
            print("Spím")
            self.stamina += sleep_time*10
        else:
            print("Nie som unavený.")

person = Person("Andrej", "Novotný")
person.kontrola()
"""
"""
class Word:
    def __init__(self):
        self.pridavne_mena =   ["veľký", "malý", "tučný", "chudý", "pomalý", "rýchly", "pekný", "škaredý"]
        self.podstatn_mena = ["programátor", "murár", "stavbár", "kuchár"]
        self.podstatne_mena_a_predlozky = ["u babky", "u mamy", "pod stromom", "za domom", "v lese", "v kríkoch"]
        self.prislovky = ["teraz", "zajtra", "veľa", "málo", "s obľubou", "rýchlo", "dlho"]
        self.slovesa =  ["spal", "chodil", "varil", "miešal", "šoféroval", "plakal", "hovoril", "učil"]
    def generovanie_slovesa(self):
        random_sloveso = random.choice(self.slovesa)
        return random_sloveso
    def generovanie_podst_mena(self):
        random_podst = random.choice(self.podstatne_mena_a_predlozky)
        return random_podst
    def generovanie_pridavneho_mena(self):
        random_prid = random.choice(self.pridavne_mena)
        return random_prid
    def generovanie_prislovky(self):
        random_prislovka = random.choice(self.prislovky)
        return random_prislovka
    def generovanie_podst(self):
        random_pod = random.choice(self.podstatn_mena)
        return random_pod
    def generuj_vetu(self):
        print(self.generovanie_pridavneho_mena(), self.generovanie_podst(), self.generovanie_prislovky(),self.generovanie_slovesa(), self.generovanie_podst_mena())


word = Word()
for i in range(11):
    word.generuj_vetu()
"""
"""
class Garage:
    def __init__(self):
        pass

    def vypis(self, target):
        temp = []
        temp.append(target)
        print("V garáži sú autá:", temp)



class Car:

    def __init__(self, spz, color):
        self.spz = spz
        self.color = color
    def zaparkuj(self, Garage):

        Garage.vypis(target=self.spz)



car = Car("CA550XD", "blue")
garage = Garage()
car.zaparkuj(garage)
car2 = Car("KM550XD", "red")
car2.zaparkuj(garage)
"""
class Garaz():

    auta_v_garazi = []
    def vypis_auta(self):
        if self.auta_v_garazi == []:
            print("Garáž je prázdna")
        else:
            print("V garáži sú autá: {}".format(", ".join(self.auta_v_garazi)))

class Auto():
    def __init__(self, SPZ, farba):
        self.spz = SPZ
        self.farba = farba

    def zaparkuj(self, garage):
        garage.auta_v_garazi.append("{0} {1}".format(self.spz, self.farba))
    def vyparkuj(self, garage):
        garage.auta_v_garazi.remove("{0} {1}".format(self.spz, self.farba))

garaz = Garaz()
bmw = Auto("CA550XD", "BLUE")
bmw.zaparkuj(garaz)
audi = Auto("KM550XD", "RED")
audi.zaparkuj(garaz)
garaz.vypis_auta()


