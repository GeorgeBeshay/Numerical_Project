from sympy import *
from math import *
import numpy as np
def signif(x, digits=6):
    if x == 0 or not isfinite(x):
        return x
    digits -=ceil(log10(abs(x)))
    return round(x, digits)
# , dfunc 
def newton(func , xguess , EPS , maxit , precision):
    if maxit == 0:
        maxit = 50
    if EPS == 0: # error 
        EPS = 0.00001
    if precision == 0: # significant figures
        precision = 10
    if xguess is None:
        xguess = 0

    # the function
    def f(x):
        f = eval(func)
        return f

    # the derivative
    x = symbols("x")
    derfunc = diff(func , x)
    def dfunc(x):
        derf = eval(str(derfunc))
        return derf
    
    # Newton Raphson implementation
    newtonSteps = ""
    newtonSteps += "f(x) = " + str(func) + "\n"
    newtonSteps += "f'(x) = " + str(derfunc) + "\n"
    for n in range (maxit):
        newtonSteps += "\n====================== " + str(n) + " Iteration ======================\n"
        newtonSteps += "xold = " + str(xguess) + "\n"
        if dfunc(xguess) == 0:
            newtonSteps += "Division by zero has occurred. \nf'(x) cannot be zero\nThis might be because the f'(x) = 0 or the guess that you chose made the f'(x) = 0\n"
            break
        try:
            xnew = signif(xguess, precision) - signif(f(xguess), precision) / signif(dfunc(xguess), precision) 
        except TypeError:
            newtonSteps += "Cannot find the root because the derivative or the main function contain a negative number with nth root example: (-2)^(1/2)\n"
            break
        
        newtonSteps += "Absolute Error = abs(xnew - xold) = abs(" + str(xnew) + " - " + str(xguess) + ") = " + str(signif(abs(xnew - xguess),precision)) + "\n"
        if abs(xnew - xguess) < EPS:
            break
    
        newtonSteps += "xnew = xold - f(xold)/f'(xold) = " + str(signif(xguess, precision)) + " - " + str(signif(f(xguess), precision)) + " / " + str(signif(dfunc(xguess), precision)) + " = " + str(signif(xnew, precision)) + "\n"
        xguess = signif(xnew, precision)
    
    # after for loop
    try:
        signif(f(xnew), precision) # this is to check that we didn't break from the loop becasue of error
        newtonSteps += "\nTo check that x is a root:\n"
        newtonSteps += "f(" + str(signif(xnew, precision)) + ") = " + str(signif(f(xnew), precision)) + "\n"
        if f(xnew) <= EPS:
            newtonSteps += "\n-------------- Newton method has converged because f(x) is approximately equal to 0 --------------\n"
            newtonSteps += "x = " + str(signif(xguess, precision)) + "\n"
        else:
            newtonSteps += "f(xnew) is not near to zero\nx is not a root\n"
    except TypeError : # UnboundLocalError
        newtonSteps += ""
    return newtonSteps,xnew,str(derfunc)


# ------------------- test -------------------
# func = "x**3 - 0.165 * x**2 + 3.993 * 10**(-4)" # page 36 in part 1
# ans,xx,derf = newton(func, 0.05 , 0 , 3 , 4)
# print(ans)
# print(xx)
# print(derf)


# func = "exp(-x)-x" # page 54 in part 1
# ans = newton(func= func , xguess= 0 , EPS= 0, maxit= 5 , precision=10)
# print(ans)
# func = "0.5**x - x + 4" # trying an example with exponent
# ans = newton(func= func , xguess= 0 , EPS= 0, maxit= 0 , precision=6)
# print(ans)


# func = "x**2 - 2" # page 63 in part 1
# ans = newton(func= func , xguess= 1 , EPS= 0, maxit= 0 , precision=10)
# print(ans)


# func = "x**(1/3)" # sheet
# ans = newton(func= func , xguess= 0.1 , EPS= 0, maxit= 0 , precision=10)
# print(ans)