import os
import shutil


def transfer_local(from_path, to):
    from_path = from_path.replace('"', '')
    to = to.replace('"', '')
    from_path = from_path.lstrip('/')
    from_path = from_path.rstrip('/')
    to = to.lstrip('/')
    to = to.rstrip('/')
    from_path_full = os.path.join(os.path.dirname(__file__), "../../Archivos", from_path)
    to_full = os.path.join(os.path.dirname(__file__), "../../Archivos", to)

    if os.path.exists(from_path_full):

        if os.path.isfile(from_path_full):
            tmp = transferArchivo(from_path_full, to_full)
            return (tmp)

        elif os.path.isdir(from_path_full):
            transferCarpeta(from_path_full, to_full)
            return (tmp)

        else:
            return(f"Error: El origen '{from_path_full}' no es una carpeta ni un archivo válido.")

    else:
        return(f"Error: No se encontró la carpeta o archivo '{from_path}' en la ruta especificada.")
        


def transferCarpeta(from_path, to_path):
    if not os.path.exists(to_path):
        os.makedirs(to_path)
    folder_name = os.path.basename(from_path)

    if os.path.exists(os.path.join(to_path, folder_name)):
        return(f"Error: La carpeta '{folder_name}' ya existe en la ubicación de destino.")

    for item in os.listdir(from_path):
        item_path = os.path.join(from_path, item)

        if os.path.isfile(item_path):
            transferArchivo(item_path, os.path.join(to_path, item))

        elif os.path.isdir(item_path):
            transferCarpeta(item_path, os.path.join(to_path, item))

    return(f"Contenido de la carpeta '{folder_name}' transferido exitosamente a '{to_path}'.")



def transferArchivo(from_path, to_path):
    to_folder = os.path.dirname(to_path)
    if not os.path.exists(to_folder):
        os.makedirs(to_folder)

    file_name = os.path.basename(from_path)

    if os.path.exists(from_path):

        if os.path.exists(to_path):
            base_name, extension = os.path.splitext(file_name)
            counter = 1
            while True:
                new_file_name = f"{base_name}({counter}){extension}"
                new_file_path = os.path.join(to_path, new_file_name)
                if not os.path.exists(new_file_path):
                    break
                counter += 1

            shutil.move(from_path, new_file_path)
            return(f"El archivo '{file_name}' ya existe en la ubicación de destino. Se ha copiado como '{new_file_name}'.")
        
        else:
            return(f"El archivo '{file_name}' se ha movido exitosamente.")

    else:
        return(f"Error: No se encontró el archivo de origen '{from_path}'.")