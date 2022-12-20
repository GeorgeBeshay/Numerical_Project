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


def LU_Doolittle(matrix, scFlag, precision, b):

    if precision==0:
        precision=10

    n = len(matrix)
    order = [0 for x in range(n)]
    scaling = [0 for x in range(n)]
    steps = ""

    steps = LU_Doolittle_Decomposition(
        matrix, n, order, scaling, scFlag, precision, steps)

    steps += substitute(matrix, order, b, precision)
    # print(steps)

    return steps


def LU_Doolittle_Decomposition(matrix, n, o, s, scFlag, precision, steps):
    for i in range(0, n):
        o[i] = i
        s[i] = signif(abs(matrix[i][0]), precision)
        for j in range(1, n):
            if (abs(matrix[i][j]) > s[i]):
                s[i] = signif(abs(matrix[i][j]), precision)
    for k in range(0, n-1):
        steps = partialPivot(matrix, o, s, n, k, scFlag, precision, steps)
        for i in range(k+1, n):
            factor = signif((matrix[o[i]][k] / matrix[o[k]][k]), precision)
            matrix[o[i]][k] = factor
            steps += addStep(matrix, steps)
            steps += f"factor = Matrix[{o[i]}][{k}]/ Matrix[{o[k]}][{k}]\n\n"
            steps += "---------------------------------------------------------------------\n"
            for j in range(k+1, n):
                matrix[o[i]][j] = signif(
                    (matrix[o[i]][j] - factor * matrix[o[k]][j]), precision)
                steps += addStep(matrix, steps)
                steps += f"Matrix[{o[i]}][{j}] = Matrix[{o[i]}][{j}] - factor * Matrix[{o[k]}][{j}]\n\n"
                steps += "------------------------------------------------------------------------\n"
    return steps


def partialPivot(matrix, o, s, n, k, scFlag, precision, steps):
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
    if (p != k):
        steps += f"Row {p} is replaced by Row {k}\n\n"
        steps += "---------------------------------------------------------------\n"
    return steps


def addStep(matrix, steps):
    step = ""
    for i in range(len(matrix)):
        step += ("".join([str(item) +
                          "        " for item in matrix[i]])+"\n\n")
    return step


def substitute(martix, o, b, percision):
    step = ""
    y = [0 for x in range(len(martix))]
    n = len(martix)
    y[o[0]] = signif(b[o[0]], percision)
    step += "--------------------------------------------------------------------------------------------------------------------\n\n"
    step += "Applying Forward Elimination\n\n"
    step += f"y[{o[0]}] = {b[o[0]]}\n\n"
    for i in range(1, n):
        sum = signif(b[o[i]], percision)
        for j in range(0, i):
            sum = signif(sum - martix[o[i]][j] * y[o[j]], percision)
        y[o[i]] = sum
        step += f"y[{o[i]}] = {sum}\n\n"

    x = [0 for x in range(n)]
    x[n-1] = signif(y[o[n-1]] / martix[o[n-1]][n-1], percision)
    step += "-------------------------------------------------------------------------------------------------------------------\n\n"
    step += "Applying Backward Elimination\n\n"
    step += f"x[{n-1}] = {x[n-1]}\n\n"
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum = signif(sum + martix[o[i]][j] * x[j], percision)
        x[i] = signif((y[o[i]] - sum) / martix[o[i]][i], percision)
        step += f"x[{i}] = {x[i]}\n\n"
    step += "-------------------------------------------------------------------------------------------------------------------\n\n"
    step += f"The Solution is:({x[0]} "
    for i in range(1, n):
        step += f", {x[i]}"
    step += ")\n\n ------------------------------------------------------------------------------------------------------------------"
    return step


# mat = [[2, 1, 1, 1, 1], [1, 2, 1, 1, 1], [
#     1, 1, 2, 1, 1], [1, 1, 1, 2, 1], [1, 1, 1, 1, 2]]
# b = [4, 5, 6, 7, 8]

# LU_Doolittle(mat, False, 4, b)
