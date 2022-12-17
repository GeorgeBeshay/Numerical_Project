from math import log10, floor
DEC_ROUND = 10
DISPLAY_ROUND = 4

# -------------------------------------------------------- UTILITY FUNCTIONS --------------------------------------------------------

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
                temp[i][j] = temp[i][j]/max_coeff # divide each element by largest element

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
            print(f'{round(j,DISPLAY_ROUND)}   ', end = '')
        print("\n")
    print('\n')

# -------------------------------------------------------- UTILITY FUNCTIONS --------------------------------------------------------


def gauss_elim(mat, scaling = False): 

    n_eq = len(mat)
    steps = []
    # pivots loop loops n_eq-1 times because the matrix will be upper
    # triangular by the time we have reached the last pivot
    for i in range(n_eq-1):

        iswitch = max_piv_row(mat.copy(),i,scaling)
        if (iswitch != i):
            mat[i] , mat[iswitch] = mat[iswitch] , mat[i] # switch with larget pivot row
            #steps.append(Step(mat.copy(), f'Switch R{i+1} and R{iswitch+1} to get the maximum pivot.')) # log step

        if (round(mat[i][i],DEC_ROUND) == 0): # if largest pivot is 0, skip this pivot and let substitution handle it
            mat[i][i] = 0
            continue

        for j in range(i+1,n_eq): # elimination loop
            
            if round(mat[j][i],DEC_ROUND) == 0: # if element is already 0, skip to next row
                mat[j][i] = 0
                continue

            multiplier = mat[j][i]/mat[i][i]
            # looping over one row to carry out elimination (including constants)
            for k in range(i,n_eq+1):
                mat[j][k] = mat[j][k] - multiplier*mat[i][k]

            #steps.append(Step(mat ,f'R{j+1} <- R{j+1}-({round(multiplier,4)})R{i+1}')) # log step
    
    return mat, steps



def gauss_jordan_elim(mat, scaling = False):

    n_eq = len(mat)
    steps = []
    # pivots loop loops n_eq-1 times because the matrix will be upper
    # triangular by the time we have reached the last pivot
    for i in range(n_eq-1):
        
        iswitch = max_piv_row(mat.copy(),i,scaling)
        if (iswitch != i):
            mat[i] , mat[iswitch] = mat[iswitch] , mat[i] # switch with larget pivot row
            #steps.append(Step(mat.copy(), f'Switch R{i+1} and R{iswitch+1} to get the maximum pivot.')) # log step
            #view_matrix(mat)

        if (round(mat[i][i],DEC_ROUND) == 0): continue # if largest pivot is 0, skip this pivot and let substitution handle it

        for j in range(i+1,n_eq): # elimination loop

            if round(mat[j][i],DEC_ROUND) == 0: continue # if element is already 0, skip to next row

            multiplier = mat[j][i]/mat[i][i]
            # looping over one row to carry out elimination (including constants)
            for k in range(i,n_eq+1):
                mat[j][k] = mat[j][k] - multiplier*mat[i][k]
            #steps.append(Step(mat.copy(),f'R{j+1} <- R{j+1}-({round(multiplier,4)})R{i+1}')) # log step
            #view_matrix(mat)

    # reverse pivot loop
    for i in range(n_eq-1, -1, -1):

        if round(mat[i][i],DEC_ROUND) == 0: continue # no pivot which means it's a free variable, move to next pivot

        if (round(mat[i][i],DEC_ROUND) == 1):
            mat[i][i] = 1
        else:
            piv = mat[i][i]
            for j in range(i,n_eq+1): # normalise the row by the pivot to make it = 1
                mat[i][j] = mat[i][j]/piv
            #steps.append(Step(mat.copy(), f'Divide R{i+1} by {round(mat[i][i],4)}.')) #log step
            #view_matrix(mat)

        # in the backward elimination, only the pivot column is eliminated and the constants column is changed.
        # the rest of the columns remain unchanged because we will be subtracting zero from them
        for j in range(i-1, -1, -1):

            if round(mat[j][i],DEC_ROUND) == 0: continue 
            multiplier = mat[j][i]

            for k in range (i,n_eq+1):
                if round(mat[i][k],DEC_ROUND) == 0: break # no change would happen
                mat[j][k] = mat[j][k]-multiplier*mat[i][k]
            #steps.append(Step(mat.copy(),f'R{j+1} <- R{j+1}-({round(mat[j][i],4)})R{i+1}')) # log step
            #view_matrix(mat)

    return mat, steps


def backward_substitution(mat):

    n_eq = len(mat)

    # gauss elimination makes all zero rows at the bottom,
    # so we loop over them with this boolean
    zeropivots = True 

    # if there are infinite solutions, we set all free variables to 1
    infinitesol = False
    sol = [1]*n_eq # initialize solution vector with 1's

    for i in range(n_eq-1, -1, -1):

        if zeropivots and round(mat[i][i],DEC_ROUND) == 0: 
            if round(mat[i][n_eq],DEC_ROUND) != 0:
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
    [1,1,-3,4],
    [2,1,-1,2],
    [3,2,-4,6]
]

B, steps = gauss_elim(A.copy())
#C, steps = gauss_jordan_elim(A.copy())

view_matrix(B)
#view_matrix(C)

sol,infinite = backward_substitution(B)
for elem in sol: print(round(elem,DISPLAY_ROUND))

print(f'\n{infinite}')
