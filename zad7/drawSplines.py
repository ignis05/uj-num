import numpy as np
from matplotlib import pyplot as plt
from shared import *


linspace = np.linspace(-1, 1, 1000)
nList = [3, 4, 5, 6, 8, 16]
# orig:
plt.title(
    'Interpolacja funkcji $f(x)=\\frac{1}{1+25x^{2}}$ za pomocą naturalnych splajnów kubicznych przechodzących przez punkty $x_i=-1+2\\frac{i}{n}$ dla kilku wybranych $n$.')
plt.grid()
plt.plot(linspace, f(linspace), label='$f(x)$', linewidth=5)
plt.scatter([0], [1], marker='.', zorder=0)  # so the marker colors are in sync
# interpolations
for index, n in enumerate(nList):
    spline, dotsX, dotsY = createSpline(n)
    plt.plot(linspace, [spline(x) for x in linspace], label='$S_{'+str(n)+'}(x)$')
    plt.scatter(dotsX, dotsY, zorder=(len(nList)*10)-(index*10), marker='+')
plt.legend(loc='lower center')

plt.show()
