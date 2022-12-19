import tkinter as tk
from tkinter import ttk
# from jacobi import *
# Window
class Window:

    def __init__(self ,master):
        selected = tk.StringVar()
        
        methods = [
            "Gauss Elimination",
            "Gauss-Jodan",
            "Gauss-Seidel",
            "Jacobi-Iteration"
        ]
        optionMenu = ttk.OptionMenu(master,selected, "Gauss Elimination",*methods)
        optionMenu.grid(row=0,column=0)
        menu = optionMenu["menu"]  
        sublist1 = tk.Menu(menu, tearoff = False)
        sublist1.add_command(label = "Doolittle Form", command= lambda: selected.set("LU Doolittle Form"))
        sublist1.add_command(label= "Crout Form", command= lambda: selected.set("LU Crout Form"))
        sublist1.add_command(label="Cholesky Form" , command= lambda: selected.set("LU Cholesky Form"))  
        menu.add_cascade(label = "LU Decomposition" ,menu= sublist1)


        def numberE(entr):
            isInt=True
            num=-1
            try:
                int(entr.get())
                entr.config(highlightthickness=0,bg ="white" )
                isInt=True
                num = int(entr.get())
            except ValueError:
                entr.config(highlightthickness=2, highlightbackground="red", bg="red",highlightcolor="red")
                # , bg="red"
                isInt = False
            return isInt ,num

        def selectMethod():
            method = selected.get()
            if method == "Gauss Elimination":
                print("in Gauss-Elimimation")
            elif method ==  "Gauss-Jodan":
                print("in Gauss-Jodan")
            elif method ==  "LU Doolittle Form":
                print("in Doolittle Form")
            elif method == "LU Crout Form":
                print("in Crout")
            elif method == "LU Cholesky Form":
                print("in Cholesky")
            elif method ==  "Gauss-Seidel":
                print("in Seidel")
            elif method == "Jacobi-Iteration":
                print("in jacobi")
        
        def getMatrices(namR,num):
            matA = [[0 for i in range(num)]for j in range(num)]
            for i in range(num):
                for j in range(num):
                    matA[i][j] = float(namR[i][j].get())
            matB = [0 for i in range(num)]
            for i in range (num):
                matB[i] = float(namR[i][num].get())
            
            print("A = ")
            print(matA)
            print("B = ")
            print(matB)
            # Call george's function

        def CreateEntry():

            create, num = numberE(numberEquations)
            selectMethod()
            if create==True:
                frame = tk.LabelFrame(master, text="Fill the system of linear Equations", padx=5, pady=5)
                frame.grid(row=3, column=0,padx=10, pady=10)
                namx = [tk.Label(frame) for i in range(num)]
                for j in range(num):
                    t="x" + str(j)
                    namx[j].config(text=t)
                    namx[j].grid(row=0, column=j)

                namR = [[tk.Entry(frame, width=4) for i in range(num + 1)] for j in range(num)]
                for i in range(num):
                    for j in range(num+1):
                        namR[i][j].grid(row=i+1, column=j)

                b2 = tk.Button(frame, text="Solve",command=lambda: getMatrices(namR, num))
                #, command = takeCof(num, namR) )
                b2.grid(row=num+1, column=num)

        numberEFrame = tk.LabelFrame(master, text="", padx=5, pady=5, borderwidth=0)
        numberEFrame.grid(row=2, column=0)
        nE = tk.Label(numberEFrame, text="The number of equations in the System")
        nE.grid(row=2, column=0)
        numberEquations = tk.Entry(numberEFrame, width=5)
        numberEquations.grid(row=2, column=1)
        b = tk.Button(numberEFrame, text="Enter", command=CreateEntry)
        b.grid(row=2, column=2)


root = tk.Tk()
window = Window(root)
root.title("Drop Down")
root.geometry("500x500")
root.mainloop()
