import os
import shutil
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
    



def create(name, body, path):
    if tipo == "Local":
        # Ruta completa de la carpeta y el archivo que deseas crear en tu proyecto
        archivo_proyecto = os.path.join(os.path.dirname(__file__), "../Archivos", path, name+".txt")

        # Verificar si la carpeta y el archivo ya existen antes de crearlos
        if not os.path.exists(archivo_proyecto):
            # Crear la carpeta y el archivo en tu proyecto
            os.makedirs(os.path.dirname(archivo_proyecto), exist_ok=True)
            # Crear el archivo y escribir el contenido
            with open(archivo_proyecto, "w") as archivo:
                archivo.write(body)

            print(f"Archivo '{name}' creado exitosamente en tu proyecto.")
            print("Carpeta creada exitosamente en tu proyecto.")
        else:
            print("La carpeta y el archivo ya existen en tu proyecto.")
            with open(archivo_proyecto, "w") as archivo:
                archivo.write(body)

            print(f"Archivo '{name}' creado exitosamente en tu proyecto.")
    else:
        print("Cloud")




def validate_filename(name):
    if name:
        if not name.endswith(".txt"):
            name += ".txt"
    return name




def delete(path, name):
    if tipo == "Local":
        name = validate_filename(name)
        path = path.replace('"', '')  
        path = path.lstrip('/')
        archivo_proyecto = os.path.join(os.path.dirname(__file__), "../Archivos", path, name)

        if os.path.exists(archivo_proyecto):
            if os.path.isfile(archivo_proyecto):
                os.remove(archivo_proyecto)
                print(f"Archivo '{name}' eliminado exitosamente.")
            elif os.path.isdir(archivo_proyecto):
                shutil.rmtree(archivo_proyecto)
                print(f"Carpeta eliminada exitosamente.")
        else:
            print(f"No se encontró el archivo o carpeta en la ruta especificada.")
    else:
        print("Cloud")



