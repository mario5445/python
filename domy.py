domy = []
maximal = 0
pocet_maximal = 0
prazdne = 0
pra = 0
while True:
    zadaj = input("Zadaj počet obvateľov v dome:")
    domy.append(zadaj)
    if zadaj == "":
        domy.pop()
        domy = [int(i) for i in domy]
        break
maximal = max(domy)

print("Počet obyvateľov je:", sum(domy))
print("Najviac", maximal , "žije v jednej domácnosti")
for maximal in domy:
    if maximal in domy:
        pocet_maximal +=1
print("Domov s najväčsím počtom  obyvateľov je:", pocet_maximal)
for pra in domy:
    if pra in domy:
        prazdne += 1
print("Prazdnych domov je:", prazdne)
