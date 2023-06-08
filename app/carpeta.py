from datetime import datetime
import os
import shutil
import encriptado as enc


global bitacoraConfigure
bitacoraConfigure = "False"
global tipo
tipo = ""
def configure(type, log, read, llave):
    global tipo
    tipo = type
    global bitacoraConfigure
    bitacoraConfigure = log
    global archivoConfigure
    archivoConfigure = read
    global llaveConfigure
    llaveConfigure = llave
    bitacoraReturn=bitacora("Output","Configure", f"Archivo configurado exitosamente")
    bitacoraLog(bitacoraReturn)
    write(f"Configure ejecutando...")
    write(bitacoraReturn)



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
            write(f"Create ejecutando...")
            write(bitacoraReturn)
            print(f"Archivo {name} creado exitosamente en tu proyecto.")         
            print("Carpeta creada exitosamente en tu proyecto.")
        else:
            bitacoraReturn=bitacora("Output","Create", f"Error: La carpeta y el archivo ya existen")
            bitacoraLog(bitacoraReturn)
            write(f"Create ejecutando...")
            write(bitacoraReturn)
            print("La carpeta y el archivo ya existen en tu proyecto.")
    
    elif tipo == "Cloud":
        print("Cloud")
    
    
    else:
        bitacoraReturn=bitacora("Output","Configure", f"Error: No se ha configurado el tipo de almacenamiento")
        bitacoraLog(bitacoraReturn)
        write(bitacoraReturn)
        print("Error: No se ha configurado el tipo de almacenamiento")





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
                write(f"Delete ejecutando...")
                write(bitacoraReturn)
                print(f"Archivo {name} eliminado exitosamente.")
            elif os.path.isdir(archivo_proyecto):
                shutil.rmtree(archivo_proyecto)
                bitacoraReturn=bitacora("Output","Delete", f"Carpeta eliminada exitosamente.")
                bitacoraLog(bitacoraReturn)
                write(f"Delete ejecutando...")
                write(bitacoraReturn)
                print(f"Carpeta eliminada exitosamente.")
        else:
            bitacoraReturn=bitacora("Output","Delete", f"Error: No se encontro el archivo o carpeta en la ruta especificada.")
            bitacoraLog(bitacoraReturn)
            write(f"Delete ejecutando...")
            write(bitacoraReturn)
            print(f"No se encontro el archivo o carpeta en la ruta especificada.")
    
    elif tipo == "Cloud":
        print("Cloud")
    
    
    else:
        bitacoraReturn=bitacora("Output","Configure", f"Error: No se ha configurado el tipo de almacenamiento")
        bitacoraLog(bitacoraReturn)
        write(bitacoraReturn)
        print("Error: No se ha configurado el tipo de almacenamiento")





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
                    bitacoraReturn = bitacora("Output", "Copy", f"Error: Ya existe una carpeta con el nombre '{os.path.basename(from_path_full)}' en la ubicación de destino.")
                    bitacoraLog(bitacoraReturn)
                    write(f"Copy ejecutando...")
                    write(bitacoraReturn)
                    print(f"Advertencia: Ya existe una carpeta con el nombre '{os.path.basename(from_path_full)}' en la ubicación de destino.")
                else:
                    # Copiar contenido de la carpeta
                    copyCarpeta(from_path_full, to_full)
                    bitacoraReturn = bitacora("Output", "Copy", f"Contenido de la carpeta '{os.path.basename(from_path_full)}' copiado exitosamente a '{to}'.")
                    bitacoraLog(bitacoraReturn)
                    write(f"Copy ejecutando...")
                    write(bitacoraReturn)
                    print(f"Contenido de la carpeta '{os.path.basename(from_path_full)}' copiado exitosamente a '{to}'.")
            elif os.path.isfile(from_path_full):
                # Verificar si ya existe un archivo con el mismo nombre en la ubicación de destino
                if os.path.exists(to_full):
                    bitacoraReturn = bitacora("Output", "Copy", f"Advertencia: Ya existe un archivo con el nombre '{os.path.basename(from_path_full)}' en la ubicación de destino.")
                    bitacoraLog(bitacoraReturn)
                    write(f"Copy ejecutando...")
                    write(bitacoraReturn)
                    print(f"Advertencia: Ya existe un archivo con el nombre '{os.path.basename(from_path_full)}' en la ubicación de destino.")

                else:
                    # Copiar archivo individual
                    copyArchivo(from_path_full, to_full)
                    bitacoraReturn = bitacora("Output", "Copy", f"Archivo '{os.path.basename(from_path_full)}' copiado exitosamente a '{to}'.")
                    bitacoraLog(bitacoraReturn)
                    write(f"Copy ejecutando...")
                    write(bitacoraReturn)
                    print(f"Archivo '{os.path.basename(from_path_full)}' copiado exitosamente a '{to}'.")
        else:
            bitacoraReturn = bitacora("Output", "Copy", f"Error: No se encontró la carpeta o archivo '{from_path}' en la ruta especificada.")
            bitacoraLog(bitacoraReturn)
            write(f"Copy ejecutando...")
            write(bitacoraReturn)
            print(f"No se encontró la carpeta o archivo '{from_path}' en la ruta especificada.")
    
    elif tipo == "Cloud":
        print("Cloud")
    
    
    else:
        bitacoraReturn=bitacora("Output","Configure", f"Error: No se ha configurado el tipo de almacenamiento")
        bitacoraLog(bitacoraReturn)
        write(bitacoraReturn)
        print("Error: No se ha configurado el tipo de almacenamiento")






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
                if os.path.isfile(from_path_full):
                    # Transferir archivo individual
                    transferArchivo(from_path_full, to_full)
                elif os.path.isdir(from_path_full):
                    # Transferir contenido de la carpeta
                    transferCarpeta(from_path_full, to_full)
                else:
                    bitacoraReturn = bitacora("Output", "Transfer", f"Error: El origen '{from_path_full}' no es una carpeta ni un archivo válido.")
                    bitacoraLog(bitacoraReturn)
                    write(f"Transfer ejecutando...")
                    write(bitacoraReturn)
                    print(f"El origen '{from_path_full}' no es una carpeta ni un archivo válido.")
            else:
                bitacoraReturn = bitacora("Output", "Transfer", f"Error: No se encontró la carpeta o archivo '{from_path}' en la ruta especificada.")
                bitacoraLog(bitacoraReturn)
                write(f"Transfer ejecutando...")
                write(bitacoraReturn)
                print(f"No se encontró la carpeta o archivo '{from_path}' en la ruta especificada.")

        elif mode == "Cloud":
            #ESCRBIR ACÁ EL CÓDIGO PARA EL LOCAL A CLOUD
            print("Transferir de Local a Cloud")
    
    elif tipo == "Cloud":
        print("Cloud")

        if mode == "Local":
            #ESCRBIR ACÁ EL CÓDIGO PARA EL CLOUD A LOCAL
            print("Transferir de Cloud a Local")

        else:
            #ESCRBIR ACÁ EL CÓDIGO PARA EL CLOUD A CLOUD
            print("Transferir de Cloud a Cloud")

    else:
        bitacoraReturn=bitacora("Output","Configure", f"Error: No se ha configurado el tipo de almacenamiento")
        bitacoraLog(bitacoraReturn)
        write(bitacoraReturn)
        print("Error: No se ha configurado el tipo de almacenamiento")
        




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
                    write(f"Rename ejecutando...")
                    write(bitacoraReturn)
                    print(f"Ya existe un archivo con el nombre {name}.")
                else:
                    os.rename(archivo_proyecto, new_path)
                    bitacoraReturn=bitacora("Output","Rename", f"El archivo '{path}' ha sido renombrado a {name}.")
                    bitacoraLog(bitacoraReturn)
                    write(f"Rename ejecutando...")
                    write(bitacoraReturn)
                    print(f"El archivo '{path}' ha sido renombrado a {name}.")
            elif os.path.isdir(archivo_proyecto):
                # Ruta completa de la nueva carpeta
                parent_dir = os.path.dirname(archivo_proyecto)
                new_path = os.path.join(parent_dir, name)
                if not os.path.exists(new_path):
                    shutil.move(archivo_proyecto, new_path)
                    bitacoraReturn=bitacora("Output","Rename", f"La carpeta '{path}' ha sido renombrado a {name}.")
                    bitacoraLog(bitacoraReturn)
                    write(f"Rename ejecutando...")
                    write(bitacoraReturn)
                    print(f"La carpeta '{path}' ha sido renombrada a {name}.")
                else:
                    bitacoraReturn=bitacora("Output","Rename", f"Error: Ya existe una carpeta con el nombre {name}.")
                    bitacoraLog(bitacoraReturn)
                    write(f"Rename ejecutando...")
                    write(bitacoraReturn)
                    print(f"Ya existe una carpeta con el nombre {name}.")
        else:
            bitacoraReturn=bitacora("Output","Rename", f"Error: No se encontro el archivo o carpeta '{path}' en la ruta especificada.")
            bitacoraLog(bitacoraReturn)
            write(f"Rename ejecutando...")
            write(bitacoraReturn)
            print(f"No se encontro el archivo o carpeta '{path}' en la ruta especificada.")
    
    elif tipo == "Cloud":
        print("Cloud")
    
    
    else:
        bitacoraReturn=bitacora("Output","Configure", f"Error: No se ha configurado el tipo de almacenamiento")
        bitacoraLog(bitacoraReturn)
        write(bitacoraReturn)
        print("Error: No se ha configurado el tipo de almacenamiento")



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
            write(f"Modify ejecutando...")
            write(bitacoraReturn)
            print(f"Contenido del archivo '{path}' modificado exitosamente.")
        else:
            bitacoraReturn=bitacora("Output","Modify", f"Error: No se encontro el archivo '{path}' en la ruta especificada.")
            bitacoraLog(bitacoraReturn)
            write(f"Modify ejecutando...")
            write(bitacoraReturn)
            print(f"No se encontro el archivo '{path}' en la ruta especificada.")
    
    elif tipo == "Cloud":
        print("Cloud")
    
    
    else:
        bitacoraReturn=bitacora("Output","Configure", f"Error: No se ha configurado el tipo de almacenamiento")
        bitacoraLog(bitacoraReturn)
        write(bitacoraReturn)
        print("Error: No se ha configurado el tipo de almacenamiento")




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
            write(f"Add ejecutando...")
            write(bitacoraReturn)
            print(f"Contenido agregado al archivo '{path}' exitosamente.")
        else:
            bitacoraReturn=bitacora("Output","Add", f"Error: No se encontro el archivo '{path}' en la ruta especificada.")
            bitacoraLog(bitacoraReturn)
            write(f"Add ejecutando...")
            write(bitacoraReturn)
            print(f"No se encontro el archivo '{path}' en la ruta especificada.")
    
    elif tipo == "Cloud":
        print("Cloud")
    
    
    else:
        bitacoraReturn=bitacora("Output","Configure", f"Error: No se ha configurado el tipo de almacenamiento")
        bitacoraLog(bitacoraReturn)
        write(bitacoraReturn)
        print("Error: No se ha configurado el tipo de almacenamiento")




