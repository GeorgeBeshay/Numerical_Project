from math import *


def signif(x, digits=6):
    if x == 0 or not isfinite(x):
        return x
    digits -= ceil(log10(abs(x)))
    return round(x, digits)


def func(f, x):
    return eval(f)


def secant(f, x0, x1, iterations, tol, precision):
    # f -> function to calculate its root
    # x0, x1 -> initial guess
    # iterations -> maximum number of iterations
    # tol -> absolute relative error
    steps = ""
    if iterations == 0:
        iterations = 50
    if tol == 0:
        tol = 10**-5
    if precision == 0:
        precision = 10
    if x0 == x1:
        return f"The initial gusses must be not equal\n"

    itr, relativeError = 0, 100
    while relativeError > tol and itr <= iterations:
        itr += 1
        x2 = signif(x1 - func(f, x1) * ((x1 - x0) /
                    (func(f, x1) - func(f, x0))), precision)
        relativeError = abs((x2 - x1) / x2) * 100

        steps += f"Iteration Number: {itr}\n\n"
        steps += f"X(i-1) = {x0}, f(X(i-1)) = {signif(func(f, x0))}\n"
        steps += f"X(i) = {x1}, f(X(i)) = {signif(func(f, x1))}\n"
        steps += f"X(i+1) = {x2}\n"
        steps += f"Relative Error = {relativeError}\n"
        steps += "----------------------------------------------------------------------\n\n"
        x0 = x1
        x1 = x2
    steps += f"The root is: {x2}\n\n"
    return steps


f = "x**3-x**2-10*x+7"

print(secant(f, 3, 4, 20, 10**-4, 6))
