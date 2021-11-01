import numpy as np

matrixA1 = np.array([
    [2.40827208, -0.36066254, 0.80575445, 0.46309511, 1.20708553],
    [-0.36066254, 1.14839502, 0.02576113, 0.02672584, -1.03949556],
    [0.80575445, 0.02576113, 2.45964907, 0.13824088, 0.0472749],
    [0.46309511, 0.02672584, 0.13824088, 2.05614464, -0.9434493],
    [1.20708553, -1.03949556, 0.0472749, -0.9434493, 1.92753926],
])
matrixA2 = np.array([
    [2.61370745, -0.6334453, 0.76061329, 0.24938964, 0.82783473],
    [-0.6334453, 1.51060349, 0.08570081, 0.31048984, -0.53591589],
    [0.76061329, 0.08570081, 2.46956812, 0.18519926, 0.13060923],
    [0.24938964, 0.31048984, 0.18519926, 2.27845311, -0.54893124],
    [0.82783473, -0.53591589, 0.13060923, -0.54893124, 2.6276678],
])

eigA = list(np.linalg.eig(matrixA1)[0])
eigB = list(np.linalg.eig(matrixA2)[0])
absEigA = [abs(el) for el in eigA]
absEigB = [abs(el) for el in eigB]
print('Wartości własne macierzy A:', eigA)
print('minLambda =', min(absEigA))
print('maxLambda =', max(absEigA))
print('kappa =', max(absEigA)/min(absEigA))
print('\nWartości własne macierzy B:', eigB)
print('minLambda =', min(absEigB))
print('maxLambda =', max(absEigB))
print('kappa =', max(absEigB)/min(absEigB))
