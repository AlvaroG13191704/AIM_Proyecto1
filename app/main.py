from .scanner.scanner import scan_command_line_create, scan_command_line_configure,scan_command_line_delete,scan_command_line_copy, scan_command_line_transfer, scan_command_line_rename, scan_command_line_modify, scan_command_line_add, scan_command_line_exec
from .scanner.tokens import extract_commands
from .cloud.createStorage import create_cloud
def main():
  # Define a command line string
  command_string = '''
  configure -type->local -encrypt_log->false -encrypt_read->false
  create -name->prueba1.txt -path->/carpeta1/ -body->"Este es el contenido del archivo 1"
  create -namE->"prueba 2.txt" -path->/"carpeta 2"/ -boDy->"Este es el contenido del archivo 2"
  delete -path->/carpeta1/ -name->prueba1.txt
  backup
  '''
  result = extract_commands(command_string)
  for token in result:
    print(token)
    if(token.get("configure")):
      configure, type, encrypt_log, encrypt_read = scan_command_line_configure(token.get("configure"))
      print(f"Command Configure:")
      print(f"Configure: {configure}")
      print(f"Type: {type}")
      print(f"Encrypt Log: {encrypt_log}")
      print(f"Encrypt Read: {encrypt_read} \n")
    elif(token.get("create")):
      create, name, path, body = scan_command_line_create(token.get("create"))
      print(f"Command Line Create:")
      print(f"Create: {create}")
      print(f"Name: {name}")
      print(f"Path: {path}")
      print(f"Body: {body}\n")
      # create the file in the cloud
      #delete the last character of the path 
      create_cloud(bucket_name="iam_project1_bucket", file_data=body, destination_blob_name=f"ARCHIVOS{path[:-1]}{name}")

    elif(token.get("delete")):
      delete, path, name = scan_command_line_delete(token.get("delete"))
      print(f"Command Delete:")
      print(f"Delete: {delete}")
      print(f"Path: {path}")
      print(f"Name: {name}\n")
    

  command_configure = 'Configure -type->local -encrypt_log->false -encrypt_read->false'
  command_line_create1 = 'create -name->prueba1.txt -path->/carpeta1/ -body->"Este es el contenido del archivo 1"'
  command_line_create2 = 'create -namE->"prueba 2.txt" -path->/"carpeta 2"/ -boDy->"Este es el contenido del archivo 2"'
  command_line_delete1 = 'delete -path->/carpeta1/ -name->prueba1.txt'
  command_line_delete2 = 'delete -path->/"carpeta 2"/ '
  command_line_copy1 = 'Copy -from->/carpeta1/prueba1.txt -to->/"carpeta 2"/'
  command_line_copy2 = 'Copy -from->/"carpeta 2"/ -to->/carpeta1/'
  command_line_transfer1 = 'transfer -from->/carpeta1/prueba1.txt -to->/"carpeta 2"/ -mode->"local"'
  command_line_transfer2 = 'transfer -from->/"carpeta 2"/ -to->/carpeta1/ -mode->"cloud"'
  command_line_rename1 = 'renaMe -paTh->/carpeta1/prueba1.txt -name->b1.txt'
  command_line_modify = 'modify -path->/carpeta1/prueba1.txt -body->"este es el nuevo contenido del archivo"'
  command_line_add = 'add -path->/carpeta1/prueba1.txt -body->"este es el nuevo contenido del archivo"'
  command_line_exec = 'exec -path->/home/Desktop/miaejecutable.mia '
  # Scan the command line string
  # configure, type, encrypt_log, encrypt_read = scan_command_line_configure(command_configure)
  # create, name, path, body = scan_command_line_create(command_line_create1)
  # delete, path, name = scan_command_line_delete(command_line_delete1)
  # copy, from_path, to_path = scan_command_line_copy(command_line_copy2)
  # transfer, from_path, to_path, mode = scan_command_line_transfer(command_line_transfer2)
  # rename, path, name = scan_command_line_rename(command_line_rename1)
  # modify, path, body = scan_command_line_modify(command_line_modify)
  # add, path, body = scan_command_line_add(command_line_add)
  # exec, path = scan_command_line_exec(command_line_exec)
  # Print the extracted values

  # print(f"Command Exec:")
  # print(f"Exec: {exec}")
  # print(f"Path: {path}\n")


  # print(f"Command Add:")
  # print(f"Add: {add}")
  # print(f"Path: {path}")
  # print(f"Body: {body}\n")

  # print(f"Command Modify:")
  # print(f"Modify: {modify}")
  # print(f"Path: {path}")
  # print(f"Body: {body}\n")

  # print(f"Command Rename:")
  # print(f"Rename: {rename}")
  # print(f"Path: {path}")
  # print(f"Name: {name}\n")
  

  # print(f"Command Transfer:")
  # print(f"Transfer: {transfer}")
  # print(f"From: {from_path}")
  # print(f"To: {to_path}")
  # print(f"Mode: {mode}\n")

  # print(f"Command Copy:")
  # print(f"Copy: {copy}")
  # print(f"From: {from_path}")
  # print(f"To: {to_path}\n")

  # print(f"Command Delete:")
  # print(f"Delete: {delete}")
  # print(f"Path: {path}")
  # print(f"Name: {name}\n")

  # Print the extracted values
  # print(f"Command Configure:")
  # print(f"Configure: {configure}")
  # print(f"Type: {type}")
  # print(f"Encrypt Log: {encrypt_log}")
  # print(f"Encrypt Read: {encrypt_read} \n")

  # print(f"Command Line Create:")
  # print(f"Create: {create}")
  # print(f"Name: {name}")
  # print(f"Path: {path}")
  # print(f"Body: {body}\n")


  # print(f"\nCommand Line 2:")
  # print(f"Name: {name2}")
  # print(f"Path: {path2}")
  # print(f"Body: {body2}")

#   lexer.input(command_line1)
#   while True:
#       token = lexer.token()
#       if not token:
#           break
#       print(token)

#   lexer.input(command_line2)
#   while True:
#       token = lexer.token()
#       if not token:
#           break
#       print(token)


if __name__ == '__main__':
  main()
