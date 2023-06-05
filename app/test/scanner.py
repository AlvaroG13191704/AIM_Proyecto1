import re

def scan_command_line(command_line):
  # Define regular expressions for matching different components
  pattern_name = r'-name->(.*?)\s'
  pattern_path = r'-path->(.*?)\s'
  pattern_body = r'-body->"(.*?)"'

  # Match the components using regular expressions
  match_name = re.search(pattern_name, command_line)
  match_path = re.search(pattern_path, command_line)
  match_body = re.search(pattern_body, command_line)

  # Extract the values from the matches
  name = match_name.group(1) if match_name else None
  path = match_path.group(1) if match_path else None
  body = match_body.group(1) if match_body else None

  # Return the extracted values
  return name, path, body
