
import numpy as np
from matplotlib import pyplot as plt


def generateInterpolation(nodeList):
    "generates interpolation function from list of points"
    def interFunc(x):
        res = 0
        for i, [xi, yi] in enumerate(nodeList):
            upProd = 1
            loProd = 1
            for j, [xj, yj] in enumerate(nodeList):
                if i == j:
                    continue
                upProd *= x-xj
                loProd *= xi-xj
            res += yi * upProd/loProd
        return res
    return interFunc


def drawInterPolation(originalFunc, nodeGenFunc, n):
    inter = generateInterpolation([[nodeGenFunc(i, n), originalFunc(nodeGenFunc(i, n))] for i in range(n+1)])
    x = np.linspace(-1, 1, 100)
    plt.plot(x, inter(x), label=f'n={n}')
