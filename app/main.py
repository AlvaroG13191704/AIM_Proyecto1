# from test.scanner import scan_command_line
from test.libPly import lexer

def main():
  # Define a command line string
  command_line1 = 'create -name->prueba1.txt -path->/carpeta1/ -body->"Este es el contenido del archivo 1"'
  command_line2 = 'create -name->"prueba 2.txt" -path->/"carpeta 2"/ -body->"Este es el contenido del archivo 2"'

  lexer.input(command_line1)
  while True:
      token = lexer.token()
      if not token:
          break
      print(token)

  lexer.input(command_line2)
  while True:
      token = lexer.token()
      if not token:
          break
      print(token)

  # # Scan the command line string
  # name1, path1, body1 = scan_command_line(command_line1)
  # name2, path2, body2 = scan_command_line(command_line2)

  # print(f"Command Line 1:")
  # print(f"Name: {name1}")
  # print(f"Path: {path1}")
  # print(f"Body: {body1}")

  # print(f"\nCommand Line 2:")
  # print(f"Name: {name2}")
  # print(f"Path: {path2}")
  # print(f"Body: {body2}")

if __name__ == '__main__':
  main()
