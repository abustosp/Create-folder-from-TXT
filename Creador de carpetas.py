import os

# Leer el TXT Carpetas.txt y crear las carpetas de la lista si no existen
archivo = open("Carpetas.txt", "r")
# Leer el archivo
lineas = archivo.readlines()
# Cerrar el archivo
archivo.close()
# Recorrer el archivo
for linea in lineas:
    # Eliminar el salto de linea
    linea = linea.replace("\n", "")
    # Crear la carpeta si no existe
    if not os.path.exists(linea):
        os.makedirs(linea)