def backup():
    if tipo == "Local":
        pass
    elif tipo == "Cloud":
        pass
    else:
        bitacoraReturn=bitacora("Output","Configure", f"Error: No se ha configurado el tipo de almacenamiento")
        bitacoraLog(bitacoraReturn)
        write(bitacoraReturn)
        print("Error: No se ha configurado el tipo de almacenamiento")





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


def copyCarpeta(from_folder, to_folder):
    # Crear la carpeta de destino si no existe
    os.makedirs(to_folder, exist_ok=True)

    # Copiar los archivos y subdirectorios dentro de la carpeta de origen
    for item in os.listdir(from_folder):
        item_path = os.path.join(from_folder, item)
        if os.path.isfile(item_path):
            copyArchivo(item_path, os.path.join(to_folder, item))
        elif os.path.isdir(item_path):
            copyCarpeta(item_path, os.path.join(to_folder, item))

def copyArchivo(src, dst):
    shutil.copy2(src, dst)  


def transferCarpeta(from_path, to_path):
    # Si no existe la carpeta de destino, se crea
    if not os.path.exists(to_path):
        os.makedirs(to_path)

    # Obtener el nombre de la carpeta de origen
    folder_name = os.path.basename(from_path)

    # Verificar si ya existe una carpeta con el mismo nombre en la ubicación de destino
    if os.path.exists(os.path.join(to_path, folder_name)):
        # Imprimir mensaje de advertencia
        bitacoraReturn=bitacora("Output","Transfer", f"Error: La carpeta '{folder_name}' ya existe en la ubicación de destino.")
        bitacoraLog(bitacoraReturn)
        write(f"Transfer ejecutando...")
        write(bitacoraReturn)
        print(f"Advertencia: La carpeta '{folder_name}' ya existe en la ubicación de destino.")

    # Mover el contenido de la carpeta de origen a la ubicación de destino
    for item in os.listdir(from_path):
        item_path = os.path.join(from_path, item)
        if os.path.isfile(item_path):
            # Transferir archivo individual
            transferArchivo(item_path, os.path.join(to_path, item))
        elif os.path.isdir(item_path):
            # Transferir contenido de la subcarpeta recursivamente
            transferCarpeta(item_path, os.path.join(to_path, item))

    # Imprimir mensaje de información
    bitacoraReturn=bitacora("Output","Transfer", f"Contenido de la carpeta '{folder_name}' transferido exitosamente a '{to_path}'.")
    bitacoraLog(bitacoraReturn)
    write(f"Transfer ejecutando...")
    write(bitacoraReturn)
    print(f"Contenido de la carpeta '{folder_name}' transferido exitosamente a '{to_path}'.")



