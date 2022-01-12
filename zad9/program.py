import numpy as np
from matplotlib import pyplot as plt
from common import *


def f(x):
    return np.sin(x)-0.37


def g(x):
    return (np.sin(x)-0.37)**2


xStar = np.arcsin(0.37)
print(xStar)

MAXI = 10

plt.subplot(1, 2, 1)
plt.title('Dla funkcji $ f(x)=sin(x)-0.37 $')
plt.yscale('log')
plt.grid()
bisectRes = bisect(f, 0, np.pi/2, MAXI)
plt.plot([i+1 for i in range(len(bisectRes))], [abs(xStar - xi) for xi in bisectRes], '-o', label='Metoda bisekcji', )
falsiRes = falsi(f, 0, np.pi/2, MAXI)
plt.plot([i+1 for i in range(len(falsiRes))], [abs(xStar - xi) for xi in falsiRes], '-o', label='Metoda falsi', )
secantsRes = secants(f, 1, np.pi/2, MAXI)
plt.plot([i+1 for i in range(len(secantsRes))], [abs(xStar - xi) for xi in secantsRes], '-o', label='Metoda siecznych', )
newtonRes = newton(f, np.cos, 1, MAXI)
print([abs(xStar - xi) for xi in newtonRes])
plt.plot([i+1 for i in range(len(newtonRes))], [abs(xStar - xi) for xi in newtonRes], '-o', label='Metoda Newtona', )
plt.gca().set_yticks([1, 0.01, 0.0001, 0.000001, 0.00000001, 0.0000000001, 0.000000000001, 0.00000000000001, 0.0000000000000001, ])
plt.legend()

plt.show()
