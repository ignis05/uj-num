import numpy as np


def bisect(f, a, b, maxI):
    resList = []

    Fa = f(a)
    Fb = f(b)

    for i in range(1, maxI+1):
        c = (a+b)/2
        Fc = f(c)
        # print(f'a:{a}, Fa:{Fa}, b:{b}, Fb:{Fb}')
        # print(f'c:{c}, i:{i}, f(c)={Fc}')
        if np.sign(Fc) == np.sign(Fa):
            Fa = Fc
            a = c
        else:
            Fb = Fc
            b = c
        resList.append(c)

    return resList


def falsi(f, a, b, maxI):
    resList = []

    Fa = f(a)
    Fb = f(b)

    for i in range(1, maxI+1):
        c = (a*Fb - b*Fa)/(Fb-Fa)
        Fc = f(c)
        # print(f'a:{a}, Fa:{Fa}, b:{b}, Fb:{Fb}')
        # print(f'c:{c}, i:{i}, f(c)={Fc}')
        if np.sign(Fc) == np.sign(Fa):
            Fa = Fc
            a = c
        else:
            Fb = Fc
            b = c
        resList.append(c)

    return resList


def secants(f, x0, x1, maxI):
    resList = []

    xi_minus = x0
    fi_minus = f(x0)
    xi = x1
    fi = f(x1)

    for i in range(1, maxI+1):
        xi_plus = (xi_minus*fi - xi*fi_minus)/(fi - fi_minus)
        fi_plus = f(xi_plus)
        xi_minus, fi_minus, xi, fi = xi, fi, xi_plus, fi_plus  # swap variables
        resList.append(xi_plus)

    return resList


def newton(f, fprim, x0, maxI):
    resList = []

    xi = x0

    for i in range(1, maxI+1):
        xi = xi - (f(xi)/fprim(xi))
        resList.append(xi)

    return resList
