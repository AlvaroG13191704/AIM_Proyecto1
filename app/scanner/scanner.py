import re

# Scan configure command line
def scan_command_line_configure(command_line):
  # Define regular expressions for matching different components
  pattern_configure = r'Configure\s'
  pattern_type = r'-type->(.*?)\s'
  pattern_encrypt_log = r'-encrypt_log->(.*?)\s' # \s is a whitespace character
  pattern_encrypt_read = r'-encrypt_read->(.*?)(\s|$)' # $ is the end of the string

  # Match the components using regular expressions
  match_configure = re.search(pattern_configure, command_line)
  match_type = re.search(pattern_type, command_line)
  match_encrypt_log = re.search(pattern_encrypt_log, command_line)
  match_encrypt_read = re.search(pattern_encrypt_read, command_line)

  # Extract the values from the matches
  configure = match_configure.group(0) if match_configure else None
  type = match_type.group(1) if match_type else None
  encrypt_log = match_encrypt_log.group(1) if match_encrypt_log else None
  encrypt_read = match_encrypt_read.group(1) if match_encrypt_read else None

  # Return the extracted values
  return configure,type, encrypt_log, encrypt_read

# Scan create command line
def scan_command_line_create(command_line):
  # Define regular expressions for matching different components
  pattern_create = r'create\s'
  pattern_name = r'-name->(?:"([^"]+)"|(\S+))\s'
  pattern_path = r'-path->(?:"([^"]+)"|/([^/]+/)+)\s'
  pattern_body = r'-body->"(.*?)"'

  # Match the components using regular expressions
  match_create = re.search(pattern_create, command_line)
  match_name = re.search(pattern_name, command_line)
  match_path = re.search(pattern_path, command_line)
  match_body = re.search(pattern_body, command_line)

  # Extract the values from the matches
  create = match_create.group(0) if match_create else None
  name = match_name.group(1) or match_name.group(2) if match_name else None
  path = None
  try:
    if match_path and match_path.group() is not None:
      path = match_path.group().split("->")[1].replace('"', '')
  except AttributeError:
    path = None

  body = match_body.group(1) if match_body else None

  # Return the extracted values
  return create, name, path, body
