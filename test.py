from math import log10, floor


# -------------------------------------------------------- UTILITY FUNCTIONS --------------------------------------------------------

def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)

class Step:
    def __init__(self, matrix, description):
        self.matrix = matrix.copy()
        self.description = description


def max_piv_row(temp, piv_index, scaling, sigfig = 5):

    if scaling: # change the target part so each row is normalized by its largest coefficient
        for i in range(piv_index, len(temp)):
            # get a temporary list of the magitude of all coefficients excluding the constant
            temprow = [abs(x) for x in temp[i][slice(len(temp[i])-1)]]
            max_coeff = max(temprow) 
            for j in range(piv_index, len(temp)):
                temp[i][j] = round_sig(temp[i][j]/max_coeff, sigfig) # divide each element by largest element

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
            print(f'{round(j,4)}   ', end = '')
        print("\n")
    print('\n')

# -------------------------------------------------------- UTILITY FUNCTIONS --------------------------------------------------------


def gauss_elim(mat, scaling = False): 

    n_eq = len(mat)
    FLOP_count = 0
    steps = []
    # pivots loop loops n_eq-1 times because the matrix will be upper
    # triangular by the time we have reached the last pivot
    for i in range(n_eq-1):
        
        iswitch = max_piv_row(mat.copy(),i,scaling)
        if (iswitch != i):
            mat[i] , mat[iswitch] = mat[iswitch] , mat[i] # switch with larget pivot row
            #steps.append(Step(mat.copy(), f'Switch R{i+1} and R{iswitch+1} to get the maximum pivot.')) # log step

        for j in range(i+1,n_eq): # elimination loop
            
            if round(mat[j][i],4) == 0: continue

            multiplier = mat[j][i]/mat[i][i]
            FLOP_count+=1
            # looping over one row to carry out elimination (including constants)
            for k in range(i,n_eq+1):
                mat[j][k] = mat[j][k] - multiplier*mat[i][k]
                FLOP_count+=2

            #steps.append(Step(mat ,f'R{j+1} <- R{j+1}-({round(multiplier,4)})R{i+1}')) # log step
    
    return mat, steps, FLOP_count



def gauss_jordan_elim(mat, scaling = False):

    n_eq = len(mat)
    FLOP_count = 0
    steps = []
    # pivots loop loops n_eq-1 times because the matrix will be upper
    # triangular by the time we have reached the last pivot
    for i in range(n_eq-1):
        
        iswitch = max_piv_row(mat.copy(),i,scaling)
        if (iswitch != i):
            mat[i] , mat[iswitch] = mat[iswitch] , mat[i] # switch with larget pivot row
            #steps.append(Step(mat.copy(), f'Switch R{i+1} and R{iswitch+1} to get the maximum pivot.')) # log step
            #view_matrix(mat)

        for j in range(i+1,n_eq): # elimination loop

            if round(mat[j][i],4) == 0: continue

            multiplier = mat[j][i]/mat[i][i]
            FLOP_count+=1
            # looping over one row to carry out elimination (including constants)
            for k in range(i,n_eq+1):
                mat[j][k] = mat[j][k] - multiplier*mat[i][k]
                FLOP_count+=2
            #steps.append(Step(mat.copy(),f'R{j+1} <- R{j+1}-({round(multiplier,4)})R{i+1}')) # log step
            #view_matrix(mat)

    # reverse pivot loop
    for i in range(n_eq-1, -1, -1):

        if mat[i][i] == 0: continue # no pivot which means it's a free variable, move to next pivot

        if (round(mat[i][i],4) != 1):
            piv = mat[i][i]
            for j in range(i,n_eq+1): # normalise the row by the pivot to make it = 1
                mat[i][j] = mat[i][j]/piv
                FLOP_count+=1
            #steps.append(Step(mat.copy(), f'Divide R{i+1} by {round(mat[i][i],4)}.')) #log step
            #view_matrix(mat)

        # in the backward elimination, only the pivot column is eliminated and the constants column is changed.
        # the rest of the columns remain unchanged because we will be subtracting zero from them
        for j in range(i-1, -1, -1):
            multiplier = mat[j][i]
            mat[j][i] = 0
            mat[j][n_eq] = mat[j][n_eq]-multiplier*mat[i][n_eq]
            #steps.append(Step(mat.copy(),f'R{j+1} <- R{j+1}-({round(mat[j][i],4)})R{i+1}')) # log step
            #view_matrix(mat)

    return mat, steps, FLOP_count


def backward_substitution(mat):

    n_eq = len(mat)

    # gauss elimination makes all zero rows at the bottom,
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
        for j in range(i+1,n_eq): sol[i] -= sol[j]*mat[i][j]
        sol[i] /= mat[i][i]

    return sol, infinitesol



A = [
    [10,-7,0,7],
    [-3,2.099,6,3.901],
    [5,-1,5,6]
]

B, steps, flops = gauss_elim(A)

# make each individual step have a separate matrix
for step in steps:
    print(step.description, '\n')
    view_matrix(step.matrix)

sol,infinite = backward_substitution(B)
for elem in sol:
    print(round(elem,4))
