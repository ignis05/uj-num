import numpy as np
from matplotlib import pyplot as plt


def f1(x):
    return 1/(1+(25*(x**2)))


def f2(x):
    return 1/(1+(x**2))


def nodeGen1(i, n):
    return -1 + 2*(i/n)


def nodeGen2(i, n):
    return np.cos(((2*i+1)/(2*(n+1)))*np.pi)


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


x = np.linspace(-1, 1, 1000)
nList = [4, 6, 8, 10]
l = len(nList)+5
# orig:
plt.plot(x, f1(x), label='$f(x)$', zorder=l+1, linewidth=2)
# interpolations
for k, n in enumerate(nList):
    inter = generateInterpolation([[nodeGen1(i, n), f1(nodeGen1(i, n))] for i in range(n+1)])
    x = np.linspace(-1, 1, 100)
    plt.plot(x, inter(x), label='$W_{'+str(n)+'}(x)$', zorder=l-k)

plt.title(r'Wielomiany interpolacyjne funkcji $f(x)=\frac{1}{1+25x^{2}}$ w zależności od stopnia n')
plt.legend()
plt.show()
