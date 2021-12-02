import numpy as np
from matplotlib import pyplot as plt
import math
np.seterr(divide='ignore')

N = 100
ACCURACY = 0.00000001


def getA(i, j):
    "Macierz A trzymana jako funkcja"
    if i == j:
        return 3
    elif abs(i-j) == 1:
        return 1
    elif abs(i-j) == 2:
        return 0.2
    return 0


def getVectorB(i):
    "Vektor B trzymany jako funkcja"
    return i+1


def jacobi(startVector, accuracy, expectedRes=None):
    "if expectedRes, creates plot point list"
    plotList = []
    prevNorm = 0
    vectorX = startVector
    # after 1000 tries program assumes, that result failed to converge
    for n in range(1, 1000):
        nextVectorX = []
        for i in range(N):
            # sum k<i
            sum1 = 0
            if i > 0:
                sum1 += getA(i, i-1)*vectorX[i-1]
            if i > 1:
                sum1 += getA(i, i-2)*vectorX[i-2]
            # sum k>i
            sum2 = 0
            if i < N-1:
                sum2 += getA(i, i+1)*vectorX[i+1]
            if i < N-2:
                sum2 += getA(i, i+2)*vectorX[i+2]
            nextVectorX.append((getVectorB(i)-sum1-sum2)/getA(i, i))
        newNorm = np.linalg.norm((np.array(vectorX)-np.array(nextVectorX)))
        vectorX = nextVectorX

        # if creating plot points
        if expectedRes:
            plotList.append(np.log10(np.linalg.norm(np.array(vectorX) - np.array(expectedRes))))

        # stop condition - vector norm changed by less than 10e-08
        if math.isclose(newNorm, prevNorm, abs_tol=accuracy):
            if expectedRes:
                return vectorX, n, plotList
            return vectorX, n
        prevNorm = newNorm


def gauss(startVector, accuracy, expectedRes=None):
    "if expectedRes, creates plot point list"
    plotList = []
    prevNorm = 0
    vectorX = startVector
    # after 1000 tries program assumes, that result failed to converge
    for n in range(1, 1000):
        nextVectorX = []
        for i in range(N):
            # sum k<i
            sum1 = 0
            if i > 0:
                sum1 += getA(i, i-1)*nextVectorX[i-1]
            if i > 1:
                sum1 += getA(i, i-2)*nextVectorX[i-2]
            # sum k>i
            sum2 = 0
            if i < N-1:
                sum2 += getA(i, i+1)*vectorX[i+1]
            if i < N-2:
                sum2 += getA(i, i+2)*vectorX[i+2]
            nextVectorX.append((getVectorB(i)-sum1-sum2)/getA(i, i))
        newNorm = np.linalg.norm((np.array(vectorX)-np.array(nextVectorX)))
        vectorX = nextVectorX

        # if creating plot points
        if expectedRes:
            plotList.append(np.log10(np.linalg.norm(np.array(vectorX) - np.array(expectedRes))))

        # stop condition - vector norm changed by less than 10e-08
        if math.isclose(newNorm, prevNorm, abs_tol=accuracy):
            if expectedRes:
                return vectorX, n, plotList
            return vectorX, n
        prevNorm = newNorm


# get result to calculate x(n) - x* for plots
result, iterCount = gauss([1]*N, ACCURACY)
print(f'result converged after {iterCount} iterations:\n', np.array(result))


def generatePlot(startVector, title, pos, size, ticks):
    _, jSize, jPlotList = jacobi(startVector, ACCURACY, result)
    _, gSize, gPlotList = gauss(startVector, ACCURACY, result)
    plt.subplot(size, 1, pos)
    plt.title(title)
    # plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.plot([i for i in range(1, jSize+1)], jPlotList, label="Jacobi")
    plt.plot([i for i in range(1, gSize+1)], gPlotList, label="Gauss")
    plt.xlabel('n')
    plt.ylabel('log || x(n) - x* ||')
    plt.legend()
    plt.gca().set_yticks(ticks)
    plt.grid()


# starting point = vector of 1's
generatePlot([1]*N, 'Start z wektora [1,1,...,1]:', 1, 3, np.arange(2, -9, step=-2))
# starting point = near result vector
generatePlot([r - 0.5 for r in result], 'Start z wektora "s[n] = wynik[n]-0.5":', 2, 3, np.arange(0, -9, step=-2))
# starting point = far from result vector
generatePlot([1000] * N, 'Start z wektora [1000,1000,...,1000]:', 3, 3, np.arange(4, -9, step=-2))

# show plot
plt.suptitle('Zbliżanie się do wyniku metod iteracyjnych dla wybranych wektorów startowych')
plt.tight_layout()
plt.show()
