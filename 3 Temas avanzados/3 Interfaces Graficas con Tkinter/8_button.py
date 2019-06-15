from tkinter import *

def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    #borrar()

def resta():
    r.set(float(n1.get()) - float(n2.get()))
    #borrar()

def producto():
    r.set(float(n1.get()) * float(n2.get()))
    #borrar()


def borrar():
    n1.set("")
    n2.set("")

##creando la raiz:
root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

# le psamos esos stringvar a las cajas para capturarlas (como en la funcion sumar)
Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack() #primer numero
Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack() # segundo numero
Label(root, text=" ").pack()
Label(root, text="\nResultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack() # res1ultado

Button(root,text="Sumar", command=sumar).pack(side="left")
Button(root,text="Resta", command=resta).pack(side="left")
Button(root,text="Producto", command=producto).pack(side="left")




#esta es la interfaz, por eso debe ir de último
root.mainloop() 