#!/usr/bin/env python

import os
import zipfile

#Definimos la ruta de la carpeta a analizar
carpeta = "F:\JW - Testigos de Jehova\Canciones del Reino"


#Definimos las extensiones de los archivos a comprimir
matchlist = ['.png', '.txt', '.wmv', '.py']

#Recorremos los archivosde la carpeta
for archivo in os.listdir(carpeta):
    for ext in matchlist:
        #Si la extension coincide lo añadimos
        if archivo.endswith(ext):
            zipwrite(os.path.join(carpeta, archivo))
    print("archivo -> "+os.path.join(carpeta, archivo))

#Finalmente cerramos el archivo para guardarlo
zip.close()


from distutils.dir_util import copy_tree


DIRECTORIO_ORIGEN = "origen"
DIRECTORIO_DESTINO = "destino"


print("Copiando...")
copy_tree(DIRECTORIO_ORIGEN, DIRECTORIO_DESTINO)
print("Copiado")


import os
if os.path.isfile("archivo/o_ruta"):
    print("Sí es un archivo")
else:
    print("No es archivo, o no existe")

Actualización: recuerda llamar a isfile con la ruta absoluta del 
archivo en caso de que te dé problemas. Para eso puedes usar os.path.join, que une rutas.


import os
if os.path.isdir("ruta/a/carpeta"):
    print("Sí es una carpeta")
else:
    print("No es una carpeta o no existe")


# Se define el nombre de la carpeta o directorio a crear
directorio = "/home/dev/Documentos/python/archivos/dir_prueba"
try:
    os.mkdir(directorio)
except OSError:
    print("La creación del directorio %s falló" % directorio)
else:
    print("Se ha creado el directorio: %s " % directorio)





import zipfile
ruta_zip = "/home/decodigo/Documentos/python/archivos/archivos.zip"
ruta_extraccion = "/home/decodigo/Documentos/python/archivos/"
password = None
archivo_zip = zipfile.ZipFile(ruta_zip, "r")
try:
    print(archivo_zip.namelist())
    archivo_zip.extractall(pwd=password, path=ruta_extraccion)
except:
    pass
archivo_zip.close()