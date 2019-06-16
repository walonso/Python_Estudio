Por debajo el comando help usa pydoc, desde el cmd puede usar:
> pydoc mi_modulo

sin embargo si no le funciona uselo asi:
> python -m pydoc mi_modulo


Con pydoc, se puede generar documentacion Html: (con el parametro -w)
> python -m pydoc -w mi_modulo

Si es un paquete con subpaquetes: (el .\ para que genere de todos los subpaquetes)
python -m pydoc -w mi_paquete .\

Para ver toda la documentacion pydoc en nuestro sistema: (en html)
> python -m pydoc -b

o para un puerto especifico
> python -m pydoc -p 8000
