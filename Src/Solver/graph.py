import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from math import *


def f(func,x):
        return eval(func)


def showGrpah(methodName, params):
        
        if methodName == "Bisection" or methodName == "False-Position":
                # parms = [func , xl, xu]
                func = params[0]
                xl = params[1]
                xu = params[2]
                plt.figure()
                xlist = np.linspace(xl , xu , num=1000)
                ylist = f(func,xlist)
                plt.axvline(xl, color='red',label= "xl")
                plt.axvline(xu, color='green',label= "xu")
                plt.plot(xlist,ylist,label= "f(x)")
                plt.axhline(y=0, color='black')
                plt.legend()
                plt.title("Plotting")
                plt.xlabel("x")
                plt.ylabel("f(x)")
                plt.show()
        elif  methodName == "Fixed point":
                # parms = [g_of_x , xi, x]
                g_of_x = params[0]
                xi = params[1]
                x = params[2]
                plt.figure()
                if x > xi:
                        xlist = np.linspace(xi , x*2 , num=1000)
                else:
                        xlist = np.linspace(x*2 , xi , num=1000)
                ylist = f(g_of_x,xlist)
                plt.plot(xlist,xlist, label="y = x")
                plt.plot(xlist,ylist,label= "g(x)")
                plt.axhline(y=0, color='black')
                plt.legend()
                plt.title("Plotting")
                plt.xlabel("x")
                plt.ylabel("g(x)")
                plt.show()
        elif methodName == "Newton-Raphson":
                # parms = [func ,xi, x, derfunc]
                func = params[0]
                xi = params[1]
                x = params[2]
                derfunc = params[3]
                plt.figure()
                if x > xi:
                        xlist = np.linspace(xi , x*2 , num=1000)
                else:
                        xlist = np.linspace(x*2 , xi , num=1000)
                print(xlist)
                ylist = f(func,xlist)
                yderlist = f(derfunc, xlist)
                plt.plot(xlist,ylist,label= "f(x)")
                plt.plot(xlist,yderlist,label= "f'(x)")
                plt.axhline(y=0, color='black')
                plt.legend()
                plt.title("Plotting")
                plt.xlabel("x")
                plt.ylabel("f(x)")
                plt.show()
        elif methodName == "Secant-Method":
                # parms = [func , x0 , x1 , x]
                func = params[0]
                x0 = params[1]
                x1 = params[2]
                x = params[3]
                plt.figure()
                mx = max(x0,x1,x)
                mini = min(x0,x1,x)
                xlist = np.linspace(mini,mx, num=1000)
                ylist = f(func,xlist)
                plt.plot(xlist,ylist,label= "f(x)")
                plt.axhline(y=0, color='black')
                plt.legend()
                plt.title("Plotting")
                plt.xlabel("x")
                plt.ylabel("f(x)")
                plt.show()

showGrpah("Bisection", ["x**2-4*x+3",0.1,2.6])
# showGrpah("False-Position", ["x**3-x-1",1,2])
# showGrpah("Fixed point", ['3/(x-2)',0,-1])
# showGrpah("Newton-Raphson", ["x**3 - 0.165 * x**2 + 3.993 * 10**(-4)" , 0.05 ,  0.06238, "3*x**2 - 0.33*x"])
# showGrpah("Newton-Raphson", ["np.exp(-x)-x" , 0 , 0.567143165, "-1 - np.exp(-x)"])

# showGrpah("Fixed point", ['np.exp(-x)',0,0.567147])
# showGrpah("Secant-Method", ["x**3-x**2-10*x+7" , 3, 4,3.35746])
# showGrpah("Secant-Method", ["np.exp(-x)-x" , 0, 1,0.567143])
# showGrpah("False-Position", ["x**4+3*x-4",0,3])
# showGrpah("Bisection", ["x**4+3*x-4",0,3])
