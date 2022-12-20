import copy
import math
import GaussMethods as GM


# --------------------- Separator ---------------------
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


# --------------------- Separator ---------------------
def crout(mat, sigdig = 10):
    n_eq = len(mat)
    # initializing L = 0 matrix and U = identity
    L = [[0]*n_eq for i in range(n_eq)]
    U = [[1 if i==j else 0 for j in range(n_eq)] for i in range(n_eq)]
    # initializing steps array
    steps = []
    steps.append(Step(L , f'L matrix'))
    steps.append(Step(U, f'U matrix'))

    for j in range(n_eq):

        # Lower Matrix Element Calculation      - Consider the j as iterating over each column
        for i in range(j, n_eq):                  # iterating over each element in the column of the lower matrix.
            sum = 0
            for k in range(j): sum = roundsig(sum + L[i][k] * U[k][j] , sigdig)
            L[i][j] = roundsig(mat[i][j] - sum , sigdig)

            steps.append(Step(L , f'in L matrix, L[{i+1}][{j+1}] = A[{i+1}][{j+1}] - {sum}')) # log step
        
        # Upper Matrix Element Calculation      - Consider the j as iterating over each row
        for i in range(j+1, n_eq):
            sum = 0
            for k in range(j):
                sum = roundsig(sum + L[j][k] * U[k][i] , sigdig)
            if L[j][j] == 0:
                raise Exception("Diagonal element is 0, cannot be solved by Crout decomposition.")
            U[j][i] = roundsig((mat[j][i] - sum) / L[j][j] , sigdig)

            steps.append(Step(U , f'in U matrix, U[{j+1}][{i+1}] = (A[{j+1}][{i+1}] - {sum}) / L[{j+1}][{j+1}]')) # log step

    return steps, L, U


def ans_crout(A, b, significant_digits = 10):

    steps1, L, U = crout(A, significant_digits)
    steps1.append(Step(L , f'L is augmented with b to solve for y.'))
    y, steps2 = GM.forward_substitution(L , steps1, b, significant_digits)
    steps2.append(Step(U , f'U is augmented with y to get the final solution.'))
    sol, steps3 = GM.backward_substitution(U, steps2, y, significant_digits)

    return GM.steps_to_string(steps3, significant_digits)

# A = [
#     [5, 4, 1],
#     [10, 9, 4],
#     [10, 13, 15]
# ]
#
# steps, L, U = crout(A, sigdig = 10)
#
# view_matrix(L)
# view_matrix(U)
#
# for step in steps:
#     print(step.description + "\n")
#     view_matrix(step.matrix)
