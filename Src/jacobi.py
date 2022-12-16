# This is Jacobi with flops
import copy
def jacobi(A,b,N,x=None):
    # Create an initial guess if not given 
    flops = 0
    if x is None:
        print("HEREREEE")
        x = [0] * len(A)

    x_new = [0]* len(A)

    x_new = copy.deepcopy(x)
    col = len(A[0])
    for n in range (N):
        print("============================= The "+ str(n)+ " Iteration =============================")
        print('intial X = ')
        print(x)
        for i in range (col):
            sum = 0
            count = 0
            equation = ''
            calc = ''
            for j in range (col):
                if i != j:
                    if count == 0: #baaaad
                       flops += 1
                    else:
                        flops += 2
                    count += 1
                    equation = equation + ' - A['+str(i) +']['+ str(j)+ '] * x[' + str(j)+ ']'
                    calc = calc + ' - '+str(A[i][j]) + ' * ' +str(x[j])
                    sum = sum + A[i][j] * x[j]

            x_new[i] = (b[i] - sum) / A[i][i]
            flops+=2

            print('x_new[' + str(i) + '] = (b['+ str(i) + ']'+ equation + ') /  A['+str(i) +']['+ str(i)+ '] = ('
            + str(b[i]) + calc + ') / ' + str(A[i][i])+ ' = ' + str(x_new[i]))
            
            print('flops: ')
            print(flops)
        x = copy.deepcopy(x_new)
        print('X after iteration = ')
        print(x)
    return x, flops
# ----------test------------
# A = [[2.77,1.0,3.0],[5.0,7.0,4.0],[1.0,1.0,1.0]]
# b =[11.0,13.0,7.0]
# guess = [1.0,1.0,1.0]

# A = [[5,-2,3],[-3,9,1],[2,-1,-7]]
# b= [-1,2,3]
# guess = None

# sol, flops = jacobi(A,b,N=6,x=guess)

# print ("A:")
# print(A)

# print ("B:")
# print(b)

# print('Final X: ')
# print(sol)

# print('Total number of flops: ')
# print(flops)