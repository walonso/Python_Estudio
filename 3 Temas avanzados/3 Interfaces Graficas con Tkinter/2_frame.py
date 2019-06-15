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

################### Frame ##########
frame = Frame(root, width=480, height=320)
#frame.pack(side="right", anchor="w") # (side: top, bottom, left, anchor: e=este, w=west) donde se quiere que este posicionado el frame del tk (contenedor) 
frame.pack(fill='x', expand=1) #rellena la raiz, segun el fill llena hacia la direccion  (fill:'x', y o both)

frame.config(cursor="pirate")
frame.config(bg="lightblue") # color fondo
frame.config(bd=25) #borde de 25 pixeles 
frame.config(relief="sunken")



root.config(cursor="arrow")
root.config(bg="blue") # color fondo
root.config(bd=15) #borde de 25 pixeles 
root.config(relief="ridge")


#esta es la interfaz, por eso debe ir de último
root.mainloop() 