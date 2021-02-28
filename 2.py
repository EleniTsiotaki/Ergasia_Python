import random

def fibo(x):
    i = 1
    j = 1
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        for k in range(x - 2):
            tmp = i
            i += j
            j = tmp
    return i

n = int(input("Poion oro ths akolouthias fibonacci thes deis an einai prwtos?"))
arithmos = fibo(n)
pl = 0
for i in range(20):  #Dialegw 20 fores enan tyxaio arithmo (oti oria thelw)
    if arithmos == 1 or arithmos == 0:
        break
    tyxaios = random.randrange(1, arithmos)
    if ((tyxaios ** arithmos) % arithmos) == (tyxaios % arithmos):
        pl += 1
    else:
        break
if pl == 20 or arithmos == 1:
    print("O", n,"os oros ths akoloythias einai o", arithmos, "kai einai prwtos")
elif pl != 20 and arithmos != 1 and arithmos != 0 :
    print("O", n,"os oros ths akoloythias einai o", arithmos, "kai den einai prwtos")
elif arithmos == 0:
    print("O arithmos einai to 0")


