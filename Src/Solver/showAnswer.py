# import Src.Solver.Header as SH
# from Src.Solver.Header import *

import Src.Solver.jacobi as JAC
import Src.Solver.seidel as SEIDEL
import Src.Solver.GaussMethods as GM
import Src.Solver.Crout as LU_CR
import Src.Solver.LUDoolittle as LU_D
import Src.Solver.Cholesky as LU_CH
import Src.Solver.bisectionMethode as BI
import Src.Solver.FalsePosition as FL
import Src.Solver.newton_raphson as NR
import Src.Solver.Fixed_Point_Iteration as FB
import Src.Solver.secantMethod as SC
import Src.Solver.graph as draw
import time

import tkinter as tk
from numberCheck import *
# Module is responsible for displaying the answer.
# Parameters:
# > Matrix A
# > MatrixB
# > Name
# > Precision
# > Num of iterations
# > Error Tolerance
# > Initial Guess
# > bool pivoting
# > bool scaling

# ------------------------- Separator -------------------------
def getSolution1(A,  B, METHOD_NAME, parameters):
    startTime = time.time_ns()
    Ans = ""
    PRECISION=0
    print(parameters[0])
    isInt, num = isIntger(parameters[0])
    if isInt:
        PRECISION = num
    # ------------------------- Separator -------------------------
    if METHOD_NAME == 'Jacobi-Iteration' or METHOD_NAME == 'Gauss-Seidel':
        INIT_GUESS = [0 for i in range(len(A))]
        for i in range(len(A)):
            isfloat, num = isFloat(parameters[1][i])
            if isfloat:
                INIT_GUESS[i] = num

        IT_NUM=0
        isInt, num = isIntger(parameters[2])
        if isInt:
            IT_NUM=num

        E_TOL=0
        isInt, num = isFloat(parameters[3])
        if isInt:
            E_TOL = num

        if METHOD_NAME == 'Jacobi-Iteration':
            Ans = JAC.jacobi(A, B, IT_NUM, INIT_GUESS, E_TOL, PRECISION)
        else:
            Ans = SEIDEL.seidel(A, B, IT_NUM, INIT_GUESS, E_TOL, PRECISION)

    elif METHOD_NAME == 'Gauss-Jordan':
        SC_FLAG= bool(parameters[1].get())
        try:
            Ans = GM.ans_gauss_jordan(A, B, SC_FLAG, PRECISION)
        except:
            Ans = 'Inconsistent System'

    elif METHOD_NAME == 'Gauss Elimination':
        SC_FLAG = bool(parameters[1].get())
        try:
            Ans = GM.ans_gauss(A, B, SC_FLAG, PRECISION)
        except:
            Ans = 'Inconsistent System'

    elif METHOD_NAME == 'LU Crout Form':
        try:
            Ans = LU_CR.ans_crout(A, B, PRECISION)
        except:
            Ans = f"Can't be solved using {METHOD_NAME}"

    elif METHOD_NAME == 'LU Doolittle Form':
        SC_FLAG = bool(parameters[1].get())
        Ans = LU_D.LU_Doolittle(A, SC_FLAG, PRECISION, B)

    elif METHOD_NAME == 'LU Cholesky Form':
        try:
            Ans = LU_CH.ans_cholesky(A, B, PRECISION)
        except:
            Ans = f"Can't be solved using {METHOD_NAME}"

    else:
        Ans = 'ERROR: INVALID SOLVING METHOD'
    # ------------------------- Separator -------------------------
    endTime = time.time_ns()
    runtime = (endTime - startTime) / (10 ** 6)
    Ans += f'\nruntime = {runtime} ms'
    showAnswer(Ans, METHOD_NAME)