def transferArchivo(from_path, to_path):
    # Si no existe la carpeta de destino, se crea
    to_folder = os.path.dirname(to_path)
    if not os.path.exists(to_folder):
        os.makedirs(to_folder)

    # Obtener el nombre del archivo de origen
    file_name = os.path.basename(from_path)

    # Verificar si ya existe un archivo con el mismo nombre en la ubicación de destino
    if os.path.exists(to_path):
        # Generar un nuevo nombre de archivo con un contador
        base_name, extension = os.path.splitext(file_name)
        counter = 1
        while True:
            new_file_name = f"{base_name}({counter}){extension}"
            new_file_path = os.path.join(to_folder, new_file_name)
            if not os.path.exists(new_file_path):
                break
            counter += 1

        # Mover el archivo de origen a la ubicación de destino con el nuevo nombre
        shutil.move(from_path, new_file_path)

        # Imprimir mensaje de información
        bitacoraReturn=bitacora("Output","Transfer", f"El archivo '{file_name}' ya existe en la ubicación de destino. Se ha renombrado como '{new_file_name}'.")
        bitacoraLog(bitacoraReturn)
        write(f"Transfer ejecutando...")
        write(bitacoraReturn)
        print(f"El archivo '{file_name}' ya existe en la ubicación de destino. Se ha renombrado como '{new_file_name}'.")
    else:
        # Mover el archivo de origen a la ubicación de destino
        shutil.move(from_path, to_path)
        

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

def write(content):
    with open('app/log/consola.txt', 'a') as file:
        file.write(content)
        file.write('\n')  # Agregar un salto de línea después del contenido
