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

    def KSIi(i):
        if i == 0 or i == n:
            return 0
        return ksi[i-1]

    def Ai(i): return (yi[i] - yi[i-1])/h - (h/6)*(KSIi(i) - KSIi(i-1))
    def Bi(i): return yi[i-1] - KSIi(i-1)*((h**2)/6)

    def spline(x):
        # sprawdzenie w ktorym przedziale jest x
        i = len(xi)-1
        for index, val in enumerate(xi):
            if val > x:
                i = index
                break
        y = (KSIi(i-1) * ((xi[i]-x)**3)/(6*h)) + (KSIi(i) * ((x-xi[i-1])**3)/(6*h)) + (Ai(i)*(x-xi[i-1])) + Bi(i)
        return y

    return spline, xi, yi


linspace = np.linspace(-1, 1, 100)
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
