subory = int(input("Zadaj kolko suborov chceš:"))

slova = []



e = 0
a = [e+1]
with open("./basnicka.txt", encoding="utf-8") as subor:
    for riadok in subor:
        slova += riadok.split()
basen = len(slova)
for i in range(subory):
    if i >= basen:
        e = i - basen
    open("%s.txt" % i, "w", encoding="utf-8").write(slova[e])

if subory > basen:
    rr = 1
    filename = "%s.txt" % rr
    new_file = open(filename, "w", encoding="utf-8")
    print(slova[e], file=new_file)
    new_file.close()

print(basen)


#for i in range(subory):
 #   if i >= m:
  #      e = i - basen
   # with open("./"+str(i)+".txt", mode="w", encoding="utf-8") as subor1:
    #    print(slova[e], file=subor1)
