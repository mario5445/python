zoznam_cisel = [1,5,8,9,15,4,6,]
zoznam_pismen = ["a", "t", "g"]
zoznam_mix = ["slovo", 20, "cc"]
zoznam_cisel[0] = 9999
zoznam_cisel.sort()
print(zoznam_cisel)

zoznam = list
print(zoznam)

zoznam_range = list(range(3,7))

#orezavanie zoznamu
neorezany_zoznma = list(range(10))
print(neorezany_zoznma)
print("-------")
print(neorezany_zoznma[0:5])
print(neorezany_zoznma[1:4])
print(neorezany_zoznma[7:9])
print(neorezany_zoznma[3:5])
print(neorezany_zoznma[2:9:3])


#velkost zoznamu
x = [5, 8, 1, 3, "slovo"]
print(len(x))

#prechadzanie zoznamu
#1
zoznam_prvkov = ["jablko", "ahoj", "pd"]
for prvok in zoznam_prvkov:
    print(prvok)

#2
for index in range(len(zoznam_prvkov)):
    print(zoznam_prvkov[index])

#metody pre zoznamy
#append
my_list = [1,2,3,4,6,5,99,55]
my_list.append(40)
print(my_list)

#pop
my_list.pop()
print(my_list)

#funkcie pre zoznamy
#len
#min/max
my_list2 = [1,56,4,5,6,5,78]
print(min(my_list2))
print(max(my_list2))