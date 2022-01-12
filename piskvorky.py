hrac1 = "x"
hrac2 = "O"
ok = None
vyherca = None
game = True
hracia_plocha = [
    ["█", 1, 2, 3],
    [1, " ", " ", " "],
    [2, " ", " ", " "],
    [3, " ", " ", " "],

]
empty_places = 9
move_counter = 0
#hracia plocha zobrazenie
def usporiadanie(hracia_plocha):
    for riadok in hracia_plocha:
        for policko in riadok:
            print(policko, end="")
        print()
    return hracia_plocha

#kontrola
def check(hracia_plocha, move_counter, game):
    while game:
        inp1 = int(input("Hráč 1: Zadaj pozičný argument1:"))
        inp2 = int(input("Hráč 1: Zadaj pozičny argument 2:"))
        if hracia_plocha[inp1][inp2] == " " and inp1 != 0 and inp2 != 0 and inp1 <= 3 and inp2 <= 3:
            move_counter += 1
            znak = hracia_plocha[inp1][inp2] = "x"
            break
        else:
            usporiadanie(hracia_plocha)
            print("Zadal si zlé číslo alebo už obsadené políčko")
            continue
    usporiadanie(hracia_plocha)
    while game:
        inp3 = int(input("Hráč 2: Zadaj pozičny argument 1:"))
        inp4 = int(input("Hráč 2: Zadaj pozičny argument 2:"))
        if hracia_plocha[inp3][inp4] == " " and inp3 != 0 and inp4 != 0 and inp3 <= 3 and inp4 <= 3:
            znak2 = hracia_plocha[inp3][inp4] = "o"
            move_counter += 1
            break
        else:
            print("Zadal si zlé číslo alebo už obsadené políčko")
            continue
    return True
"""
def horizontalna_vyhra(hracia_plocha, vyherca, ok):
    if hracia_plocha[1][1] == hracia_plocha[1][2] == hracia_plocha[1][3] and hracia_plocha[1][1] != " ":
        vyherca = hracia_plocha[1][1]
        print("Koniec")
        ok = 2
    elif hracia_plocha[2][1] == hracia_plocha[2][2] == hracia_plocha[2][3] and hracia_plocha[2][1] != " ":
        vyherca = hracia_plocha[2][1]
        print("Koniec")
        ok = 2
    elif hracia_plocha[3][1] == hracia_plocha[3][2] == hracia_plocha[3][3] and hracia_plocha[3][1] != " ":
        vyherca = hracia_plocha[3][1]
        print("Koniec")
        ok = 2
    return hracia_plocha, vyherca, ok
"""
"""
def win_control(hracia_plocha, game):
    if vyherca == "x":
        print("Vyhrál hráč 1")
        game = False
        return game
    elif vyherca == "o":
        print("Vyhral hráč 2")
        game = False
        return game
    else:
        game = True
        return game
"""



"""
def vertikalna_vyhra(hracia_plocha):
    while True:
        if hracia_plocha[1][1] == hracia_plocha[2][1] == hracia_plocha[3][1] or hracia_plocha[1][2] == hracia_plocha[2][2] == hracia_plocha[3][2] or hracia_plocha[1][3] == hracia_plocha[2][3] == hracia_plocha[3][3]:
            if hracia_plocha[1][1] or hracia_plocha[1][2] or hracia_plocha[1][3] == "x":
                print("Vyhral hráč 1. Gratulujem!!!")
                break
            elif hracia_plocha[1][1] or hracia_plocha[1][2] or hracia_plocha[1][3] == "o":
                print("Vyhral hráč 2. Gratulujem!!!")
                usporiadanie(hracia_plocha)
                break

def diagonalna_vyhra(hracia_plocha):
    while True:
        if hracia_plocha[1][1] == hracia_plocha[2][2] == hracia_plocha[3][3] or hracia_plocha[1][3] == hracia_plocha[2][2] == hracia_plocha[3][1]:
            if hracia_plocha[1][1] or hracia_plocha[1][3] == "x":
                print("Vyhral hráč 1. Gratulujem!!!")
                usporiadanie(hracia_plocha)
                break
            elif hracia_plocha[1][1] or hracia_plocha[1][3] == "o":
                print("Vyhral hráč 2. Gratulujem!!!")
                usporiadanie(hracia_plocha)
                break



def remiza(hracia_plocha, game, move_counter, empty_places):
    if move_counter == empty_places:
        print("Remiza chlapi")
        game = False
    return game, move_counter
"""



#priebeh hry
while True:
    usporiadanie(hracia_plocha)
    check(hracia_plocha, move_counter, game)
    #horizontalna_vyhra(hracia_plocha, game, vyherca)
    #print(vyherca)
    #win_control(hracia_plocha, game)
    #vertikalna_vyhra(hracia_plocha)
    #diagonalna_vyhra(hracia_plocha)
#   remiza(hracia_plocha, game, move_counter, empty_places)
    print(move_counter)


