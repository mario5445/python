domy = []
maximal = 0
pocet_maximal = 0
prazdne = 0
while True:
    zadaj = int(input("Zadaj počet obvateľov v dome:"))
    domy.append(zadaj)
    if zadaj == "":
        domy.pop()
        break
maximal = max(domy)

print("Počet obyvateľov je:", sum(domy))
print("Najviac", maximal , "žije v jednej domácnosti")
for pocet_maximal in domy:
    if pocet_maximal == maximal:
        pocet_maximal += 1
print("Domov s najväčsím počtom  obyvateľov je:", pocet_maximal)
for prazdne in domy:
    if prazdne == 0:
        prazdne += 1
print("Prazdnych domov je:", prazdne)
