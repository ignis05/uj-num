
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve


def f(x):
    return 1/(1+(25*(x**2)))


def createSpline(n):
    """Generuje i zwraca funkcje s(x) dla podanego n

    Args:
        n (int): ilość punktów przez które powinien przechodzić spline
    """

    def genXiList(n):
        return [-1+2*(i/n) for i in range(n+1)]

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
