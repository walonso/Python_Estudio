from tkinter import *

##creando la raiz:
root = Tk()

texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Consolas", 12), padx=15,pady=15, selectbackground="red") #30 caracteres y 10 caracteres


#esta es la interfaz, por eso debe ir de último
root.mainloop() 