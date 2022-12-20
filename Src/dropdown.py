import tkinter as tk
from tkinter import ttk
# from jacobi import *
# Window



class Window:

    def __init__(self, master):
        selected = tk.StringVar()

        methods = [
            "Gauss Elimination",
            "Gauss-Jodan",
            "Gauss-Seidel",
            "Jacobi-Iteration"
        ]
        optionMenu = ttk.OptionMenu(
            master, selected, "Gauss Elimination", *methods)
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

        def numberE(entr):
            isInt = True
            num = -1
            try:
                int(entr.get())
                entr.config(highlightthickness=0, bg="white")
                isInt = True
                num = int(entr.get())
            except ValueError:
                entr.config(highlightthickness=2, highlightbackground="red",
                            bg="red", highlightcolor="red")
                # , bg="red"
                isInt = False
            return isInt, num

        def isFloat(entr):
                isfloat = True
                num = -1
                try:
                    float(entr.get())
                    entr.config(highlightthickness=0, bg="white")
                    isfloat = True
                    num = float(entr.get())
                except ValueError:
                    if not entr.get():
                        num = 0
                        isfloat = True
                    else:
                        entr.config(highlightthickness=2, highlightbackground="red",
                                    bg="red", highlightcolor="red")
                        isfloat = False

                return isfloat, num


        def selectMethod():
            method = selected.get()
            if method == "Gauss Elimination":
                print("in Gauss-Elimimation")
            elif method == "Gauss-Jodan":
                print("in Gauss-Jodan")
            elif method == "LU Doolittle Form":
                print("in Doolittle Form")
            elif method == "LU Crout Form":
                print("in Crout")
            elif method == "LU Cholesky Form":
                print("in Cholesky")
            elif method == "Gauss-Seidel":
                print("in Seidel")
            elif method == "Jacobi-Iteration":
                print("in jacobi")

        def getMatrices(namR, num, parameters):
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
            print(bool(parameters[1].get()))

            # Call george's function give it A, B, parameters

        def CreateEntry():

            create, num = numberE(numberEquations)
            selectMethod()
            if create == True:
                frame = tk.LabelFrame(
                    master, text="Fill the system of linear Equations", padx=5, pady=5)
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
                    master, text="More paramters inputs", padx=5, pady=5)
                frame1.grid(row=3, column=10, padx=10, pady=10)
                parameters = []
                precision = tk.Label(frame1)
                precision.configure(text="Precision")
                precision.grid(row=1, column=0, padx=5, pady=5)
                parameters.append(tk.Entry(frame1, width=5).grid(
                    row=1, column=1, padx=5, pady=5))

                method = selected.get()
                if method == "Gauss Elimination" or method == "Gauss-Jodan" or method == "LU Doolittle Form":
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
                    parameters.append(tk.Entry(frame1, width=5).grid(
                        row=5, column=1, padx=5, pady=5))
                    relativeError = tk.Label(frame1)
                    relativeError.configure(text="Absolute relative Error")
                    relativeError.grid(row=6, column=0, padx=5, pady=5)
                    parameters.append(tk.Entry(frame1, width=5).grid(
                        row=6, column=1, padx=5, pady=5))


                b2 = tk.Button(frame, text="Solve",
                               command=lambda: getMatrices(namR, num, parameters))
                # , command = takeCof(num, namR) )
                b2.grid(row=num + 1, column=num)




        numberEFrame = tk.LabelFrame(
            master, text="", padx=5, pady=5, borderwidth=0)
        numberEFrame.grid(row=2, column=0)
        nE = tk.Label(
            numberEFrame, text="The number of equations in the System")
        nE.grid(row=2, column=0)
        numberEquations = tk.Entry(numberEFrame, width=5)
        numberEquations.grid(row=2, column=1)
        b = tk.Button(numberEFrame, text="Enter", command=CreateEntry)
        b.grid(row=2, column=2)
        # h = tk.Scrollbar(master, orient='vertical')
        # h.grid(row=4, column=0, columnspan=20, sticky='ns')


root = tk.Tk()
window = Window(root)
root.title("Drop Down")
root.geometry("500x500")
#root.state("zoomed")
root.mainloop()
