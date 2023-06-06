import os
import encriptado as enc

def configure(type, log, read, llave):
    global tipo 
    tipo = type
    global bitacoraConfigure
    bitacoraConfigure = log
    global archivoConfigure
    archivoConfigure = read
    global llaveConfigure
    llaveConfigure = llave



#Usar casi siempre para el archivo encriptado
def desencriptar(texto):
    llave=llaveConfigure
    return enc.decrypt_password(texto, llave)


#Usar para encriptar la bitácora
def encriptar(texto):
    llave=llaveConfigure
    return enc.encrypt_password(texto, llave)
    



# Funcion create que crea un archivo txt
def create(name, body, path):
    print(tipo)
    # Ruta completa de la carpeta que deseas crear en tu proyecto
    carpeta_proyecto = os.path.join(os.path.dirname(__file__), "../Archivos", path)
    archivo_proyecto = os.path.join(os.path.dirname(__file__), "../Archivos", path, name+".txt")

    # Verificar si la carpeta ya existe antes de crearla
    if not os.path.exists(carpeta_proyecto):
        # Crear la carpeta en tu proyecto
        os.makedirs(carpeta_proyecto)
        # Crear el archivo y escribir el contenido
        with open(archivo_proyecto, "w") as archivo:
            archivo.write(body)

        print(f"Archivo '{name}' creado exitosamente en tu proyecto.")
        print("Carpeta creada exitosamente en tu proyecto.")
    else:
        print("La carpeta ya existe en tu proyecto.")
        with open(archivo_proyecto, "w") as archivo:
            archivo.write(body)

        print(f"Archivo '{name}' creado exitosamente en tu proyecto.")




