import numpy as np
from matplotlib import pyplot as plt
from shared import *

linspace = np.linspace(-1, 1, 1000)
nList = [4, 6, 8, 10]
fig = plt.figure()
plt.suptitle(
    'Błąd przy interpolacji funkcji $f(x)=\\frac{1}{1+25x^{2}}$ za pomocą naturalnych splajnów kubicznych, w zależności od ilości punktów, przez które przechodzi spline')
for i, n in enumerate(nList):
    ax = fig.add_subplot(2, 2, i+1)

    plt.title('$| f(x) - S_{' + str(n) + '}(x) |$')
    spline, xPoints, _ = createSpline(n)
    ax.set_xticks(xPoints)
    plt.plot(linspace, [abs(f(x) - spline(x)) for x in linspace], color=f'C{i}')
    ax.grid(which='major', axis='both', alpha=0.8)
plt.tight_layout()
plt.show()
