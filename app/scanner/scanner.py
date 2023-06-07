import re

# Scan configure command line
def scan_command_line_configure(command_line):
  # Define regular expressions for matching different components
  pattern_configure = r'Configure\s'
  pattern_type = r'-type->(.*?)\s'
  pattern_encrypt_log = r'-encrypt_log->(.*?)\s' # \s is a whitespace character
  pattern_encrypt_read = r'-encrypt_read->(.*?)(\s|$)' # $ is the end of the string

  # Match the components using regular expressions
  match_configure = re.search(pattern_configure, command_line,re.I)
  match_type = re.search(pattern_type, command_line,re.I)
  match_encrypt_log = re.search(pattern_encrypt_log, command_line,re.I)
  match_encrypt_read = re.search(pattern_encrypt_read, command_line,re.I)

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
  pattern_body = r'-body->"(.*?)"(\s|$)' # $ is the end of the string

  # Match the components using regular expressions
  match_create = re.search(pattern_create, command_line,re.I)
  match_name = re.search(pattern_name, command_line,re.I)
  match_path = re.search(pattern_path, command_line,re.I)
  match_body = re.search(pattern_body, command_line,re.I)

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


# Scan delete command line
def scan_command_line_delete(command_line):
  # Define regular expressions for matching different components
  pattern_delete = r'delete\s'
  pattern_path = r'-path->(?:"([^"]+)"|/([^/]+/)+)(\s|$)'
  pattern_name = r'-name->(?:"([^"]+)"|(\S+))(\s|$)' # could come or not

  # Match the components using regular expressions
  match_delete = re.search(pattern_delete, command_line,re.I)
  match_path = re.search(pattern_path, command_line,re.I)
  match_name = re.search(pattern_name, command_line,re.I)

  # Extract the values from the matches
  delete = match_delete.group(0) if match_delete else None
  path = None
  try:
    if match_path and match_path.group() is not None:
      path = match_path.group().split("->")[1].replace('"', '')
  except AttributeError:
    path = None
  # this None could be ambigous, becuase it could come or not
  name = "not coming"
  try:
    if match_name and match_name.group() is not None:
      name = match_name.group().split("->")[1]
  except AttributeError:
    name = None


  # Return the extracted values
  return delete, path, name


# Scan copy command line
def scan_command_line_copy(command_line):
  # Define regular expressions for matching different components
  pattern_copy = r'copy\s'
  pattern_from = r'-from->(?:"([^"]*)"|/([^/]+/?)+)\s'
  pattern_to = r'-to->(?:"([^"]+)"|/([^/]+/)+)(\s|$)'

  # Match the components using regular expressions
  match_copy = re.search(pattern_copy, command_line,re.I)
  match_from = re.search(pattern_from, command_line,re.I)
  match_to = re.search(pattern_to, command_line,re.I)

  # Extract the values from the matches
  copy = match_copy.group(0) if match_copy else None
  from_path = None
  try:
    if match_from and match_from.group() is not None:
      from_path = match_from.group().split("->")[1].replace('"', '').replace(' -to','')
  except AttributeError:
    from_path = None
  to_path = None
  try:
    if match_to and match_to.group() is not None:
      to_path = match_to.group().split("->")[1].replace('"', '')
  except AttributeError:
    to_path = None

  # Return the extracted values
  return copy, from_path, to_path

# Scan transfer command line
def scan_command_line_transfer(command_line):
  # Define regular expressions for matching different components
  pattern_transfer = r'transfer\s'
  pattern_from = r'-from->(?:"([^"]*)"|/([^/]+/?)+)\s'
  pattern_to = r'-to->(?:"([^"]+)"|/([^/]+/)+)(\s|$)'
  pattern_mode = r'-mode->(.*?)(\s|$)'

  # Match the components using regular expressions
  match_transfer = re.search(pattern_transfer, command_line,re.I)
  match_from = re.search(pattern_from, command_line,re.I)
  match_to = re.search(pattern_to, command_line,re.I)
  match_mode = re.search(pattern_mode, command_line,re.I)

  # Extract the values from the matches
  transfer = match_transfer.group(0) if match_transfer else None
  from_path = None
  try:
    if match_from and match_from.group() is not None:
      from_path = match_from.group().split("->")[1].replace('"', '').replace(' -to','')
  except AttributeError:
    from_path = None
  to_path = None
  try:
    if match_to and match_to.group() is not None:
      to_path = match_to.group().split("->")[1].replace('"', '')
  except AttributeError:
    to_path = None

  mode = match_mode.group(1).replace('"','') if match_mode else None

  if mode == "local":
    mode = "local"
  elif mode == "cloud":
    mode = "cloud"
  else:
    mode = None

  # Return the extracted values
  return transfer, from_path, to_path, mode

