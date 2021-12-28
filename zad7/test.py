import numpy as np
from matplotlib import pyplot as plt
import scipy
from scipy import sparse
from scipy.sparse.linalg import spsolve


def f(x):
    return 1/(1+(25*(x**2)))


def genXiList(n):
    return [-1+2*(i/n) for i in range(n+1)]


n = 5

xi = genXiList(n)
yi = [f(x) for x in xi]

h = (xi[n] - xi[0])/n
wektorY = np.array([(6/(h**2)) * (yi[i-2] - 2*yi[i-1] + yi[i]) for i in range(2, n+1)])
matrix = sparse.diags([1, 4, 1], [-1, 0, 1], shape=(n-1, n-1)).tocsr()
print(matrix)
ksi = spsolve(matrix, wektorY)
print(n)
print(ksi)
