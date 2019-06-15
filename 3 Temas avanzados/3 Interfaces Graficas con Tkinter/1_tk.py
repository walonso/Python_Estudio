from tkinter import *

##creando la raiz:
root = Tk()

root.title("Hola mundo")
## Resizable:
#root.resizable(0,0) #asi no se podria hacer resize
#root.resizable(0,1) # resizable verticalmente
#root.resizable(1,0) # resizable horizontalmente
root.resizable(1,1) # por defecto resizable en ambos lados.
root.iconbitmap('hola.ico')


#esta es la interfaz, por eso debe ir de último
root.mainloop() 