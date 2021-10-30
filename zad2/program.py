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
vectorB = np.array([5.40780228, 3.67008677, 3.12306266,  -1.11187948, 0.54437218]).T
vectorBprim = vectorB + np.array([1e-05, 0, 0, 0, 0]).T

vectorY1 = np.linalg.solve(matrixA1, vectorB)
vectorYprim1 = np.linalg.solve(matrixA1, vectorBprim)
delta1 = np.linalg.norm(vectorY1-vectorYprim1, ord=2)
print('\ndla i=1:', '\ny1= ', vectorY1, "\ny'1= ", vectorYprim1, '\ndelta1= ', delta1)

vectorY2 = np.linalg.solve(matrixA2, vectorB)
vectorYprim2 = np.linalg.solve(matrixA2, vectorBprim)
delta2 = np.linalg.norm(vectorY2-vectorYprim2, ord=2)
print('\ndla i=2:', '\ny2= ', vectorY2, "\ny'2= ", vectorYprim2, '\ndelta2= ', delta2)
