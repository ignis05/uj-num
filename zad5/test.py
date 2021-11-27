import numpy as np

N = 100

listA = []
for i in range(1, N+1):
    element = []
    listA.append(element)
    for j in range(1, N+1):
        val = 0
        if i == j:
            val = 3
        elif abs(i-j) == 1:
            val = 1
        elif abs(i-j) == 2:
            val = 0.2
        element.append(val)

matrixA = np.array(listA)

vectorB = np.array([i for i in range(1, N+1)]).T

print("wektor x:")
print(np.linalg.solve(matrixA, vectorB))
