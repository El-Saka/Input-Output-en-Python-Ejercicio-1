# Abrimos el archivo en modo escritura y escribimos dentro
with open("archivo.txt", "w" ) as archivo:
    archivo.write("Hola Mundo")

# Cerramos el archivo
archivo.close()

# Abrimos el archivo en modo lectura y leemos su contenido
with open("archivo.txt", "r" ) as archivo:
    contenido = archivo.read()

# Imprimimos el contenido del archivo
print(contenido)