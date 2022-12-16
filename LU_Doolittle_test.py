def LU_Doolittle_Decomposition(a, n, o, s):
    L = [[0 for x in range(n)]for y in range(n)]
    U = [[0 for x in range(n)]for y in range(n)]
    flops = 0
    for i in range(0, n):
        o[i] = i
        s[i] = abs(a[i][0])
        for j in range(1, n):
            if (abs(a[i][j]) > s[i]):
                s[i] = abs(a[i][j])
    for k in range(0, n-1):
        flops += partialPivot(a, o, s, n, k, flops)
        for i in range(k+1, n):
            factor = a[o[i]][k] / a[o[k]][k]
            flops += 1
            a[o[i]][k] = factor
            for j in range(k+1, n):
                a[o[i]][j] = a[o[i]][j] - factor * a[o[k]][j]
                flops += 2
    for i in range(0, n):
        for j in range(0, n):
            if (i == j):
                L[i][j] = 1
                U[i][j] = a[i][j]
            elif (i > j):
                L[i][j] = a[i][j]
            else:
                U[i][j] = a[i][j]
    # print(f'flops=', flops)
    return L, U


def partialPivot(a, o, s, n, k, flops):
    p = k
    big = abs(a[o[k]][k] / s[o[k]])
    flops += 1
    for i in range(k+1, n):
        temp = abs(a[o[i]][k] / s[o[i]])
        flops += 1
        if (temp > big):
            big = temp
            p = i
    temp = o[p]
    o[p] = o[k]
    o[k] = temp
    return flops


mat = [[2, -1, -2], [-4, 6, 3], [-4, -2, 8]]
n = 3

print(LU_Doolittle_Decomposition(
    mat, n, [0 for x in range(n)], [0 for x in range(n)]))
