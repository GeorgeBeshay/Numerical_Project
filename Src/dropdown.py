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
        sublist1.add_command(label = "Downlittle Form", command= lambda: selected.set("LU Downlittle Form"))
        sublist1.add_command(label= "Crout Form", command= lambda: selected.set("LU Crout Form"))
        sublist1.add_command(label="Cholesky Form" , command= lambda: selected.set("LU Cholesky Form"))  
        menu.add_cascade(label = "LU Decomposition" ,menu= sublist1)

        # def my_show():
        #    method = selected.get()
        #    if method == "Jacobi-Iteration":
        #     print("in jacobi") 

        # b1 = tk.Button(master,text="Confirm",command=my_show)
        # b1.grid(row=0,column=1)

        def numberE(entr):
            method = selected.get()
            if method == "Jacobi-Iteration":
                print("in jacobi")
            isInt=True
            num=-1
            try:
                int(entr.get())
                entr.config(highlightthickness=0)
                isInt=True
                num = int(entr.get())
            except ValueError:
                entr.config(highlightthickness=2, highlightbackground="red", highlightcolor="red")
                isInt = False
            return isInt ,num


        def takeCof (num, namR):
            mat = [[0 for i in range(num+1)]for j in range(num)]
            for i in range(num):
                for j in range(num + 1):
                    isint ,num=numberE(namR[i][j])
                    if isint==False :
                        CreateEntry()
                        return
                    else:
                        mat[i][j]=num


        def CreateEntry():
            create, num = numberE(numberEquations)
            if create==True:

                frame = tk.LabelFrame(master, text="Fill the system of linear Equations", padx=5, pady=5)
                frame.grid(row=3, column=0,padx=10, pady=10)
                namx = [tk.Label(frame) for i in range(num)]
                for j in range(num):
                    t="x"+str(j)
                    namx[j].config(text=t)
                    namx[j].grid(row=0, column=j)

                namR = [[tk.Entry(frame, width=4) for i in range(num+1)]for j in range(num)]
                for i in range(num):
                    for j in range(num+1):
                        namR[i][j].grid(row=i+1, column=j)

                b2 = tk.Button(frame, text="enter")
                    #, command = takeCof(num, namR) )
                b2.grid(row=num+1, column=num)


        numberEFrame = tk.LabelFrame(master, text="", padx=5, pady=5, borderwidth=0)
        numberEFrame.grid(row=2, column=0)
        nE = tk.Label(numberEFrame, text="The number of equations in the System")
        nE.grid(row=2, column=0)
        numberEquations = tk.Entry(numberEFrame, width=5)
        numberEquations.grid(row=2, column=1)
        b = tk.Button(numberEFrame, text="enter", command=CreateEntry)
        b.grid(row=2, column=2)

    
        

root = tk.Tk()
window = Window(root)
root.title("Drop Down")
root.geometry("500x500")
root.mainloop()
