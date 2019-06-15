from tkinter import *

##creando la raiz:
root = Tk()
"""

# variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")


# Configuracion de un marco
#frame = Frame(root, width=480, height=320)
#frame.pack() #Pack empaqueta y distribuye segun los elementos

# root o frame sirven para empaquetar
Label(root, text = "Hola mundo").pack(anchor="nw") #nw = north west #donde se quiere inyectar
#label.place(x=100,y=100) 
label = Label(root, text = "otra etiqueta") 
label.pack(anchor="center")
Label(root, text = "Ultima etiqueta").pack(anchor="se") 

label.config(bg="green", fg="blue", font=("verdana",24))
label.config(textvariable=texto)
"""
# agregando imagen
imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")


#esta es la interfaz, por eso debe ir de último
root.mainloop() 