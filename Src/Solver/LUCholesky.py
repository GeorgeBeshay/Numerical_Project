import math
import numpy as np


def cholesky(A):
    L = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(i+1):
            sum1 = 0.0
            for k in range(j):
                sum1 += L[i][k] * L[j][k]
            if i == j:
                print("sin if")
                print("sum= ", sum1)
                print("A[i][j]= ", A[i][j])
                print("[i][j] ", i, j)
                L[i][j] = math.sqrt(A[i][j] - sum1)
                print("L[i][i]= ", L[i][j])
            else:
                print("in else")
                print("sum= ", sum1)
                print("A[i][j]= ", A[i][j])
                print("L[j][j]= ", L[j][j])
                L[i][j] = (A[i][j] - sum1) / L[j][j]
                print("[i][j] ", i, j)
                print("L[i][j]= ", L[i][j])
    lt = np.array(L).T
    return L,lt

#------test------
# A = [[6, 15, 55], [15, 55, 225], [55, 225, 979]]
# L, lt = cholesky(A)
# for r in L:
#     for c in r:
#         print(c, end=" ")
#     print()
# print(" ")
#
# for r in lt:
#     for c in r:
#         print(c, end=" ")
#     print()
# m=np.matmul(np.array(L),np.array(lt))
# print(" ")
#
# for r in m:
#     for c in r:
#         print(c, end=" ")
#     print()
