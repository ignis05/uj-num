import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from funkcje import *


def f(x):
    return np.sin(x)-0.37


def g(x):
    return (np.sin(x)-0.37)**2


def gPrim(x):
    return 2 * (np.sin(x)-0.37) * np.cos(x)


def u(x):
    return g(x)/gPrim(x)


def uPrim(x):
    return ((np.sin(x)-0.37)*np.tan(x)*np.arcsin(x)+1) / 2


xStar = np.arcsin(0.37)


plt.subplot(1, 2, 1)
plt.title('Dla funkcji $ f(x)=sin(x)-0.37 $')
plt.yscale('log')
plt.grid()
bisectRes = bisect(f, 0, np.pi/2, 20)
plt.plot([i+1 for i in range(len(bisectRes))], [abs(xStar - xi) for xi in bisectRes], '-o', label='Metoda bisekcji', )
falsiRes = falsi(f, 0, np.pi/2, 13)
plt.plot([i+1 for i in range(len(falsiRes))], [abs(xStar - xi) for xi in falsiRes], '-o', label='Metoda falsi', )
secantsRes = secants(f, 0, np.pi/2, 10)
plt.plot([i+1 for i in range(len(secantsRes))], [abs(xStar - xi) for xi in secantsRes], '-o', label='Metoda siecznych', )
newtonRes = newton(f, np.cos, 1, 10)
plt.plot([i+1 for i in range(len(newtonRes))], [abs(xStar - xi) for xi in newtonRes], '-o', label='Metoda Newtona', )
plt.gca().set_yticks([1, 0.01, 0.0001, 0.000001, 0.00000001, 0.0000000001, 0.000000000001, 0.00000000000001, 0.0000000000000001, ])
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.xlabel('iteracja')
plt.ylabel('$|x* - x_i|$')
plt.legend(loc='upper right')

plt.subplot(1, 2, 2)
plt.title('Dla funkcji $ g(x)=(sin(x)-0.37)^2 $  ( dla $u(x)=\\frac{g(x)}{g\'(x)}$)')
plt.yscale('log')
plt.grid()
# * bisekcji i falsi wymagaja przeciwnych znakow, g(x) ma tylko wartosci nieujemne
secantsRes = secants(u, 0, np.pi/2, 10)
plt.plot([i+1 for i in range(len(secantsRes))], [abs(xStar - xi) for xi in secantsRes], '-o', label='Metoda siecznych', color='C2')
newtonRes = newton(u, uPrim, 1, 10)
plt.plot([i+1 for i in range(len(newtonRes))], [abs(xStar - xi) for xi in newtonRes], '-o', label='Metoda Newtona', color='C3')
plt.gca().set_yticks([1, 0.01, 0.0001, 0.000001, 0.00000001, 0.0000000001, 0.000000000001, 0.00000000000001, 0.0000000000000001, ])
plt.xlabel('iteracja')
plt.ylabel('$|x* - x_i|$')
plt.legend(loc='upper right')

plt.tight_layout()
plt.suptitle('Odchylenie przybliżonej wartości pierwiastka od dokładnego wyniku w zależności od wybranych funkcji i metod iteracyjnych')
plt.show()
