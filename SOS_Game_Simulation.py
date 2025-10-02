import random
import math

diastaseis = True # Elegxw oti panta exw orthogwnio
while diastaseis == True:
    rows = int(input("Mikos?"))
    cols = int(input("Platos?"))
    if rows == cols:
        print("Theloume orthogwnio pinaka kai oxi tetragwno! Ksanaprospathise!")
    else:
        diastaseis = False
ori = 0
ka = 0
dia = 0
for z in range(100):
    arr = []
    pinakas_sos = []
    misa = math.ceil(rows * cols / 2)  # strogkilopoihsh pros ta panw

    for i in range(misa):
        pinakas_sos.append("s")
        pinakas_sos.append("o")
    o = 0
    s = 0
    while o == s:
        for i in range(cols):
            col = []
            for j in range(rows):
                stoixeio = random.choice(pinakas_sos)  # pairnw tyxaia "s" h "o"
                col.append(stoixeio)
                if stoixeio == "o":
                    o += 1
                elif stoixeio == "s":
                    s += 1
            arr.append(col)
            #print(arr[i])
    #print(misa)
    #print(arr)

    oriz = 0
    kath = 0
    diag = 0
    for i in range(cols):
        for j in range(rows):
            if j < rows-2:
                if arr[i][j] == "s":
                    if arr[i][j + 1] == "o":
                        if arr[i][j + 2] == "s":
                            oriz += 1  # Orizontia sos
                            ori += 1

            if i < cols - 2:
                if arr[i][j] == "s":
                    if arr[i + 1][j] == "o":
                        if arr[i + 2][j] == "s":
                            kath += 1  # Katheta sos
                            ka += 1

            if cols >= 2 and rows >= 2:
                if (i < cols - 2) and (j < rows - 2):
                    if arr[i][j] == "s":
                        if arr[i + 1][j + 1] == "o":
                            if arr[i + 2][j + 2] == "s":
                                diag += 1  # diagwnia sos
                                dia += 1

            if cols >= 2 and rows >= 2:
                if(j > 1) and (i < cols - 2):
                    if arr[i][j] == "s":
                        if arr[i + 1][j - 1] == "o":
                            if arr[i + 2][j - 2] == "s":
                                diag += 1  # diagwnia sos
                                dia += 1
    #print("thn", z, "fora to athroisma twn sos einai", oriz + kath + diag)

pl_sos = ori + ka + dia  # synolika sos
#print("To synoliko plithos twn sos einai:", pl_sos)
mo = pl_sos / 100
print("O mesos oros olwn twn sos einai:", mo)
