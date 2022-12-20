import math
import copy


class Step:
    def __init__(self, matrix, description):
        self.matrix = copy.deepcopy(matrix)
        self.description = description


def signif(x, digits=6):
    if x == 0 or not math.isfinite(x):
        return x
    digits -= math.ceil(math.log10(abs(x)))
    return round(x, digits)


def LU_Doolittle(matrix, scFlag, precision):
    n = len(matrix)
    order = [0 for x in range(n)]
    scaling = [0 for x in range(n)]

    return LU_Doolittle_Decomposition(matrix, n, order, scaling, scFlag, precision)


def LU_Doolittle_Decomposition(matrix, n, o, s, scFlag, precision):
    L = [[0 for x in range(n)]for y in range(n)]
    U = [[0 for x in range(n)]for y in range(n)]
    steps = []
    for i in range(0, n):
        o[i] = i
        s[i] = signif(abs(matrix[i][0]), precision)
        for j in range(1, n):
            if (abs(matrix[i][j]) > s[i]):
                s[i] = signif(abs(matrix[i][j]), precision)
    for k in range(0, n-1):
        partialPivot(matrix, o, s, n, k, scFlag, precision)
        for i in range(k+1, n):
            factor = signif((matrix[o[i]][k] / matrix[o[k]][k]), precision)
            matrix[o[i]][k] = factor
            # steps.append(Step (matrix=matrix, f"Matrix[{o[i]}]" ))
            for j in range(k+1, n):
                matrix[o[i]][j] = signif(
                    (matrix[o[i]][j] - factor * matrix[o[k]][j]), precision)
    for i in range(0, n):
        for j in range(0, n):
            if (i == j):
                L[i][j] = 1
                U[i][j] = matrix[i][j]
            elif (i > j):
                L[i][j] = matrix[i][j]
            else:
                U[i][j] = matrix[i][j]
    return L, U


def partialPivot(matrix, o, s, n, k, scFlag, precision):
    p = k
    if (scFlag):
        big = signif((abs(matrix[o[k]][k] / s[o[k]])), precision)
    else:
        big = signif(abs(matrix[o[k]][k]), precision)
    for i in range(k+1, n):
        if (scFlag):
            temp = signif(abs(matrix[o[i]][k] / s[o[i]]), precision)
        else:
            temp = signif(abs(matrix[o[i]][k]), precision)
        if (temp > big):
            big = temp
            p = i
    temp = o[p]
    o[p] = o[k]
    o[k] = temp


# mat = [[2, -1, -2], [-4, 6, 3], [-4, -2, 8]]

# print(LU_Doolittle(mat, True, 4))
