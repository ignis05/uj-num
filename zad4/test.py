from scipy.linalg import lu
import numpy as np

N = 50

listA = []
for i in range(1, N+1):
    element = []
    listA.append(element)
    for j in range(1, N+1):
        val = 1
        if i == j:
            val = 10
        elif i+1 == j:
            val = 8
        element.append(val)

matrixA = np.array(listA)
vectorB = np.array([5 for _ in range(1, N+1)]).T

print(np.linalg.solve(matrixA, vectorB))
