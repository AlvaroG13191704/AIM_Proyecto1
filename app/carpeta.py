from datetime import datetime
import os
import shutil
import encriptado as enc
from local.bitacora import bitacora
from cloud.addStorage import add_cloud
from cloud.deleteStorage import delete_cloud
from cloud.modifyStorage import modify_cloud
from cloud.renameStorage import rename_cloud
from cloud.copyStorage import copy_cloud
from cloud.transferStorage import transfer_cloud
from cloud.createStorage import create_cloud
from local.createLocal import create_local
from local.deleteLocal import delete_local
from local.copyLocal import copy_local
from local.transferLocal import transfer_local
from local.renameLocal import rename_local
from local.modifyLocal import modify_local
from local.addLocal import add_local



global bitacoraConfigure
bitacoraConfigure = "false"
global tipo
tipo = ""
global contadorLocal
contadorLocal = 0
global contadorCloud
contadorCloud = 0

def configure(type, log, read, llave):
    comando="Configure"
    if type == None or log == None or read == None:
        tmp = "Error: No se ha configurado el tipo de almacenamiento"
        bitacora("Output", comando, tmp, "", "")
    else:
        global tipo
        tipo = type
        global bitacoraConfigure
        bitacoraConfigure = log
        global archivoConfigure
        archivoConfigure = read
        global llaveConfigure
        llaveConfigure = llave

        tmp = "Archivo configurado exitosamente"
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)



def create(name, body, path):
    comando="Create"
    if tipo == "local":
        tmp = create_local(name, body, path)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
    
    elif tipo == "cloud":
        tmp = create_cloud(body, path, name)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
       
    else:
        tmp = "Error: No se ha configurado el tipo de almacenamiento"
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)



def delete(path, name):
    comando="Delete"
    if tipo == "local":
        tmp = delete_local(path, name)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
    
    elif tipo == "cloud":
        tmp = delete_cloud(path, name)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
    
    else:
        tmp = "Error: No se ha configurado el tipo de almacenamiento"
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)



def copy(from_path, to):
    comando="Copy"
    if tipo == "local":
        tmp = copy_local(from_path, to)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
   
    elif tipo == "cloud":
        tmp = copy_cloud(from_path, to)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
    
    else:
        tmp = "Error: No se ha configurado el tipo de almacenamiento"
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)



def transfer(from_path, to, mode):
    comando="Transfer"
    if tipo == "local":
        tmp = transfer_local(from_path, to, mode)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)

    elif tipo == "cloud":

        if mode == "local":
            # ESCRIBIR ACÁ EL CÓDIGO PARA EL CLOUD A LOCAL
            print("Transferir de cloud a local")

        else:
            tmp = transfer_cloud(from_path, to)
            bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
    
    else:
        tmp = "Error: No se ha configurado el tipo de almacenamiento"
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
        


def rename(path, name):
    comando="Rename"
    if tipo == "local":
        tmp = rename_local(path, name)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
    
    elif tipo == "cloud":
        tmp = rename_cloud(path, name)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
      
    else:
        tmp = "Error: No se ha configurado el tipo de almacenamiento"
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)



def modify(path, body):
    comando="Modify"
    if tipo == "local":
        tmp = modify_local(path, body)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
    
    elif tipo == "cloud":
        tmp = modify_cloud(path, body)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
    
    else:
        tmp = "Error: No se ha configurado el tipo de almacenamiento"
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)



def add(path, body):
    comando="Add"
    if tipo == "local":
        tmp = add_local(path, body)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
    
    elif tipo == "cloud":
        tmp = add_cloud(path, body)
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)
    
    else:
        tmp = "Error: No se ha configurado el tipo de almacenamiento"
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)



def backup():
    comando="Backup"
    if tipo == "local":
        print("Backup LOCAL -- - - - - - - ")
    elif tipo == "cloud":
        print("Backup CLOUD -- - - - - - - ")
    else:
        tmp = "Error: No se ha configurado el tipo de almacenamiento"
        bitacora("Output", comando, tmp, bitacoraConfigure, llaveConfigure)