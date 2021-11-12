import numpy as np
from scipy.linalg import lu

N = 6

listA = []
for i in range(1, N+1):
    element = []
    listA.append(element)
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

listX = [i for i in range(1, N+1)]

matrixA = np.array(listA)

vectorX = np.array(listX).T

vectorY = np.linalg.solve(matrixA, vectorX)

p, l, u = lu(matrixA)

print("p:\n")
print(p)
print("l:\n")
print(l)
print("u:\n")
print(u)

print(vectorY)