import tkinter as tk
from tkinter import ttk
from jacobi import *
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
        optionMenu.pack(padx= 50, pady=10)
        menu = optionMenu["menu"]  
        sublist1 = tk.Menu(menu, tearoff = False)
        sublist1.add_command(label = "Downlittle Form", command= lambda: selected.set("LU Downlittle Form"))
        sublist1.add_command(label= "Crout Form", command= lambda: selected.set("LU Crout Form"))
        sublist1.add_command(label="Cholesky Form" , command= lambda: selected.set("LU Cholesky Form"))  
        menu.add_cascade(label = "LU Decomposition" ,menu= sublist1)

        def my_show():
           method = selected.get()
           if method == "Jacobi-Iteration":
            print("in jacobi") 
            # A = [[2.77,1.0,3.0],[5.0,7.0,4.0],[1.0,1.0,1.0]]
            # b =[11.0,13.0,7.0]
            # guess = [1.0,1.0,1.0]
            # sol, flops = jacobi(A,b,N=6,x=guess)
            # print ("A:")
            # print(A)

            # print ("B:")
            # print(b)
            
            # print('Final X: ')
            # print(sol)

            # print('Total number of flops: ')
            # print(flops)


        b1 = tk.Button(root,text="Confirm",command=my_show)
        b1.pack()
       
        
        

root = tk.Tk()
window = Window(root)
root.title("Drop Down")
root.geometry("500x500")
root.mainloop()
