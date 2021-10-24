import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.cos(x)


def fPrim(x):
    return - np.sin(x)


pointX = np.float32(0.3)


def przybA(x, h):
    return (f(x + h) - f(x)) / h


def przybB(x, h):
    return (f(x + h) - f(x - h)) / (h*np.float32(2))


def epsilon(x, h, func):
    return np.abs(func(x, h)-fPrim(x))


deriv = fPrim(pointX)
print("derivative: ", str(deriv), )

minA = {'val': 1, 'h': 1}
minB = {'val': 1, 'h': 1}

xAxis = []
resA = []
resB = []

limit = np.float32(1) / np.power(np.float32(10), np.float32(7))
hVal = np.float32(1) / np.float32(10)

while hVal > limit:
    aproxA = przybA(pointX, hVal)
    epsiA = epsilon(pointX, hVal, przybA)
    aproxB = przybB(pointX, hVal)
    epsiB = epsilon(pointX, hVal, przybB)
    print("h=", str(hVal), "|     aproxA: ", str(aproxA), "|     epsiA: ", str(epsiA), "|    aproxB: ", str(aproxB), "|     epsiB: ", str(epsiB))
    xAxis.append(np.log10(hVal))
    resA.append(np.log10(epsiA))
    resB.append(np.log10(epsiB))

    if epsiA < minA['val']:
        minA['val'] = epsiA
        minA['h'] = hVal
    if epsiB < minB['val']:
        minB['val'] = epsiB
        minB['h'] = hVal

    hVal = hVal / np.float32(1.1)

print('Smallest error for A:\nh*={0}\terr={1}'.format(minA['h'], minA['val']))
print('Smallest error for B:\nh*={0}\terr={1}'.format(minB['h'], minB['val']))

plt.plot(xAxis, resA, label='epsilon A', color='C0')
plt.plot(xAxis, resB, label='epsilon B', color='C1')
plt.xlabel('h')
plt.ylabel('Approximation error')
plt.title('Aproximation error based on h value (32 bit)')
plt.legend()
plt.show()
