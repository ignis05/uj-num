import numpy as np

N = 100

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


# from scipy.linalg import lu
# p, l, u = lu(matrixA)
# print("\np:")
# print(p)
# print("\nl:")
# print(l)
# print("\nu:")
# print(u)

# vectorT = np.linalg.solve(l, vectorX)
# print("\nvector T:")
# print(vectorT)


print("wektor y:")
print(np.linalg.solve(matrixA, vectorX))
print("\nwyznacznik A")
print(np.linalg.det(matrixA))
