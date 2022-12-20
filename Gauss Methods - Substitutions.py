import copy, math
# -------------------------------------------------------- UTILITY FUNCTIONS --------------------------------------------------------

class Step:
    def __init__(self, matrix, description):
        self.matrix = copy.deepcopy(matrix)
        self.description = description

def roundsig(x, digits = 10):
    if x == 0 or not math.isfinite(x):
        return x
    digits -= math.ceil(math.log10(abs(x)))
    return round(x, digits)

def max_piv_row(temp, piv_index, scaling = False, sigdig = 10):

    if scaling: # change the target part so each row is normalized by its largest coefficient
        for i in range(piv_index, len(temp)):
            # get a temporary list of the magitude of all coefficients excluding the constant
            temprow = [abs(temp[x]) for x in range(len(temp)-1)]
            max_coeff = max(temprow) 
            # divide each element by largest element
            for j in range(piv_index, len(temp)): temp[i][j] = roundsig(temp[i][j]/max_coeff , sigdig) 

    maxrow = piv_index
    max = abs(temp[piv_index][piv_index])
    
    for i in range( piv_index+1, len(temp) ):
        if abs(temp[i][piv_index]) > max: #piv_index represents both the row and column of current pivot
            max = abs(temp[i][piv_index])
            maxrow = i

    return maxrow


def steps_to_string(steps, dig):
    ans = f''
    for step in steps:
        ans += step.description + '\n\n'
        if step.matrix:
            for i in step.matrix:
                for j in i:
                    ans += f'{j:{dig+6}.{dig}f}'
                ans += '\n\n'
            ans += '\n\n'
    
    return ans


# -------------------------------------------------------- UTILITY FUNCTIONS --------------------------------------------------------


def gauss_elim(matrix, scaling = False, sigdig = 10): 

    mat = copy.deepcopy(matrix)
    n_eq = len(mat)
    steps = []
    steps.append(Step(mat , f'A = '))
    # pivots loop loops n_eq-1 times because the matrix will be upper
    # triangular by the time we have reached the last pivot
    for i in range(n_eq-1):

        iswitch = max_piv_row(copy.deepcopy(mat), i, scaling, sigdig)
        if (iswitch != i):
            mat[i] , mat[iswitch] = mat[iswitch] , mat[i] # switch with larget pivot row
            steps.append(Step(mat , f'Switch R{i+1} and R{iswitch+1} to get the maximum pivot.')) # log step

        if mat[i][i] == 0: continue # if largest pivot is 0, skip this pivot and let substitution handle it

        for j in range(i+1,n_eq): # elimination loop
            
            if mat[j][i] == 0: continue # if element is already 0, skip to next row

            multiplier = roundsig(mat[j][i]/mat[i][i] , sigdig)
            # looping over one row to carry out elimination (including constants)
            for k in range(i,n_eq+1):
                mat[j][k] = roundsig(mat[j][k]-multiplier*mat[i][k] , sigdig)

            steps.append(Step(mat ,f'R{j+1} <- R{j+1}-({multiplier})R{i+1}')) # log step
    
    return mat, steps



def gauss_jordan_elim(matrix, scaling = False, sigdig = 10):

    n_eq = len(mat)
    mat , steps = gauss_elim(matrix, scaling, sigdig)

    # reverse pivot loop
    for i in range(n_eq-1, -1, -1):

        if mat[i][i] == 0: continue # no pivot which means it's a free variable, move to next pivot

        if mat[i][i] != 1:

            piv = mat[i][i]
            # normalise the row by the pivot to make it = 1
            for j in range(i,n_eq+1): mat[i][j] = roundsig(mat[i][j]/piv , sigdig)

            steps.append(Step(mat, f'Divide R{i+1} by {piv}.')) #log step

        # in the backward elimination, the pivot is 1 so the multiplier
        # is the element we wish to eliminate.
        for j in range(i-1, -1, -1):

            if mat[j][i] == 0: continue 
            multiplier = mat[j][i]

            for k in range (i,n_eq+1):
                if mat[i][k] == 0: continue # no change would happen
                mat[j][k] = roundsig(mat[j][k]-multiplier*mat[i][k] , sigdig)
            steps.append(Step(mat, f'R{j+1} <- R{j+1}-({multiplier})R{i+1}')) # log step

    return mat, steps


