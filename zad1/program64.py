import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.cos(x)


def fPrim(x):
    return - np.sin(x)


pointX = np.float64(0.3)


def przybA(x, h):
    return (f(x + h) - f(x)) / h


def przybB(x, h):
    return (f(x + h) - f(x - h)) / (h*np.float64(2))


def epsilon(x, h, func):
    return np.abs(func(x, h)-fPrim(x))


deriv = fPrim(pointX)
print("derivative: ", str(deriv), )

xAxis = []
resA = []
resB = []

limit = np.float64(1) / np.power(np.float64(10), np.float64(16))
hVal = np.float64(1) / np.float64(10)

while hVal > limit:
    aproxA = przybA(pointX, hVal)
    epsiA = epsilon(pointX, hVal, przybA)
    aproxB = przybB(pointX, hVal)
    epsiB = epsilon(pointX, hVal, przybB)
    print("h=", str(hVal), "|     aproxA: ", str(aproxA), "|     epsiA: ", str(epsiA), "|    aproxB: ", str(aproxB), "|     epsiB: ", str(epsiB))
    xAxis.append(np.log10(hVal))
    resA.append(np.log10(epsiA))
    resB.append(np.log10(epsiB))

    hVal = hVal / np.float64(1.5)

plt.plot(xAxis, resA, label='epsilon A', color='C0')
plt.plot(xAxis, resB, label='epsilon B', color='C1')
plt.xlabel('h')
plt.ylabel('Approximation error')
plt.title('Aproximation error based on h value (64 bit)')
plt.legend()
plt.show()
