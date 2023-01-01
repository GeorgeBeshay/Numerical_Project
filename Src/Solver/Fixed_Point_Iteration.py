# Fixed Point Iteration - Method Module
# --------------------- Separator ---------------------
import math
from sympy import *
from tabulate import tabulate
import numpy as np
from math import *
# --------------------- Separator ---------------------


def roundSig(x, digits=10):
    if x == 0 or not math.isfinite(x):
        return x
    digits -= math.ceil(math.log10(abs(x)))
    return round(x, digits)


def FPI(f_of_x: str, g_of_x: str, x0: float = 0, Es: float = 10 ** -5, max_iter: int = 50, digits=10):
    if max_iter == 0:
        max_iter = 50
    if Es == 0:
        Es = 10 ** -5
    if digits == 0:
        digits = 10
    # --------------------- Separator ---------------------
    table = []
    xr = x0
    xrOld: float
    Ea = 0
    startFlag = True
    iter_count = 0
    #x = symbols("x")
    def g_x(func,x):
        f = eval(func)
        return f
    # --------------------- Separator ---------------------
    while (Ea > Es or startFlag) and iter_count <= max_iter:
        startFlag = False
        xrOld = xr
        
        xr = roundSig(g_x(g_of_x,xrOld), digits)
        if xr != 0:
            Ea = abs((xr - xrOld) / xr) * 100
        table.append([iter_count, xr, Ea])
        iter_count += 1
    # --------------------- Separator ---------------------
    return "x(i+1) = g(xi)\n" + tabulate(table, headers=['It Num', 'xi', 'Ea %']),xr
# --------------------- Separator ---------------------


# print(FPI('x**2-2*x-3', '3/(x-2)'))             # Remove this
ans,x=FPI('x**2-2*x-3', '3/(x-2)',0, 0.0001,20,6)
print(ans)
print(x)