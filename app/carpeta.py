from datetime import datetime
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
    return enc.decrypt(texto, llave)


#Usar para encriptar la bitácora
def encriptar(texto):
    llave=llaveConfigure
    return enc.encrypt(texto, llave)
    



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
            bitacoraReturn=bitacora("Output","Create", f"Archivo {name} creado exitosamente")
            bitacoraLog(bitacoraReturn)
            print(f"Archivo {name} creado exitosamente en tu proyecto.")
            print("Carpeta creada exitosamente en tu proyecto.")
        else:
            bitacoraReturn=bitacora("Output","Create", f"Error: La carpeta y el archivo ya existen")
            bitacoraLog(bitacoraReturn)
            print(bitacoraReturn)
            print("La carpeta y el archivo ya existen en tu proyecto.")
    else:
        print("Cloud")



def delete(path, name):
    if tipo == "Local":
        name = validate_filename(name)
        path = path.replace('"', '')  
        path = path.lstrip('/')
        archivo_proyecto = os.path.join(os.path.dirname(__file__), "../Archivos", path, name)

        if os.path.exists(archivo_proyecto):
            if os.path.isfile(archivo_proyecto):
                os.remove(archivo_proyecto)
                bitacoraReturn=bitacora("Output","Delete", f"Archivo {name} eliminado exitosamente.")
                bitacoraLog(bitacoraReturn)
                print(f"Archivo {name} eliminado exitosamente.")
            elif os.path.isdir(archivo_proyecto):
                shutil.rmtree(archivo_proyecto)
                bitacoraReturn=bitacora("Output","Delete", f"Carpeta eliminada exitosamente.")
                bitacoraLog(bitacoraReturn)
                print(f"Carpeta eliminada exitosamente.")
        else:
            bitacoraReturn=bitacora("Output","Delete", f"Error: No se encontro el archivo o carpeta en la ruta especificada.")
            bitacoraLog(bitacoraReturn)
            print(f"No se encontro el archivo o carpeta en la ruta especificada.")
    else:
        print("Cloud")





def copy(from_path, to):
    if tipo == "Local":
        from_path = from_path.replace('"', '')
        to = to.replace('"', '')
        from_path = from_path.lstrip('/')
        to = to.lstrip('/')

        # Construir las rutas completas de origen y destino
        from_path_full = os.path.join(os.path.dirname(__file__), "../Archivos", from_path)
        to_full = os.path.join(os.path.dirname(__file__), "../Archivos", to)

        if os.path.exists(from_path_full):
            if os.path.isdir(from_path_full):
                # Validar si ya existe una carpeta con el mismo nombre en la ubicación de destino
                if os.path.isdir(to_full) and os.path.basename(from_path_full) == os.path.basename(to_full):
                    bitacoraReturn=bitacora("Output","Copy", f"Error: Ya existe una carpeta con el nombre {os.path.basename(from_path_full)} en la ubicación de destino.")
                    bitacoraLog(bitacoraReturn)
                    print(f"Advertencia: Ya existe una carpeta con el nombre '{os.path.basename(from_path_full)}' en la ubicación de destino.")
                else:
                    # Copiar contenido de la carpeta
                    copy_folder_contents(from_path_full, to_full)
                    bitacoraReturn=bitacora("Output","Copy", f"Contenido de la carpeta '{os.path.basename(from_path_full)}' copiado exitosamente a '{to}'.")
                    bitacoraLog(bitacoraReturn)
                    print(f"Contenido de la carpeta '{os.path.basename(from_path_full)}' copiado exitosamente a '{to}'.")
            elif os.path.isfile(from_path_full):
                # Copiar archivo individual
                copy_file(from_path_full, to_full)
                bitacoraReturn=bitacora("Output","Copy", f"Archivo '{os.path.basename(from_path_full)}' copiado exitosamente a '{to}'.")
                bitacoraLog(bitacoraReturn)
                print(f"Archivo '{os.path.basename(from_path_full)}' copiado exitosamente a '{to}'.")
        else:
            bitacoraReturn=bitacora("Output","Copy", f"Error: No se encontro la carpeta o archivo '{from_path}' en la ruta especificada.")
            bitacoraLog(bitacoraReturn)
            print(f"No se encontro la carpeta o archivo '{from_path}' en la ruta especificada.")
    else:
        print("Cloud")




