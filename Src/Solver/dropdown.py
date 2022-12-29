import tkinter as tk
from tkinter import ttk
from numberCheck import *
import Src.Solver.showAnswer as show
# from jacobi import *
# Window



class Window:

    def __init__(self, master):
        menubar = tk.Menu(master)
        mainMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Method', menu=mainMenu)
        mainMenu.add_command(label='Solve System of linear equation', command= lambda: self.SLE())
        mainMenu.add_command(label='Find root of equation', command=lambda :self.findRoot())
        root.config(menu=menubar)
        self.mainFrame = tk.LabelFrame(
            master, text="", padx=5, pady=5, borderwidth=0)
        self.mainFrame.grid(row=0, padx=5)

    def findRoot(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()
        selected = tk.StringVar()
        methods = [
            "Bisection",
            "False-Position",
            "Fixed point",
            "Newton-Raphson",
            "Secant-Method"
        ]
        optionMenu = ttk.OptionMenu(
            self.mainFrame, selected, "Bisection", *methods)
        optionMenu.grid(row=0, column=1 ,padx=5, pady=5)
        EqLable = tk.Label(
            self.mainFrame, text="Equation")
        EqLable.grid(row=1, column=0 ,padx=5, pady=5)
        Eq = tk.Entry(self.mainFrame, width=40)
        Eq.grid(row=1, column=1,padx=5, pady=5)
        b = tk.Button(self.mainFrame, text="Enter", command= lambda: self.createParam(selected.get(),Eq))
        b.grid(row=1, column=3 ,padx=5, pady=5)

    def createParam(self, method,Eq):
        pf=tk.LabelFrame(self.mainFrame, text="Parameters",padx=5, pady=5)
        pf.grid(row=2, column=1)
        parameters = []
        parameters.append(Eq)
        precision = tk.Label(pf, text="Precision")
        precision.grid(row=1, column=0, padx=5, pady=5)
        prec = tk.Entry(pf, width=7)
        prec.grid(row=1, column=1, padx=5, pady=5)
        parameters.append(prec)

        iteration = tk.Label(pf, text="Iteration")
        iteration.grid(row=2, column=0, padx=5, pady=5)
        itr = tk.Entry(pf, width=7)
        itr.grid(row=2, column=1, padx=5, pady=5)
        parameters.append(itr)

        eps = tk.Label(pf, text="EPS")
        eps.grid(row=3, column=0, padx=5, pady=5)
        e = tk.Entry(pf, width=7)
        e.grid(row=3, column=1, padx=5, pady=5)
        parameters.append(e)

        if method=="Bisection" or method=="False-Position":
            xl = tk.Label(pf, text="Xl")
            xl.grid(row=4, column=0, padx=5, pady=5)
            xlower = tk.Entry(pf, width=7)
            xlower.grid(row=4, column=1, padx=5, pady=5)
            parameters.append(xlower)

            xu = tk.Label(pf, text="Xu")
            xu.grid(row=4, column=2, padx=5, pady=5)
            xupper = tk.Entry(pf, width=7)
            xupper.grid(row=4, column=3, padx=5, pady=5)
            parameters.append(xupper)
        elif method =="Fixed point":
            x0 = tk.Label(pf, text="Initial x")
            x0.grid(row=4, column=0, padx=5, pady=5)
            xi = tk.Entry(pf, width=7)
            xi.grid(row=4, column=1, padx=5, pady=5)
            parameters.append(xi)
            g = tk.Label(pf, text="g(x)")
            g.grid(row=4, column=2, padx=5, pady=5)
            gx = tk.Entry(pf, width=7)
            gx.grid(row=4, column=3, padx=5, pady=5)
            parameters.append(gx)
        elif method=="Newton-Raphson":
            x0 = tk.Label(pf, text="Initial x")
            x0.grid(row=4, column=0, padx=5, pady=5)
            xi = tk.Entry(pf, width=7)
            xi.grid(row=4, column=1, padx=5, pady=5)
            parameters.append(xi)
        elif method=="Secant-Method":
            x0 = tk.Label(pf, text="X0")
            x0.grid(row=4, column=0, padx=5, pady=5)
            xi = tk.Entry(pf, width=7)
            xi.grid(row=4, column=1, padx=5, pady=5)
            parameters.append(xi)

            x1 = tk.Label(pf, text="X1")
            x1.grid(row=4, column=2, padx=5, pady=5)
            xi1 = tk.Entry(pf, width=7)
            xi1.grid(row=4, column=3, padx=5, pady=5)
            parameters.append(xi1)
        solve = tk.Button(pf, text="Solve", command=lambda:
                          show.getSolution2(method,parameters))
        solve.grid(row=5, column=4)


    def SLE(self):

        for widget in self.mainFrame.winfo_children():
            widget.destroy()

        selected = tk.StringVar()
        methods = [
            "Gauss Elimination",
            "Gauss-Jordan",
            "Gauss-Seidel",
            "Jacobi-Iteration"
        ]
        optionMenu = ttk.OptionMenu(
            self.mainFrame, selected, "Gauss Elimination", *methods)
        optionMenu.grid(row=0, column=0)
        menu = optionMenu["menu"]
        sublist1 = tk.Menu(menu, tearoff=False)
        sublist1.add_command(label="Doolittle Form",
                            command=lambda: selected.set("LU Doolittle Form"))
        sublist1.add_command(label="Crout Form",
                                command=lambda: selected.set("LU Crout Form"))
        sublist1.add_command(label="Cholesky Form",
                            command=lambda: selected.set("LU Cholesky Form"))
        menu.add_cascade(label="LU Decomposition", menu=sublist1)

        numberEFrame = tk.LabelFrame(
            self.mainFrame, text="", padx=5, pady=5, borderwidth=0)
        numberEFrame.grid(row=2, column=0)
        nE = tk.Label(
            numberEFrame, text="The number of equations in the System")
        nE.grid(row=2, column=0)
        numberEquations = tk.Entry(numberEFrame, width=5)
        numberEquations.grid(row=2, column=1)
        b = tk.Button(numberEFrame, text="Enter", command=lambda:self.CreateEntry(numberEquations,selected))
        b.grid(row=2, column=2)
        # h = tk.Scrollbar(mainFrame, orient='vertical')
        # h.grid(row=4, column=0, columnspan=20, sticky='ns')


    def getMatrices(self,namR, num, parameters,selected):
        matA = [[0 for i in range(num)]for j in range(num)]
        for i in range(num):
            for j in range(num):
                isfloat,coef= isFloat(namR[i][j])
                if isfloat:
                    matA[i][j] = coef
        matB = [0 for i in range(num)]
        for i in range(num):
            isfloat, coef = isFloat(namR[i][num])
            if isfloat:
                matB[i] = coef

        print("A = ")
        print(matA)
        print("B = ")
        print(matB)
        print("scalable = ")
        print(parameters[0].get())
        method = selected.get()
        show.getSolution1(matA, matB, method, parameters)
        # Call george's function give it A, B, parameters

    def CreateEntry(self,numberEquations,selected):

        create, num = isIntger(numberEquations)
        if create == True:
            frame = tk.LabelFrame(
                self.mainFrame, text="Fill the system of linear Equations", padx=5, pady=5)
            frame.grid(row=3, column=0, padx=10, pady=10)
            namx = [tk.Label(frame) for i in range(num)]
            for j in range(num):
                t = "x" + str(j)
                namx[j].config(text=t)
                namx[j].grid(row=0, column=j)

            namR = [[tk.Entry(frame, width=4)
                     for i in range(num + 1)] for j in range(num)]
            for i in range(num):
                for j in range(num+1):
                    namR[i][j].grid(row=i+1, column=j)

            # More paramters inputs
            frame1 = tk.LabelFrame(
                self.mainFrame, text="More paramters inputs", padx=5, pady=5)
            frame1.grid(row=3, column=10, padx=10, pady=10)
            parameters = []
            precision = tk.Label(frame1)
            precision.configure(text="Precision")
            precision.grid(row=1, column=0, padx=5, pady=5)
            prec=tk.Entry(frame1, width=5)
            prec.grid(row=1, column=1, padx=5, pady=5)
            parameters.append(prec)

            method = selected.get()
            if method == "Gauss Elimination" or method == "Gauss-Jordan" or method == "LU Doolittle Form":
                scalable = tk.IntVar()
                scale = tk.Checkbutton(frame1, text="Scaling", variable=scalable)
                scale.grid(row=0, column=0, padx=5, pady=5)
                parameters.append(scalable)
            elif method == "Gauss-Seidel" or method == "Jacobi-Iteration":
                initialGuess = tk.Label(frame1)
                initialGuess.configure(text="Initial Guess")
                initialGuess.grid(row=2, column=0, padx=5, pady=5)
                frameXs = tk.LabelFrame(frame1, borderwidth=0)
                frameXs.grid(row=3, column=0)
                xs = [tk.Label(frameXs) for i in range(num)]
                for j in range(num):
                    t = "x" + str(j)
                    xs[j].config(text=t)
                    xs[j].grid(row=0, column=j)
                xsEntry = [tk.Entry(frameXs, width=4) for i in range(num)]
                for i in range(num):
                    xsEntry[i].grid(row=1, column=i)
                parameters.append(xsEntry)
                iterations = tk.Label(frame1)
                iterations.configure(text="Number of Iterations")
                iterations.grid(row=5, column=0, padx=5, pady=5)
                N = tk.Entry(frame1, width=5)
                N.grid(row=5, column=1, padx=5, pady=5)
                parameters.append(N)
                relativeError = tk.Label(frame1)
                relativeError.configure(text="Absolute relative Error")
                relativeError.grid(row=6, column=0, padx=5, pady=5)
                tol = tk.Entry(frame1, width=5)
                tol.grid(row=6, column=1, padx=5, pady=5)
                parameters.append(tol)


            b2 = tk.Button(frame, text="Solve",
                           command=lambda: self.getMatrices(namR, num, parameters, selected))
            # , command = takeCof(num, namR) )
            b2.grid(row=num + 1, column=num)







root = tk.Tk()
window = Window(root)
root.title("Drop Down")
root.geometry("550x550")
#root.state("zoomed")
root.mainloop()
