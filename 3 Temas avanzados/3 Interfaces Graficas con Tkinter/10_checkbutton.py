from tkinter import *

def seleccionar():
    cadena = ""
    if (leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin Leche"
    
    if (azucar.get()):
        cadena += " y con azucar"
    else:
        cadena += " y sin azucar"

    monitor.config(text=cadena)
##creando la raiz:

root = Tk()

root.title("Hola mundo")
root.config(bd=15)

leche = IntVar() #1 si, 0 no
azucar = IntVar()

imagen = PhotoImage(file="imagen.gif")
Label(root,image=imagen).pack(side="left") 

frame = Frame(root)
frame.pack(side="left")

Label(frame, text = "¿Como quiere el cafe?").pack(anchor="w")
Checkbutton(frame, text="con leche", variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="con azucar", variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack(side="right")

#esta es la interfaz, por eso debe ir de último
root.mainloop() 