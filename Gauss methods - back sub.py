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

def max_piv_row(temp, piv_index, sigdig = 10, scaling = False):

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

def view_matrix(mat):
    for i in mat:
        for j in i:
            print(f'{j}   ', end = '')
        print("\n")
    print('\n')

# -------------------------------------------------------- UTILITY FUNCTIONS --------------------------------------------------------


def gauss_elim(mat, scaling = False, sigdig = 10): 

    n_eq = len(mat)
    steps = []
    # pivots loop loops n_eq-1 times because the matrix will be upper
    # triangular by the time we have reached the last pivot
    for i in range(n_eq-1):

        iswitch = max_piv_row(copy.deepcopy(mat), i, scaling)
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
    
    return steps



def gauss_jordan_elim(mat, scaling = False, sigdig = 10):

    n_eq = len(mat)
    steps = gauss_elim(mat, scaling, sigdig)

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

    return steps


def backward_substitution(mat, sigdig = 10):

    n_eq = len(mat)

    # gauss elimination puts all zero rows at the bottom,
    # so we loop over them with this boolean
    zeropivots = True 

    # if there are infinite solutions, we set all free variables to 1
    infinitesol = False
    sol = [1]*n_eq # initialize solution vector with 1's

    for i in range(n_eq-1, -1, -1):

        if zeropivots and mat[i][i] == 0: 
            if mat[i][n_eq] != 0:
                raise Exception("Inconsistent System")
            else:
                infinitesol = True
                continue
        else:
            zeropivots = False

        sol[i] = mat[i][n_eq]
        for j in range(i+1,n_eq): sol[i] = roundsig(sol[i] - sol[j]*mat[i][j] , sigdig)
        sol[i] = roundsig(sol[i]/mat[i][i] , sigdig)

    return sol, infinitesol


def GJ_substitution(mat, sigdig = 10):

    n_eq = len(mat)
    # index of the first non-zero pivot
    firstnonzero = n_eq-1
    # if there are infinite solutions, we set all free variables to 1
    infinitesol = False
    sol = [1]*n_eq # initialize solution vector with 1's

    # loop to check for free variables and inconsistent systems
    for i in range(n_eq-1, 0, -1): 

        if mat[i][i] == 0: 
            if mat[i][n_eq] != 0:
                raise Exception("Inconsistent System")
            else:
                infinitesol = True
                firstnonzero -= 1
                continue
        else:
            break

    if firstnonzero == n_eq-1: # there are no free variables, solution is just the last column
        for i in range(n_eq): sol[i] = mat[i][n_eq]
    else: # there are free variables whose columns are not eliminated
        for i in range(n_eq):
            sol[i] = mat[i][n_eq]
            for j in range (firstnonzero+1, n_eq): sol[i] -= mat[i][j]

    return sol, infinitesol


def forward_substitution(mat, sigdig = 10):

    n_eq = len(mat)
    sol = [1]*n_eq

    for i in range(n_eq):
        sol[i] = mat[i][n_eq]
        for j in range(i): sol[i]  = roundsig(sol[i]-sol[j]*mat[i][j], sigdig)
        sol[i] = roundsig(sol[i]/mat[i][i], sigdig)

    return sol



A = [
    [1,1,-3,4],
    [2,1,-1,2],
    [3,2,-4,7]
]

sig = 5

steps1 = gauss_elim(copy.deepcopy(A), sig)
steps2 = gauss_jordan_elim(copy.deepcopy(A), sig)

for step in steps2:
    print(step.description)
    view_matrix(step.matrix)


for step in steps1:
    print(step.description + "\n")
    view_matrix(step.matrix)
sol,infinite = backward_substitution(steps1[len(steps1)-1].matrix, sig)

for elem in sol: print(elem)

print(f'\n{infinite}')

