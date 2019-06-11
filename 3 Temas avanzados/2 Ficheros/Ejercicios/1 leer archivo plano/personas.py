from io import open

fichero = open("personas.txt","r")#, encoding="utf-8")
lineas = fichero.readlines()
fichero.close()

personas = []

for linea in lineas:
    campos = linea.replace("\n","").split(";")
    persona = { "id":campos[0], "nombre":campos[1],"apellido":campos[2],"nacimiento":campos[3]}
    personas.append(persona)
    
#print(personas)
for p in personas:
    print("(id={}) {} {} => {}".format(p['id'],p['nombre'],p['apellido'],p['nacimiento']))