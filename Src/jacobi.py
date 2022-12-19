# This is Jacobi with flops
import copy

def jacobi(A , b , N = 50 , x = None , max_error = 0.001, precision = 10):

    print("N = " + str(N) + " , max_error = " + str(max_error))
    # Create an initial guess if not given 
    flops = 0
    if x is None:
        x = [0] * len(A)

    x_new = [0]* len(A)

    x_new = copy.deepcopy(x)

    col = len(A[0])
    n = 0
    relative_error = 100 # any large number to make it enter the loop

    while n < N and relative_error > max_error:
        print("============================= The "+ str(n)+ " Iteration =============================")
        print('intial X = ')
        print(x)
        n += 1
        for i in range (col):
            sum = 0
            count = 0
            equation = ''
            calc = ''
            for j in range (col):
                if i != j:
                    if count == 0: 
                       flops += 1
                    else:
                        flops += 2
                    count += 1
                    equation = equation + ' - A['+str(i) +']['+ str(j)+ '] * x_old[' + str(j)+ ']'
                    calc = calc + ' - '+str(A[i][j]) + ' * ' +str(x[j])
                    sum = sum + A[i][j] * x[j]

            x_new[i] = round((b[i] - sum) / A[i][i] , precision)
            flops+=2
            if i == 0:
                relative_error = (abs((x_new[i]-x[i])/x_new[i])) * 100
            elif (abs(x_new[i]-x[i])/x_new[i]) * 100 > relative_error:
                relative_error = (abs((x_new[i]-x[i])/x_new[i])) * 100
            print('x_new[' + str(i) + '] = (b['+ str(i) + ']'+ equation + ') /  A['+str(i) +']['+ str(i)+ '] = ('
            + str(b[i]) + calc + ') / ' + str(A[i][i])+ ' = ' + str(x_new[i]))
            
            print('flops: ')
            print(flops)
        print("++++++++++++++++++++++++++++++++++++++++")
        print("MAX RELATIVE ERROR = " + str(relative_error))
        print("++++++++++++++++++++++++++++++++++++++++")    
        x = copy.deepcopy(x_new)
        print('X after iteration = ')
        print(x)
    return x, flops
# ----------test------------
A = [[2.77,1.0,3.0],[5.0,7.0,4.0],[1.0,1.0,1.0]]
b =[11.0,13.0,7.0]
guess = [1.0,1.0,1.0]

# A = [[5,-2,3],[-3,9,1],[2,-1,-7]]
# b= [-1,2,3]
# guess = None

sol, flops = jacobi(A,b,N=6,x=guess , max_error= 0.1, precision=5)
print("============================= FINISHED =============================")
# print ("A:")
# print(A)

# print ("B:")
# print(b)

print('Final X: ')
print(sol)

print('Total number of flops: ')
print(flops)