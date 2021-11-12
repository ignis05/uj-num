import numpy as np

N = 6

matrixA = []
# iterate from 1 so the i in equation is correct
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


print(np.matrix(matrixA))

# LU decomposition
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


print("\n====new====")
print(np.matrix(matrixA))


def getL(x, y):
    # L diagonal
    if x == y:
        return 1
    # L below diag 1
    if x == y+1:
        return matrixA[x][0]
    # rest
    return 0


def getU(x, y):
    # U diagonal
    if x == y:
        return matrixA[x][1]
    # U above diag 1
    if x+1 == y:
        return matrixA[x+1][2]
    # U above diag 2
    if x+2 == y:
        return matrixA[x+2][3]
    return 0


# todo: remove test:
lList = []
uList = []
for i in range(N):
    lList.append([])
    uList.append([])
    for j in range(N):
        lList[i].append(0)
        lList[i][j] = getL(i, j)
        uList[i].append(0)
        uList[i][j] = getU(i, j)
l = np.array(lList)
u = np.array(uList)

print("\nl:")
print(l)
print("\nu:")
print(u)

# Lt = x | forwards substitution
vectorT = []
for i in range(0, N):
    prev = 0
    for j in range(0, len(vectorT)):
        prev += getL(i, j) * vectorT[j]
    vectorT.append((i+1 - prev)/getL(i, i))

print(vectorT)

# Uy = t | backwards substitution
vectorY = [None] * N
for i in reversed(range(0, N)):
    prev = 0
    for j in reversed(range(i+1, N)):
        prev += getU(i, j) * vectorY[j]
    vectorY[i] = (vectorT[i] - prev)/getU(i, i)

print("\n=== result: ===")
print(vectorY)
