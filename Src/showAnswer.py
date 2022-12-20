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
def getSolutionText(A,  B, METHOD_NAME, PRECISION, IT_NUM, E_TOL, INIT_GUESS, PIV_FLAG, SC_FLAG):
    Ans = ""
    # ------------------------- Separator -------------------------
    if METHOD_NAME == 'Jacobi-Iteration':
        Ans = SH.JAC(A, B, IT_NUM, INIT_GUESS, E_TOL, PRECISION)
    elif METHOD_NAME == 'Gauss-Seidel':
        Ans = SH.SEIDAL(A, B, IT_NUM, INIT_GUESS, E_TOL, PRECISION)
    elif METHOD_NAME == 'Gauss-Jordan':
        Ans = SH.GJE(A, SC_FLAG)
    elif METHOD_NAME == 'Gauss Elimination':
        Ans = SH.GE(A, SC_FLAG)
    elif METHOD_NAME == 'LU Crout Form':
        Ans = SH.LU_CR()
    elif METHOD_NAME == 'LU Doolittle Form':
        Ans = SH.LU_D()
    elif METHOD_NAME == 'LU Cholesky Form':
        Ans = SH.LU_CH()
    else:
        Ans = 'ERROR: INVALID SOLVING METHOD'
    # ------------------------- Separator -------------------------
    return Ans


def showAnswer(A,  B, METHOD_NAME, PRECISION, IT_NUM, E_TOL, INIT_GUESS, PIV_FLAG, SC_FLAG):
    # ------------------------- Separator -------------------------
    Ans = getSolutionText(A,  B, METHOD_NAME, PRECISION, IT_NUM, E_TOL, INIT_GUESS, PIV_FLAG, SC_FLAG)
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
