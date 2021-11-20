N = 50

# Dana macierz jest macierzą U
# macierz L jest jednostkowa więc we wszystkich obliczeniach pomijam L, bo LU=U
# natomiast macierz U nie ma iteracyjnych wartości, więc nie ma potrzeby trzymania jej w pamięci - wszystkie wartości można bez problemy zwrócić z funkcji


def getU(x, y):
    "funkcja pomocnicza zwracająca odpowiednią wartość macierzy U"
    # U diagonal
    if x == y:
        return 9
    # U above diag 1
    if x+1 == y:
        return 7
    return 0


# wektor B składa się z samych 5, więc nie ma potrzeby trzymać go w pamięci
# A * vectorZ = vectorB
vectorZ = [None] * N
for i in reversed(range(0, N)):
    prev = 0
    for j in reversed(range(i+1, N)):
        prev += getU(i, j) * vectorZ[j]
    vectorZ[i] = (5 - prev)/getU(i, i)

# wektor U składa się z samych 1, więc nie ma potrzeby trzymać go w pamięci
# A * vectorZprim = vectorU
vectorZprim = [None] * N
for i in reversed(range(0, N)):
    prev = 0
    for j in reversed(range(i+1, N)):
        prev += getU(i, j) * vectorZprim[j]
    vectorZprim[i] = (1 - prev)/getU(i, i)

# vectorY = vectorZ - top/bot

# 1 + vectorV.T * vectorZprim, gdzie vectorV.T = 1.T, czyli:
bot = 1 + sum(vectorZprim)
# topNr =  vectorV.T * vectorZ, gdzie vectorV.T = 1.T, czyli:
topNr = sum(vectorZ)
# top = vectorZprim * topNr
top = [val*topNr for val in vectorZprim]
# topSBot = top / bot
topSBot = [val/bot for val in top]

# vectorY = vectorZ - topSBot
vectorY = [val - topSBot[i] for i, val in enumerate(vectorZ)]
print(vectorY)
