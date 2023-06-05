from ply import lex

# Define the tokens
tokens = (
  'CREATE',
  'NAME',
  'PATH',
  'BODY',
)

# Regular expression rules for tokens

def t_CREATE(t):
  r'create\s'
  return t

def t_NAME(t):
  r'-name->(.*?)\s'
  t.value = t.value[7:].strip()
  return t

def t_PATH(t):
  r'-path->(.*?)\s'
  t.value = t.value[7:].strip()
  return t

def t_BODY(t):
  r'-body->"(.*?)"'
  t.value = t.value[7:-1]
  return t

# Ignored characters (whitespace)
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
  print(f"Illegal character: {t.value[0]}")
  t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
