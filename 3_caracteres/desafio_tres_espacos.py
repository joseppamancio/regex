import re
string = 'a   b'

print(re.findall(r'a   b', string))
print(re.findall(r'a\s\s\sb', string))

# Um ou mais espaços em branco
print(re.findall(r'a\s+b', string))

# Alguma coisa entreos caracteres
print(re.findall(r'a...b', string))

# Multiplicando Caracteres 3 vezes
print(re.findall(r'a\s{3}b', string))