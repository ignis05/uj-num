import numpy as np
from matplotlib import pyplot as plt
from shared import *


def f1(x):
    return 1/(1+(25*(x**2)))


def f2(x):
    return 1/(1+(x**2))


def nodeGen2(i, n):
    return np.cos(((2*i+1)/(2*(n+1)))*np.pi)


# f1
x = np.linspace(-1, 1, 1000)
nList = [4, 8, 16, 24, 48, 96]
l = len(nList)+5
# orig:
plt.subplot(1, 2, 1)
plt.title(r'Wielomiany interpolacyjne funkcji $f_1(x)=\frac{1}{1+25x^{2}}$ w zależności od stopnia n')
plt.grid()
plt.plot(x, f1(x), label='$f(x)$', linewidth=5)
# interpolations
for k, n in enumerate(nList):
    inter = generateInterpolation([[nodeGen2(i, n), f1(nodeGen2(i, n))] for i in range(n+1)])
    x = np.linspace(-1, 1, 1000)
    plt.plot(x, inter(x), label='$W_{'+str(n)+'}(x)$')
plt.legend(loc='lower center')

# f2
x = np.linspace(-1, 1, 1000)
nList = [4, 8, 16, 24, 48, 96]
l = len(nList)+5
# orig:
plt.subplot(1, 2, 2)
plt.title(r'Wielomiany interpolacyjne funkcji $f_2(x)=\frac{1}{1+x^{2}}$ w zależności od stopnia n')
plt.grid()
plt.plot(x, f2(x), label='$f(x)$', linewidth=5)
# interpolations
for k, n in enumerate(nList):
    inter = generateInterpolation([[nodeGen2(i, n), f2(nodeGen2(i, n))] for i in range(n+1)])
    x = np.linspace(-1, 1, 1000)
    plt.plot(x, inter(x), label='$W_{'+str(n)+'}(x)$')
plt.legend(loc='lower center')

plt.suptitle(r'Interpolacja wybranych funkcji za pomocą siatki $x_i=cos(\frac{2i+1}{2(n+1)}\pi)$')
plt.show()
