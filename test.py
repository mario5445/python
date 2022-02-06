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
    return hracia_plocha, move_counter, game