import numpy as np
from matplotlib import pyplot as plt
from scipy import sparse
from scipy.sparse.linalg import spsolve


def f(x):
    return 1/(1+(25*(x**2)))


def genXiList(n):
    return [-1+2*(i/n) for i in range(n+1)]


def createSpline(n):
    xi = genXiList(n)
    yi = [f(x) for x in xi]

    h = (xi[n] - xi[0])/n

    wektorY = np.array([(6/(h**2)) * (yi[i-2] - 2*yi[i-1] + yi[i]) for i in range(2, n+1)])
    matrix = sparse.diags([1, 4, 1], [-1, 0, 1], shape=(n-1, n-1)).tocsr()
    ksi = spsolve(matrix, wektorY)

    print(f'xi: {xi}')
    print(f'yi: {yi}')

    def KSIi(i):
        if i == 0 or i == n:
            return 0
        return ksi[i-1]

    def Ai(i): return (yi[i] - yi[i-1])/h - (h/6)*(KSIi(i) - KSIi(i-1))
    def Bi(i): return yi[i-1] - KSIi(i-1)*((h**2)/6)

    def spline(x):
        i = [i for i, val in enumerate(xi) if val >= x][0]
        y = (KSIi(i-1) * ((xi[i]-x)**3)) + (KSIi(i) * ((x-xi[i-1])**3)) + (Ai(i)*(x-xi[i-1])) + Bi(i)
        print(f'x={x}, y={y}')
        return y

    return spline


linspace = np.linspace(-1, 1, 100)
nList = [4]
# orig:
# plt.title(r'Wielomiany interpolacyjne funkcji $f_1(x)=\frac{1}{1+25x^{2}}$ w zależności od stopnia n')
plt.grid()
plt.plot(linspace, f(linspace), label='$f(x)$', linewidth=5)
# interpolations
for k, n in enumerate(nList):
    spline = createSpline(n)
    plt.plot(linspace, [spline(x) for x in linspace], label='$S_{'+str(n)+'}(x)$')
plt.legend(loc='lower center')

plt.show()