def transfer(from_path, to, mode):
    if tipo == "Local":
        if mode == "Local":
            from_path = from_path.replace('"', '')
            to = to.replace('"', '')
            from_path = from_path.lstrip('/')
            to = to.lstrip('/')

            # Construir las rutas completas de origen y destino
            from_path_full = os.path.join(os.path.dirname(__file__), "../Archivos", from_path)
            to_full = os.path.join(os.path.dirname(__file__), "../Archivos", to)

            if os.path.exists(from_path_full):
                if os.path.isdir(from_path_full):
                    # Validar si ya existe una carpeta con el mismo nombre en la ubicación de destino
                    if os.path.isdir(to_full) and os.path.basename(from_path_full) == os.path.basename(to_full):
                        bitacoraReturn=bitacora("Output","Transfer", f"Error: Ya existe una carpeta con el nombre {os.path.basename(from_path_full)} en la ubicación de destino.")
                        bitacoraLog(bitacoraReturn)
                        print(f"Advertencia: Ya existe una carpeta con el nombre '{os.path.basename(from_path_full)}' en la ubicación de destino.")
                    else:
                        # Transferir contenido de la carpeta
                        transfer_folder_contents(from_path_full, to_full)
                        bitacoraReturn=bitacora("Output","Transfer", f"Contenido de la carpeta '{os.path.basename(from_path_full)}' transferido exitosamente a '{to}'.")
                        bitacoraLog(bitacoraReturn)
                        print(f"Contenido de la carpeta '{os.path.basename(from_path_full)}' transferido exitosamente a '{to}'.")
                else:
                    bitacoraReturn=bitacora("Output","Transfer", f"Error: El origen '{from_path_full}' no es una carpeta.")
                    bitacoraLog(bitacoraReturn)
                    print(f"El origen '{from_path_full}' no es una carpeta.")
            else:
                bitacoraReturn=bitacora("Output","Transfer", f"Error: No se encontro la carpeta o archivo '{from_path}' en la ruta especificada.")
                bitacoraLog(bitacoraReturn)
                print(f"No se encontro la carpeta '{from_path}' en la ruta especificada.")
        elif mode == "Cloud":
            print("Transferir de Local a Cloud")
        else:
            print("Modo no válido.")
    else:
        print("Cloud")






def rename(path, name):
    if tipo == "Local":
        name = name.strip()
        path = path.lstrip('/')
        archivo_proyecto = os.path.join(os.path.dirname(__file__), "../Archivos", path)

        if os.path.exists(archivo_proyecto):
            if os.path.isfile(archivo_proyecto):
                # Ruta completa del nuevo archivo
                new_path = os.path.join(os.path.dirname(archivo_proyecto), name)
                # Verificar si el nuevo archivo ya existe
                if os.path.exists(new_path):
                    bitacoraReturn=bitacora("Output","Rename", f"Error: Ya existe un archivo con el nombre {name}.")
                    bitacoraLog(bitacoraReturn)
                    print(f"Ya existe un archivo con el nombre {name}.")
                else:
                    os.rename(archivo_proyecto, new_path)
                    bitacoraReturn=bitacora("Output","Rename", f"El archivo '{path}' ha sido renombrado a {name}.")
                    bitacoraLog(bitacoraReturn)
                    print(f"El archivo '{path}' ha sido renombrado a {name}.")
            elif os.path.isdir(archivo_proyecto):
                # Ruta completa de la nueva carpeta
                parent_dir = os.path.dirname(archivo_proyecto)
                new_path = os.path.join(parent_dir, name)
                if not os.path.exists(new_path):
                    shutil.move(archivo_proyecto, new_path)
                    bitacoraReturn=bitacora("Output","Rename", f"La carpeta '{path}' ha sido renombrado a {name}.")
                    bitacoraLog(bitacoraReturn)
                    print(f"La carpeta '{path}' ha sido renombrada a {name}.")
                else:
                    bitacoraReturn=bitacora("Output","Rename", f"Error: Ya existe una carpeta con el nombre {name}.")
                    bitacoraLog(bitacoraReturn)
                    print(f"Ya existe una carpeta con el nombre {name}.")
        else:
            bitacoraReturn=bitacora("Output","Rename", f"Error: No se encontro el archivo o carpeta '{path}' en la ruta especificada.")
            bitacoraLog(bitacoraReturn)
            print(f"No se encontro el archivo o carpeta '{path}' en la ruta especificada.")
    else:
        print("Cloud")



