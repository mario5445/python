slovo = input("Zadaj slovo:")
samohlasky = "aáäiíoóeéôuúyý"
spoluhlasky = "qwrtzpsdfghjklxcvbnmľďščťžňĺŕ"
cisla = "0123456789"
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