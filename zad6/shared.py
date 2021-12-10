def generateInterpolation(nodeList):
    "generates interpolation function from list of points"
    def interFunc(x):
        res = 0
        for i, [xi, yi] in enumerate(nodeList):
            upProd = 1
            loProd = 1
            for j, [xj, yj] in enumerate(nodeList):
                if i == j:
                    continue
                upProd *= x-xj
                loProd *= xi-xj
            res += yi * upProd/loProd
        return res
    return interFunc
