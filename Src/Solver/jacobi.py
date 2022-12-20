# This is Jacobi 
import copy
import math

def signif(x, digits=6):
    if x == 0 or not math.isfinite(x):
        return x
    digits -= math.ceil(math.log10(abs(x)))
    return round(x, digits)

def jacobi(A , b , N, x , max_error , precision ):
    jacSteps = ""
    jacSteps += "N = " + str(N) + " , max_error = " + str(max_error) + "\n"
    if N==0 :
        N = 50
    if precision==0:
        precision = 10
    if max_error==0:
        max_error = 0.0000001
    x_new = [0]* len(A)

    x_new = copy.deepcopy(x)

    col = len(A[0])
    n = 0
    relative_error = 100 # any large number to make it enter the loop
    for i in range (col):
        if A[i][i] == 0:
            jacSteps = "Can not solve using Jacobi"
            return jacSteps

    while n < N and relative_error > max_error:
        jacSteps += "============================= The "+ str(n)+ " Iteration =============================\n"
        jacSteps += "intial X = \n" 
        jacSteps += str(x) +"\n" 
        n += 1
        for i in range (col):
            sum = 0
            equation = ''
            calc = ''
            for j in range (col):
                if i != j:
                    equation = equation + ' - A['+str(i) +']['+ str(j)+ '] * x_old[' + str(j)+ ']'
                    calc = calc + ' - '+str(A[i][j]) + ' * ' + str(x[j])
                    sum = signif(sum + A[i][j] * x[j], precision)

            x_new[i] = signif((b[i] - sum) / A[i][i] , precision)
            if x_new[i]!=0:
                if i == 0:
                    relative_error = (abs((x_new[i]-x[i])/x_new[i])) * 100
                elif (abs(x_new[i]-x[i])/x_new[i]) * 100 > relative_error:
                    relative_error = (abs((x_new[i]-x[i])/x_new[i])) * 100
            jacSteps += 'x_new[' + str(i) + '] = (b['+ str(i) + ']'+ equation + ') /  A['+str(i) +']['+ str(i)+ '] = ('+ str(b[i]) + calc + ') / ' + str(A[i][i])+ ' = ' + str(x_new[i]) +"\n"
        jacSteps += "++++++++++++++++++++++++++++++++++++++++\n"
        jacSteps +="MAX RELATIVE ERROR = " + str(relative_error) + "\n"
        jacSteps +="++++++++++++++++++++++++++++++++++++++++\n" 
        x = copy.deepcopy(x_new)
        jacSteps +='X after iteration = \n'
        jacSteps += str(x) +"\n"
    jacSteps += "============================= FINISHED =============================\n"
    jacSteps +='Final X = \n'
    jacSteps += str(x) +"\n"

   

    return jacSteps
# ----------test------------
# A = [[2.77,1.0,3.0],[5.0,7.0,4.0],[1.0,1.0,1.0]]
# b =[11.0,13.0,7.0]
# guess = [1.0,1.0,1.0]
# A=[[2,6],[1,3]]
# b=[7,5]
# A = [[5,-2,3],[-3,9,1],[2,-1,-7]]
# b= [-1,2,3]
# guess = None

# jacSteps = jacobi(A,b,N=6,x=guess , precision=5)
# print(jacSteps)
# print("============================= FINISHED =============================")
# print ("A:")
# print(A)

# print ("B:")
# print(b)

# print('Final X: ')
# print(sol)

