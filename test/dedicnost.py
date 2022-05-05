class Animal:
    def __init__(self, meno):
        self.meno = meno
    def jedz(self, jedlo):
        print(f"{self.meno}: {jedlo} mi chutí!")


class Macka(Animal):
    def urob_zvuk(self):
        print(f"{self.meno}: Mňau!")

    def zamnaukaj(self):
        print(f"{self.meno}: Mnau!")
    def jedz(self, jedlo):
        super().jedz("Ryba")
        print(f"{self.meno}: {jedlo} mi nechutí!")

class Pes(Animal):
    def urob_zvuk(self):
        print(f"{self.meno}: Haf!")

    def zastekaj(self):
        print(f"{self.meno}: Haf!")

macka = Macka("Muro")
pes = Pes("Dunčo")

"Môžem používať jedz, ktoré som definoval v triede Animal"
macka.jedz("Ryba")
macka.urob_zvuk()

"Môžem používať jedz, ktoré som definoval v triede Animal"
pes.jedz("Mäso")
pes.urob_zvuk()


#Polymorfizmus
zvieratka = [Macka("Micka"), Pes("Azor")]

for zvieratko in zvieratka:
    zvieratko.jedz("Granule")
    zvieratko.urob_zvuk()
#Generalizacia

class A(Pes,Macka):
    pass
a = A("a")
a.zamnaukaj()
a.zastekaj()
