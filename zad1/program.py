import numpy as np
import matplotlib.pyplot as plt

# np.float32 or np.float64
precision = np.float64
# 7 or 16
hRange = 16
# 'a' or 'b'
equation = 'a'


def f(x):
    return np.cos(x)


def fPrim(x):
    return - np.sin(x)


pointX = precision(0.3)


def przybA(x, h):
    return (f(x + h) - f(x)) / h


def przybB(x, h):
    return (f(x + h) - f(x - h)) / (h*precision(2))


def epsilon(x, h, func):
    return np.abs(func(x, h)-fPrim(x))


deriv = fPrim(pointX)
print("derivative: ", str(deriv), )

xAxis = []
yAxis = []

limit = precision(1) / np.power(precision(10), precision(hRange))
hVal = precision(1) / precision(10)

while hVal > limit:
    aproxA = przybA(pointX, hVal)
    epsiA = epsilon(pointX, hVal, przybA)
    aproxB = przybB(pointX, hVal)
    epsiB = epsilon(pointX, hVal, przybB)
    print("h=", str(hVal), "|     aproxA: ", str(aproxA), "|     epsiA: ", str(epsiA), "|    aproxB: ", str(aproxB), "|     epsiB: ", str(epsiB))
    xAxis.append(np.log10(hVal))
    if equation == 'a':
        yAxis.append(np.log10(epsiA))
    else:
        yAxis.append(np.log10(epsiB))

    hVal = hVal / precision(2)

plt.plot(xAxis, yAxis)
plt.show()
