from math import *

def signif(x, digits=6):
    if x == 0 or not isfinite(x):
        return x
    digits -=ceil(log10(abs(x)))
    return round(x, digits)

def function(f,x):
    return eval(f)

def bisection(f,xl,xu,N,EPS,percision):
    ans=''
    if N==0:
        N=50
    if EPS==0:
        EPS=10**-5
    if percision==0:
        percision = 10

    if (function(f,xl) * function(f,xu))>0:
        ans="No bracket"
        return ans

    if function(f,xl)==0:
        return str(xl)
    elif function(f,xu)==0:
        return str(xu)

    n=0
    relative_error=100
    xrold=0
    while n<N and relative_error > EPS:
        xr=signif((xu+xl)/2.0,percision)

        if xr!=0:
            relative_error = (abs((xr-xrold)/xr))*100

        test=function(f,xl) * function(f,xr)
        if test==0:
            ans += "Iteration " + str(n) + " :\n"
            ans += "xl = " + str(xl) + "\nxu = " + str(xu) + "\n"
            ans += "xr = (xu+xl)/2 = " + str(xr) + "\n"
            ans += "f(xr) = 0\n"
            ans += "Relative error = " + str(relative_error) + "\n"
            break
        ans += "Iteration " + str(n) + " :\n"
        ans += "xl = " + str(xl) + "\nxu = " + str(xu) + "\n"
        ans += "xr = (xu+xl)/2 = " + str(xr) + "\n"
        ans += "f(xr) ="+str(signif(function(f,xr),percision))+ "\n"
        if n>0:
            ans += "Relative error = " + str(relative_error) + "\n"
        if test>0:
            xl=xr
        else:
            xu = xr
        ans+="---------------------------------------------\n"
        xrold=xr
        n+=1

    return ans




#
# f="x**4+3*x-4"
#
# a=bisection(f,0,1,0,0,6)
# print(a)