# Scan rename command line
def scan_command_line_rename(command_line):
  # Define regular expressions for matching different components
  pattern_rename = r'rename\s'
  pattern_path = r'-path->(?:"([^"]*)"|/([^/]+/?)+)\s'
  pattern_new_name = r'-name->(?:"([^"]+)"|(\S+))(\s|$)' # could come or not

  # Match the components using regular expressions
  match_rename = re.search(pattern_rename, command_line,re.I)
  match_path = re.search(pattern_path, command_line,re.I)
  match_new_name = re.search(pattern_new_name, command_line,re.I)

  # Extract the values from the matches
  rename = match_rename.group(0) if match_rename else None
  path = None
  try:
    if match_path and match_path.group() is not None:
      path = match_path.group().split("->")[1].replace('"', '')
  except AttributeError:
    path = None

  new_name = "not coming"
  try:
    if match_new_name and match_new_name.group() is not None:
      new_name = match_new_name.group().split("->")[1]
  except AttributeError:
    new_name = None

  # Return the extracted values
  return rename, path, new_name

# Scan modify command line
def scan_command_line_modify(command_line):
  # Define regular expressions for matching different components
  pattern_modify = r'modify\s'
  pattern_path = r'-path->(?:"([^"]*)"|/([^/]+/?)+)\s'
  pattern_body = r'-body->"(.*?)"(\s|$)' # $ is the end of the string

  # Match the components using regular expressions
  match_modify = re.search(pattern_modify, command_line,re.I)
  match_path = re.search(pattern_path, command_line,re.I)
  match_new_body = re.search(pattern_body, command_line,re.I)

  # Extract the values from the matches
  modify = match_modify.group(0) if match_modify else None
  path = None
  try:
    if match_path and match_path.group() is not None:
      path = match_path.group().split("->")[1].replace('"', '').replace(' -body','')
  except AttributeError:
    path = None

  new_body = match_new_body.group(1) if match_new_body else None

  # Return the extracted values
  return modify, path, new_body

# Scan add command line
def scan_command_line_add(command_line):
  # Define regular expressions for matching different components
  pattern_add = r'add\s'
  pattern_path = r'-path->(?:"([^"]*)"|/([^/]+/?)+)\s'
  pattern_body = r'-body->"(.*?)"(\s|$)' # $ is the end of the string

  # Match the components using regular expressions
  match_add = re.search(pattern_add, command_line,re.I)
  match_path = re.search(pattern_path, command_line,re.I)
  match_new_body = re.search(pattern_body, command_line,re.I)

  # Extract the values from the matches
  add = match_add.group(0) if match_add else None
  path = None
  try:
    if match_path and match_path.group() is not None:
      path = match_path.group().split("->")[1].replace('"', '').replace(' -body','')
  except AttributeError:
    path = None

  new_body = match_new_body.group(1) if match_new_body else None

  # Return the extracted values
  return add, path, new_body


# Scan exec command line
def scan_command_line_exec(command_line):
  # Define regular expressions for matching different components
  pattern_exec = r'exec\s'
  pattern_path = r'-path->(?:"([^"]*)"|/([^/]+/?)+)(\s|$)'

  # Match the components using regular expressions
  match_exec = re.search(pattern_exec, command_line,re.I)
  match_path = re.search(pattern_path, command_line,re.I)

  # Extract the values from the matches
  exec = match_exec.group(0) if match_exec else None
  path = None
  try:
    if match_path and match_path.group() is not None:
      path = match_path.group().split("->")[1].replace('"', '').replace(' -mode','')
  except AttributeError:
    path = None

  # Return the extracted values
  return exec, path