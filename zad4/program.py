import time
start = time.time()
N = 50

# Dana macierz jest macierzą U
# macierz L jest jednostkowa więc we wszystkich obliczeniach pomijam L, bo LU=U
# natomiast macierz U nie ma iteracyjnych wartości, więc nie ma potrzeby trzymania jej w pamięci

# wektor B składa się z samych 5, więc nie ma potrzeby trzymać go w pamięci
# A * vectorZ = vectorB
vectorZ = [None] * N
for i in reversed(range(0, N)):
    prev = 0
    if i < N-1:
        # A(i,i+1) == 7
        prev += 7 * vectorZ[i+1]
    # A(i,i) == 9, vectorB[i] == 5
    vectorZ[i] = (5 - prev) / 9

# wektor U składa się z samych 1, więc nie ma potrzeby trzymać go w pamięci
# A * vectorZprim = vectorU
vectorZprim = [None] * N
for i in reversed(range(0, N)):
    prev = 0
    if i < N-1:
        # A(i,i+1) == 7
        prev += 7 * vectorZprim[i+1]
    # A(i,i) == 9, vectorU[i] == 1
    vectorZprim[i] = (1 - prev) / 9

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
print(f"time: {time.time() - start}")
