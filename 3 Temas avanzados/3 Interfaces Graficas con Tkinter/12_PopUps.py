from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

##creando la raiz:
root = Tk()

# el mesagge box que muestra 
# aceptar o rechazar algo

def test():
    #1. Mostrar informacion:
    #MessageBox.showinfo("Hola!", "Hola mundo")
    #2. Mostrar warning:
    #MessageBox.showwarning("Alerta", "Sección solo para admins")
    # 3. Mostrar error:
    #MessageBox.showerror("Error", "Ha ocurrido un error inesperado")
    # 4. Preguntar si o no
    """
    resultado = MessageBox.askquestion("Salir","¿Esta seguro que quiere salir sin guardar?")
    if resultado == "yes": #no
        root.destroy()
    """
    # 5. Preguntar aceptar o cancelar
    """
    resultado = MessageBox.askokcancel("Salir","¿Sobreescribir el fichero actual?")
    if resultado == True: #False
        root.destroy()
    """
    # 6. pregruntar si o no (la diferencia con el 4, es que esta retorna booleano)
    """
    resultado = MessageBox.askyesno("Salir","¿Esta seguro que quiere salir sin guardar?")
    if resultado:
        root.destroy()
    """
    # 7. Reintentar
    """
    resultado = MessageBox.askretrycancel("Reintentar","No se puede conectar")
    if resultado:
        root.destroy()
    """
    #8. pedir color de paleta de colores
    """
    color = ColorChooser.askcolor(title="Elige color")
    print(color)  #devuelve tupla de 2 elementos
    """
    #9 pedir ruta archivo
    """
    ruta = FileDialog.askopenfilename(title="Abrir un fichero")
    print(ruta) #devuelve ruta, si no selecciona nada, devuelve vacio
    """
    #10 pedir ruta archivo, desde algun punto
    """
    ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:", 
        filetypes=(("Ficheros de texto","*.txt"),  #si solo fuera uno, debe ir igual la coma
            ("Ficheros de texto avanzado","*.txt2"),
            ("Todos los ficheros","*.*") ))
    print(ruta) #devuelve ruta, si no selecciona nada, devuelve vacio
    """
    #11. Pedir fichero donde guardar la data (aca si creo un fichero y lo dejo abierto)
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="w", defaultextension=".txt") # por defecto es w escritura  open('ruta','w')
    print(fichero)
    if fichero is not None:
        fichero.write("Hola!")
        fichero.close()

Button(root, text="clicame", command=test).pack()

#esta es la interfaz, por eso debe ir de último
root.mainloop() 