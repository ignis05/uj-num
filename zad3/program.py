import numpy as np

N = 100

matrixA = []
for i in range(1, N+1):
    element = []
    matrixA.append(element)
    for j in range(1, N+1):
        val = 0
        if i == j:
            val = 1.2
        elif i == j+1:
            val = 0.2
        elif i+1 == j:
            val = 0.1 / i
        elif i+2 == j:
            val = 0.4 / (i**2)
        element.append(val)

vectorX = [i for i in range(1, N+1)]

# print(matrixA)
# print(vectorX)

# LU decomposition
for i in range(N):
    # prevent index oob, if i==0:
    # matrixA[i][i] = matrixA[i][i]
    # matrixA[i][i+1] = matrixA[i][i+1]
    # so just skip them
    if i > 0:
        matrixA[i][i] = matrixA[i][i] - (matrixA[i][i-1] * matrixA[i-1][i])
        if(i+1 < N):
            matrixA[i][i+1] = matrixA[i][i+1] - (matrixA[i][i-1] * matrixA[i-1][i+1])
    # also skips this
    # matrixA[i][i+2] = matrixA[i][i+2]
    if(i+1 < N):
        matrixA[i+1][i] = matrixA[i][i+1] / matrixA[i][i]


# print("====new====\n")
# print(matrixA)


def getL(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    return matrixA[x][y]


def getU(x, y):
    if x > y:
        return 0
    return matrixA[x][y]


# todo: remove test:
print(len(matrixA))
print(len(matrixA[0]))
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

print("l:\n")
print(l)
print("u:\n")
print(u)
exit(0)
# Lt = x
vectorT = []
for i in range(0, N):
    prev = 0
    for j in range(0, len(vectorT)):
        prev += getL(i, j) * vectorT[j]
    vectorT.append((vectorX[i] - prev))

print(vectorT)

# Uy = t
vectorY = []
for i in range(0, N):
    prev = 0
    for j in range(0, len(vectorY)):
        print(f"{i}, {j}")
        prev += getL(N-1-i, len(vectorY)-1-j) * vectorY[len(vectorY)-1-j]
    vectorY.append((vectorT[N-1-i] - prev))

print("result: ===\n")
vectorY.reverse()
print(vectorY)
