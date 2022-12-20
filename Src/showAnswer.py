import Solver.Header as SH
import tkinter as tk
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
def getSolutionText(A,  B, METHOD_NAME, parameters):
    Ans = ""
    PRECISION = int(parameters[0].get())
    # ------------------------- Separator -------------------------
    if METHOD_NAME == 'Jacobi-Iteration':
        INIT_GUESS = [0 for i in range(len(A))]
        for i in range(len(A)):
            INIT_GUESS=float(parameters[1][i].get())
        IT_NUM=int(parameters[2].get())
        E_TOL=int(parameters[3].get())
        Ans = SH.JAC(A, B, IT_NUM, INIT_GUESS, E_TOL, PRECISION)

    elif METHOD_NAME == 'Gauss-Seidel':
        INIT_GUESS = [0 for i in range(len(A))]
        for i in range(len(A)):
            INIT_GUESS = float(parameters[1][i].get())
        IT_NUM = int(parameters[2].get())
        E_TOL = int(parameters[3].get())
        Ans = SH.SEIDAL(A, B, IT_NUM, INIT_GUESS, E_TOL, PRECISION)

    elif METHOD_NAME == 'Gauss-Jordan':
        SC_FLAG= bool(parameters[1].get())
        Ans = SH.GJE(A, SC_FLAG, PRECISION)

    elif METHOD_NAME == 'Gauss Elimination':
        SC_FLAG = bool(parameters[1].get())
        Ans = SH.GE(A, SC_FLAG, PRECISION)

    elif METHOD_NAME == 'LU Crout Form':
        Ans = SH.LU_CR(A, PRECISION)

    elif METHOD_NAME == 'LU Doolittle Form':#scaling
        SC_FLAG = bool(parameters[1].get())
        Ans = SH.LU_D(A, B, SC_FLAG, PRECISION)

    elif METHOD_NAME == 'LU Cholesky Form':
        Ans = SH.LU_CH(A, PRECISION)

    else:
        Ans = 'ERROR: INVALID SOLVING METHOD'
    # ------------------------- Separator -------------------------
    return Ans


def showAnswer(A,  B, METHOD_NAME, parameters):
    # ------------------------- Separator -------------------------
    Ans = getSolutionText(A,  B, METHOD_NAME, parameters)
    # ------------------------- Separator -------------------------
    answerWindow = tk.Tk()
    answerWindow.title('Application Answer Window')
    answerWindow.geometry('1200x600')
    for i in range(24):
        answerWindow.columnconfigure(i, weight=1)
        answerWindow.rowconfigure(i, weight=1)
    answerWindow.config(bg='#0F3D3E')

    TitleFrame = tk.Frame(answerWindow, borderwidth=5, relief='solid')
    TitleFrame.grid(row=0, column=8, columnspan=8, sticky='news')
    TitleFrame.columnconfigure(0, weight=1)
    TitleFrame.rowconfigure(0, weight=1)
    Title = tk.Label(TitleFrame, text=f"Solving using: {METHOD_NAME}", font='Arial 18', bg='#22A39F')
    Title.grid(row=0, column=0, sticky='news')

    answerFrame = tk.Frame(answerWindow, borderwidth=5, relief='solid')
    answerFrame.grid(row=4, rowspan=18, column=4, columnspan=16, sticky='news')
    answerFrame.columnconfigure(0, weight=1)
    answerFrame.rowconfigure(0, weight=1)
    answerBody = tk.Label(answerFrame, text=Ans, font='Arial 15', bg='#22A39F')
    answerBody.grid(row=0, column=0, sticky='news')

    return answerWindow
    # ------------------------- Separator -------------------------


# The following code is used for testing the module, should be removed after finishing.
showAnswer(None, None, 'Method name', None, None, None, None, None, None).mainloop()
