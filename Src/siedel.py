# Seidel by trying jacobi with flops

from numpy import zeros

def seidel(A,b,N=25,x=None):
    # Create an initial guess if not given                                                                                                          
    flops = 0
    if x is None:
        x = zeros(len(A[0]))

    x_new = x
    col = len(A[0])
    for n in range (N):
        x = x_new
        print('X = ')
        print(x)
        for i in range (col):
            print('i = '+ str(i))
            sum = 0
            count = 0
            for j in range (col):
                if i != j:
                    if count == 0: #baaaad
                       flops += 1
                    else:
                        flops += 2
                    count += 1
                    sum = sum + A[i][j] * x_new[j]
                    print('A[i][j] * x[j] = '+str(A[i][j]) +'*'+str (x[j])+ ' = '+str(A[i][j] * x[j]))
                   
                    print('flops: ')
                    print(flops)
            x_new[i] = (b[i] - sum) / A[i][i]
            flops+=2
            print('x_new[' + str(i) + '] = ' + str(x_new[i]))
            print('flops: ')
            print(flops)

        
    return x,flops

#------------test--------------

# A = [[2.77,1.0,3.0],[5.0,7.0,4.0],[1.0,1.0,1.0]]
# b =[11.0,13.0,7.0]
# guess = [1.0,1.0,1.0]

# #sol = seidel(A,b,N=25,x=guess)

# sol,flops = seidel(A,b,N=6,x=guess)
# print ("A:")
# # pprint(A)
# # to print the 2D matrix in a nice way
# print(A)

# print ("B:")
# print(b)

# print('X: ')
# print(sol)
# print('flops: ')
# print(flops)