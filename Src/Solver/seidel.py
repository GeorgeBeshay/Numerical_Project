# Seidel with flops
from numpy import zeros
import math

def signif(x, digits=6):
    if x == 0 or not math.isfinite(x):
        return x
    digits -= math.ceil(math.log10(abs(x)))
    return round(x, digits)


def seidel(A, b, N = 50, x = None, max_error = 0.0000001, precision = 10):
    seidelSteps = ""
    seidelSteps += "N = " + str(N) + " , max_error = " + str(max_error)+"\n"  # do you want this
    if N==0:
        N = 50
    if precision==0:
        precision = 10
    if max_error==0:
        max_error = 0.0000001
    # Create an initial guess if not given
    if x is None:
        x = zeros(len(A[0]))
    x_new = x

    col = len(A[0])
    n = 0
    relative_error = 100 # any large number to make it enter the loop
    for i in range (col):
        if A[i][i] == 0:
            seidelSteps = "Can not solve using Seidel"
            return seidelSteps


    while n < N and relative_error > max_error:
        seidelSteps += "============================= The "+ str(n)+ " Iteration =============================\n"
        seidelSteps += 'intial X = \n'
        seidelSteps += str(x)+"\n"
        n += 1
        for i in range (col):
            sum = 0
            equation = ''
            calc = ''
            current_x = x[i] # this variable is used to store current x for error calc
            for j in range (col):
                if i != j:
                    equation = equation + ' - A['+str(i) +']['+ str(j)+ '] * x[' + str(j)+ ']'
                    calc = calc + ' - '+ str(A[i][j]) + ' * ' + str(x[j])
                    sum = signif(sum + A[i][j] * x[j] , precision)

            x_new[i] = signif((b[i] - sum) / A[i][i], precision)
            if i == 0:
                relative_error = (abs((x_new[i]-current_x)/x_new[i])) * 100
            elif (abs(x_new[i]-current_x)/x_new[i]) * 100 > relative_error:
                relative_error = (abs((x_new[i]-current_x)/x_new[i])) * 100

            seidelSteps += 'x_new[' + str(i) + '] = (b['+ str(i) + ']'+ equation + ') /  A['+str(i) +']['+ str(i)+ '] = ('+ str(b[i]) + calc + ') / ' + str(A[i][i])+ ' = ' + str(x_new[i]) + "\n"
        seidelSteps += "++++++++++++++++++++++++++++++++++++++++\n"
        seidelSteps += "MAX RELATIVE ERROR = " + str(relative_error)+"\n"
        seidelSteps += "++++++++++++++++++++++++++++++++++++++++\n"
        seidelSteps += 'X after iteration = \n'
        seidelSteps += str(x) + "\n"
    seidelSteps += "============================= FINISHED =============================\n"
    seidelSteps += "Final X: \n"
    seidelSteps += str(x)+"\n"

    return seidelSteps

#------------test--------------

A = [[1,3,2,4,-3],[2,6,0,-1,-2],[0,0,6,2,-1], [1,3,-1,4,2],[0,0,0,0,0]]
b = [-7,0,12,-6,0]
# guess = [1.0,0.0,1.0]
N = None
seidelSteps = seidel(A, b, N=50, x=None, precision=10,max_error=0.05)
print(seidelSteps)
# sol = seidel(A,b,N=25,x=guess)




