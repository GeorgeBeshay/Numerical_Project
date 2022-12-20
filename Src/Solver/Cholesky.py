import copy, math
from math import sqrt

class Step:
    def __init__(self, matrix, description):
        self.matrix = copy.deepcopy(matrix)
        self.description = description

def roundsig(x, digits = 10):
    if x == 0 or not math.isfinite(x):
        return x
    digits -= math.ceil(math.log10(abs(x)))
    return round(x, digits)

def view_matrix(mat):
    for i in mat:
        for j in i:
            print(f'{j}   ', end = '')
        print("\n")
    print('\n')

def cholesky(mat, sigdig = 10):

    n_eq = len(mat)
    L = [[0]*n_eq for i in range(n_eq)]
    U = [[0]*n_eq for i in range(n_eq)]
    steps = []
    
    for i in range(n_eq):
        for j in range (i+1):
            
            sum = 0

            if j == i:
                for k in range(j): sum = roundsig(sum + L[j][k]**2 , sigdig)
                try:
                    L[i][i] = roundsig(sqrt(mat[i][i]-sum) , sigdig)
                    U[i][i] = L[i][i]
                except ValueError:
                    raise Exception("Not positive definite, cannot be solved by Cholesky decomposition.")

                steps.append(Step(L , f'L[{i+1}][{i+1}] = sqrt(A[{i+1}][{i+1}] - {sum})'))
            else:

                if mat[i][j] != mat[j][i]:
                    raise Exception("Matrix is not symmetric, cannot be solved by Cholesky decomposition.")
                if L[j][j] == 0:
                    raise Exception("Diagonal element is 0, cannot be solved by Cholesky decomposition.")

                for k in range(j): sum = roundsig(sum + L[j][k]*L[i][k] , sigdig)
                L[i][j] = roundsig((mat[i][j]-sum) / L[j][j] , sigdig)
                U[j][i] = L[i][j]
                steps.append(Step(L , f'L[{i+1}][{j+1}] = (A[{i+1}][{j+1}] - {sum}) / L[{j+1}][{j+1}]'))

    return steps , L , U

A = [
    [6,15,55],
    [15,55,225],
    [55,225,979]
]

steps , L , U = cholesky(A)

view_matrix(L)
view_matrix(U)
for step in steps:
    print(step.description + "\n")
    view_matrix(step.matrix)