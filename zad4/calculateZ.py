import numpy as np

N = 50

listA = []
for i in range(1, N+1):
    element = []
    listA.append(element)
    for j in range(1, N+1):
        val = 0
        if i == j:
            val = 9
        elif i+1 == j:
            val = 7
        element.append(val)

matrixA = np.array(listA)

vectorB = np.array([5 for _ in range(1, N+1)]).T

vectorU = np.array([1 for _ in range(1, N+1)]).T


print("wektor z:")
print(np.linalg.solve(matrixA, vectorB))
print("\nwektor zPrim:")
print(np.linalg.solve(matrixA, vectorU))