def backward_substitution(matrix, steps, constants = None, sigdig = 10):

    n_eq = len(matrix)

    if constants:
        for i in range(n_eq): matrix[i].append(constants[i])

    # gauss elimination puts all zero rows at the bottom,
    # so we loop over them with this boolean
    zeropivots = True 

    # if there are infinite solutions, we set all free variables to 1
    infinitesol = False
    sol = [1]*n_eq # initialize solution vector with 1's

    for i in range(n_eq-1, -1, -1):

        if zeropivots and matrix[i][i] == 0: 
            if matrix[i][n_eq] != 0:
                raise Exception("Inconsistent System")
            else:
                infinitesol = True
                continue
        else:
            zeropivots = False

        sum = 0
        for j in range(i+1,n_eq): sum = roundsig(sum + sol[j]*matrix[i][j] , sigdig)
        sol[i] = roundsig((matrix[i][n_eq]-sum)/matrix[i][i] , sigdig)
        stepstr = f'X[{i+1}] = ({matrix[i][n_eq]}-{sum})'
        if matrix[i][i] != 1:
            stepstr += f'/{matrix[i][i]}'
        stepstr += f' = {sol[i]}'
        steps.append(Step(None , stepstr))

    stepstr = f'The solution vector is ('
    for i in range(n_eq-1): stepstr += f'{sol[i]}, '
    stepstr += f'{sol[n_eq-1]}). '

    if infinitesol:
        stepstr += f'This is one of an infinite number of solutions.'
    else:
        stepstr += f'This is a unique solution.'

    steps.append(Step(None , stepstr))

    return sol, steps


def GJ_substitution(matrix, steps, sigdig = 10):

    n_eq = len(matrix)
    # index of the first non-zero pivot
    firstnonzero = n_eq-1
    # if there are infinite solutions, we set all free variables to 1
    infinitesol = False
    sol = [1]*n_eq # initialize solution vector with 1's

    # loop to check for free variables and inconsistent systems
    for i in range(n_eq-1, 0, -1): 

        if matrix[i][i] == 0: 
            if matrix[i][n_eq] != 0:
                raise Exception("Inconsistent System")
            else:
                infinitesol = True
                firstnonzero -= 1
                continue
        else:
            break

    if firstnonzero == n_eq-1: # there are no free variables, solution is just the last column
        for i in range(n_eq):
            sol[i] = matrix[i][n_eq]
            steps.append(Step(None , f'X[{i+1}] = {sol[i]}'))
    else: # there are free variables whose columns are not eliminated
        for i in range(n_eq):
            sol[i] = matrix[i][n_eq]
            for j in range (firstnonzero+1, n_eq): 
                sol[i] = roundsig(sol[i] - matrix[i][j] , sigdig)

        for i in range(n_eq):
            sol[i] = matrix[i][n_eq]
            sum = 0
            for j in range (firstnonzero+1, n_eq): 
                sum = roundsig(sum + matrix[i][j] , sigdig)
            sol[i] = roundsig(matrix[i][n_eq]-sum , sigdig)
            steps.append(Step(None , f'X[{i+1}] = {matrix[i][n_eq]}-{sum} = {sol[i]}'))

    stepstr = f'The solution vector is ('
    for i in range(n_eq-1): stepstr += f'{sol[i]}, '
    stepstr += f'{sol[n_eq-1]}). '

    if infinitesol:
        stepstr += f'This is one of an infinite number of solutions.'
    else:
        stepstr += f'This is a unique solution.'

    steps.append(Step(None , stepstr))

    return sol, steps


def forward_substitution(matrix, steps, constants = None, sigdig = 10):

    if constants:
        for i in range(n_eq): matrix[i].append(constants[i])
    
    n_eq = len(matrix)
    sol = [1]*n_eq

    for i in range(n_eq):
        sol[i] = matrix[i][n_eq]
        sum = 0
        for j in range(i): sum = roundsig(sum + sol[j]*matrix[i][j], sigdig)
        sol[i] = roundsig((matrix[i][n_eq]-sum)/matrix[i][i], sigdig)
        steps.append(Step(None, f'y[{i+1}] = ({matrix[i][n_eq]}-{sum})'))

    return sol, steps



A = [
    [1,-2,1,0],
    [2,1,-3,5],
    [4,-7,1,-1]
]

sig = 5

mat, steps1 = gauss_elim(matrix = A, sigdig = sig)
sol, steps2 = backward_substitution(matrix = mat, steps = steps1, sigdig = sig)
print(steps_to_string(steps2, sig))
