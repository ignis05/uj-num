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

print(matrixA)
print(vectorX)
