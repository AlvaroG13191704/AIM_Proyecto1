from .scanner.scanner import scan_command_line_create, scan_command_line_configure
# from test.libPly import lexer

def main():
  # Define a command line string
  command_configure = 'Configure -type->local -encrypt_log->false -encrypt_read->false'
  command_line_create1 = 'create -name->prueba1.txt -path->/carpeta1/ -body->"Este es el contenido del archivo 1"'
  command_line_create2 = 'create -name->"prueba 2.txt" -path->/"carpeta 2"/ -body->"Este es el contenido del archivo 2"'

  # Scan the command line string
  configure, type, encrypt_log, encrypt_read = scan_command_line_configure(command_configure)
  create, name, path, body = scan_command_line_create(command_line_create2)
    
  # Print the extracted values
  print(f"Command Configure:")
  print(f"Configure: {configure}")
  print(f"Type: {type}")
  print(f"Encrypt Log: {encrypt_log}")
  print(f"Encrypt Read: {encrypt_read} \n")

  print(f"Command Line Create:")
  print(f"Create: {create}")
  print(f"Name: {name}")
  print(f"Path: {path}")
  print(f"Body: {body}\n")

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
