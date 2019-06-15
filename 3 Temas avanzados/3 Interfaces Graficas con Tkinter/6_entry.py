from tkinter import *

##creando la raiz:
root = Tk()

# con grid se imagina como cuadricula
label = Label(root, text="Nombre muy largo")
label.grid(row=0, column=0, sticky="e", padx=5, pady=5) #sticky es para que se justifique el texto al este, north, suth..
entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="disabled") #con state queda deshabilitado o habilitado(normal) el campo


label2 = Label(root, text="Contraseña")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5) #sticky 
entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show="*") #muestre * en lugar del texto



#esta es la interfaz, por eso debe ir de último
root.mainloop() 