domy = []
maximal = 0
pocet_maximal = 0
prazdne = 0

while True:
    zadaj = input("Zadaj počet obvateľov v dome:")
    domy.append(zadaj)
    if zadaj == "":
        domy.pop()
        domy = [int(i) for i in domy]
        break
maximal = max(domy)

for pra in domy:
    pra = 0
    if pra in domy:
        prazdne += 1
print("Počet obyvateľov je:", sum(domy))
print("Najviac", maximal , "žije v jednej domácnosti")
for i in domy:
    i = max(domy)
    if i in domy:
        pocet_maximal +=1
print("Domov s najväčsím počtom  obyvateľov je:", pocet_maximal)

print("Prazdnych domov je:", prazdne)