def getSolution2(METHOD_NAME, parameters):
    startTime = time.time_ns()
    Ans = ""
    fun=parameters[0].get()

    PRECISION = 0
    isInt, num = isIntger(parameters[1])
    if isInt:
        PRECISION = num

    iteration = 0
    isInt, num = isIntger(parameters[2])
    if isInt:
        iteration = num

    eps = 0
    isf, num = isFloat(parameters[3])
    if isf:
        eps = num

    par=[]

    if METHOD_NAME == "Bisection" or METHOD_NAME == "False-Position":
        xl = 0
        isf, num = isFloat(parameters[4])
        if isf:
            xl = num
        xu = 0
        isf, num = isFloat(parameters[5])
        if isf:
            xu = num
        if METHOD_NAME == "Bisection":
            Ans+=BI.bisection(fun,xl,xu,iteration,eps,PRECISION)
        elif METHOD_NAME == "False-Position":
            Ans+= FL.false_position(fun,xl,xu,eps,iteration,PRECISION)
        par.append(fun)
        par.append(xl)
        par.append(xu)
    elif METHOD_NAME == "Fixed point":
        x0 = 0
        isf, num = isFloat(parameters[4])
        if isf:
            x0 = num
        g = parameters[5].get()
        Ans, x=FB.FPI(fun,g,x0,eps,iteration,PRECISION)
        par.append(g)
        par.append(x0)
        par.append(x)
    elif METHOD_NAME == "Newton-Raphson":
        x0 = 0
        isf, num = isFloat(parameters[4])
        if isf:
            x0 = num
        Ans , x, derf=NR.newton(fun,x0,eps,iteration,PRECISION)
        par.append(fun)
        par.append(x0)
        par.append(x)
        par.append(derf)
    elif METHOD_NAME == "Secant-Method":
        x0 = 0
        isf, num = isFloat(parameters[4])
        if isf:
            x0 = num
        x1 = 0
        isf, num = isFloat(parameters[5])
        if isf:
            x1 = num
        Ans,x=SC.secant(fun,x0,x1,iteration,eps,PRECISION)
        par.append(fun)
        par.append(x0)
        par.append(x1)
        par.append(x)
    endTime = time.time_ns()
    runtime = (endTime - startTime) / (10 ** 6)
    Ans += f'\nruntime = {runtime} ms'
    showAnswer(Ans, METHOD_NAME)
    draw.showGrpah(METHOD_NAME, par)

def showAnswer(Ans, METHOD_NAME):
    # ------------------------- Separator -------------------------
    answerWindow = tk.Tk()
    answerWindow.title('Application Answer Window')
    answerWindow.geometry('1200x600')
    for i in range(24):
        answerWindow.columnconfigure(i, weight=1)
        answerWindow.rowconfigure(i, weight=1)
    answerWindow.config(bg='#0F3D3E')
    answerWindow.state('zoomed')

    TitleFrame = tk.Frame(answerWindow, borderwidth=5, relief='solid')
    TitleFrame.grid(row=0, column=8, columnspan=8, sticky='news')
    TitleFrame.columnconfigure(0, weight=1)
    TitleFrame.rowconfigure(0, weight=1)
    Title = tk.Label(TitleFrame, text=f"Solving using: {METHOD_NAME}", font='Arial 18', bg='#22A39F')
    Title.grid(row=0, column=0, sticky='news')

    answerFrame = tk.Frame(answerWindow, borderwidth=5, relief='solid')
    answerFrame.grid(row=4, rowspan=18, column=4, columnspan=16, sticky='news')
    answerFrame.columnconfigure(0, weight=30)
    answerFrame.rowconfigure(0, weight=30)
    answerFrame.columnconfigure(1, weight=1)
    answerFrame.rowconfigure(1, weight=1)
    # answerBody = tk.Label(answerFrame, text=Ans, font='Arial 15', bg='#22A39F')
    answerBody = tk.Text(answerFrame, font='Arial 15', bg='#22A39F', wrap='none')
    answerBody.grid(row=0, column=0, sticky='news')

    scrollbarY = tk.Scrollbar(answerFrame, command=answerBody.yview)
    answerBody.config(yscrollcommand=scrollbarY.set)
    scrollbarY.grid(row=0, column=1, rowspan=1, sticky='news')

    scrollbarX = tk.Scrollbar(answerFrame, command=answerBody.xview, orient='horizontal')
    answerBody.config(xscrollcommand=scrollbarX.set)
    scrollbarX.grid(row=1, column=0, columnspan=1, sticky='news')

    answerBody.insert(tk.END, Ans)


    return answerWindow
    # ------------------------- Separator -------------------------


# The following code is used for testing the module, should be removed after finishing.
# showAnswer(None, None, 'Method name', [1]).mainloop()
