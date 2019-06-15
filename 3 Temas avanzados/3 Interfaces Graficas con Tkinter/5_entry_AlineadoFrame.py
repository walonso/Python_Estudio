from tkinter import *

##creando la raiz:
root = Tk()

frame = Frame(root)
frame.pack()

entry = Entry(frame)
entry.pack(side="right")

label = Label(frame, text="Nombre")
label.pack(side="left")

frame2 = Frame(root)
frame2.pack()

entry2 = Entry(frame2)
entry2.pack(side="right")

label2 = Label(frame2, text="Apellidos")
label2.pack(side="left")



#esta es la interfaz, por eso debe ir de último
root.mainloop() 