from numpy import array

# rozmiar macierzy i wektora
N = 100


# zapisanie wejściowej macierzy A jako tablica[N][4]
matrixA = []
for i in range(1, N+1):
    row = [[], [], [], []]
    matrixA.append(row)

    # 1 - diag:
    row[1] = 1.2
    if i > 1:
        # 0 - below diag 1:
        row[0] = 0.2
        # 2 - above diag 1

        row[2] = 0.1 / (i-1)
    else:
        row[0] = 0
        row[2] = 0
    if i > 2:
        # 3 - above diag 2
        row[3] = 0.4 / pow(i-2, 2)
    else:
        row[3] = 0


# rozkład LU "in-place"
for i in range(N):
    # above diag 2
    if i > 1:
        # matrixA[i][3] = matrixA[i][3]
        pass
    else:
        matrixA[i][3] = 0

    # above diag 1
    if i > 0:
        matrixA[i][2] = matrixA[i][2] - matrixA[i-1][0] * matrixA[i][3]
    elif i > 0:
        # matrixA[i][2] = matrixA[i][2]
        pass
    else:
        matrixA[i][2] = 0

    # below diag 1
    if i > 0:
        matrixA[i][0] = matrixA[i][0]/matrixA[i-1][1]
    else:
        matrixA[i][0] = 0

    # diag
    if i > 0:
        matrixA[i][1] = matrixA[i][1] - matrixA[i][0] * matrixA[i][2]
    else:
        # matrixA[i][1] = matrixA[i][1]
        pass

# obliczenie Lt = x | forward substitution
# zamiast zapisywania całego wektora x w pamięci, są brane jego wartości jako vectorX[i] = i+1
vectorT = []
for i in range(0, N):
    prev = 0
    if i > 0:
        prev += matrixA[i][0] * vectorT[i-1]
    vectorT.append((i+1 - prev))

# print(array(vectorT))

# obliczenie Uy = t | backward substitution
vectorY = [None] * N
for i in reversed(range(0, N)):
    prev = 0
    if i < N-1:
        prev += matrixA[i+1][2] * vectorY[i+1]
    if i < N-2:
        prev += matrixA[i+2][3] * vectorY[i+2]
    vectorY[i] = (vectorT[i] - prev)/matrixA[i][1]

# wykorzystywane tylko do wyświetlania wyników - numpy.array wyświetla się znacznie ładniej niż zwykła lista
print("wektor y:")
print(array(vectorY))

# det(A) = det(L) * det(U) = 1 * det(U) = iloczyn i->N: U[i][i]
det = 1
for i in range(N):
    det *= matrixA[i][1]

print("\nwyznacznik A:")
print(det)
