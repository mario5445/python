slovo = input("Zadaj slovo:")
samohlasky = "a", "e", "i", "o", "u", "y"
spoluhlasky = "r", "t", "z", "p", "s", "d", "f", "g", "h", "j", "k", "l", "c", "v", "b", "n", "m", "q", "w", "x"
cisla = "9", "8", "7", "6", "5", "4", "3", "2", "1", "0",
pocitadlo_samohlasky = 0
pocitadlo_spoluhlasky = 0
pocitadlo_cisla = 0    
pocitadlo_ostatne = 0
for znak in slovo:
    if znak in spoluhlasky:
        pocitadlo_spoluhlasky += 1
    elif znak in samohlasky:
        pocitadlo_samohlasky += 1
    elif znak in cisla:
        pocitadlo_cisla += 1
    else:
        pocitadlo_ostatne += 1   
       
        
print("Pocet samohlasok:", pocitadlo_samohlasky)
print("Pocet spoluhlasok:", pocitadlo_spoluhlasky)
print("Pocet cisel:", pocitadlo_cisla)
print("Pocet ostatnych:", pocitadlo_ostatne)