def modify(path, body):
    if tipo == "Local":
        path = path.lstrip('/')
        archivo_proyecto = os.path.join(os.path.dirname(__file__), "../Archivos", path)

        if os.path.isfile(archivo_proyecto):
            # Modificar el contenido del archivo
            with open(archivo_proyecto, "w") as archivo:
                archivo.write(body)
            bitacoraReturn=bitacora("Output","Modify", f"Contenido del archivo '{path}' modificado exitosamente.")
            bitacoraLog(bitacoraReturn)
            print(f"Contenido del archivo '{path}' modificado exitosamente.")
        else:
            bitacoraReturn=bitacora("Output","Modify", f"Error: No se encontro el archivo '{path}' en la ruta especificada.")
            bitacoraLog(bitacoraReturn)
            print(f"No se encontro el archivo '{path}' en la ruta especificada.")
    else:
        print("Cloud")




def add(path, body):
    if tipo == "Local":
        path = path.lstrip('/')
        archivo_proyecto = os.path.join(os.path.dirname(__file__), "../Archivos", path)

        if os.path.isfile(archivo_proyecto):
            # Agregar contenido al archivo
            with open(archivo_proyecto, "a") as archivo:
                archivo.write(body)
            bitacoraReturn=bitacora("Output","Add", f"Contenido agregado al archivo '{path}' exitosamente.")
            bitacoraLog(bitacoraReturn)
            print(f"Contenido agregado al archivo '{path}' exitosamente.")
        else:
            bitacoraReturn=bitacora("Output","Add", f"Error: No se encontro el archivo '{path}' en la ruta especificada.")
            bitacoraLog(bitacoraReturn)
            print(f"No se encontro el archivo '{path}' en la ruta especificada.")
    else:
        print("Cloud")




def bitacora(type, comand, instruction):
    fecha=""
    fecha = fechaYhora()
    print(bitacoraConfigure)
    if bitacoraConfigure=="True":
        instruccion = enc.encrypt((f"{fecha} - {type} - {comand} - {instruction}\n"), llaveConfigure)
    else:
        instruccion = f"{fecha} - {type} - {comand} - {instruction}\n"        
    return instruccion





# --------------------------------------------------------------------------------
#                           METODOS AUXILIARES
# --------------------------------------------------------------------------------


#Validar el nombre del archivo
def validate_filename(name):
    if name:
        if not name.endswith(".txt"):
            name += ".txt"
    return name


def copy_folder_contents(from_folder, to_folder):
    # Crear la carpeta de destino si no existe
    os.makedirs(to_folder, exist_ok=True)

    # Copiar los archivos y subdirectorios dentro de la carpeta de origen
    for item in os.listdir(from_folder):
        item_path = os.path.join(from_folder, item)
        if os.path.isfile(item_path):
            copy_file(item_path, os.path.join(to_folder, item))
        elif os.path.isdir(item_path):
            copy_folder_contents(item_path, os.path.join(to_folder, item))

def copy_file(src, dst):
    shutil.copy2(src, dst)  # Copiar archivo preservando los metadatos


def transfer_folder_contents(from_folder, to_folder):
    # Crear la carpeta de destino si no existe
    os.makedirs(to_folder, exist_ok=True)

    # Mover los archivos y subdirectorios dentro de la carpeta de origen
    for item in os.listdir(from_folder):
        item_path = os.path.join(from_folder, item)
        if os.path.isfile(item_path):
            shutil.move(item_path, os.path.join(to_folder, item))
        elif os.path.isdir(item_path):
            transfer_folder_contents(item_path, os.path.join(to_folder, item))

def fechaYhora():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime


def bitacoraLog(texto):
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    dia_actual = fecha_actual.day
    mes_actual = fecha_actual.month
    año_actual = fecha_actual.year

    # Construir la ruta del archivo de registro
    ruta_log_archivos = os.path.join(os.path.dirname(__file__), "../Archivos/log", str(dia_actual), str(mes_actual), str(año_actual))
    os.makedirs(ruta_log_archivos, exist_ok=True)  # Crear directorios si no existen

    nombre_archivo = "log_archivos.txt"
    ruta_completa = os.path.join(ruta_log_archivos, nombre_archivo)

    # Abrir el archivo en modo de apendizaje (append) y escribir el texto
    with open(ruta_completa, "a") as archivo:
        archivo.write(texto)

    print(f"Texto agregado al archivo de registro: {texto}")