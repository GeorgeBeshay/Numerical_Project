# -------------------- Imports --------------------
import LU_Decomposition_Calculator as LU_Calc
import numpy as np
# -------------------- Driver Code --------------------
A = [[1, 2, 3], [2, 20, 26], [3, 26, 70]]
LU_Calc.crout(A).showAns()
