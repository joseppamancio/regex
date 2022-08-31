import re

string = '.$+*?-'

# dentro de um conjunto não precisamos colocar o '\' para informar que é um caractere literal
print(re.findall(r'[.]', string))
# ['.']

print(re.findall(r'[.].', string))
# ['.$']

print(re.findall(r'[+.?*$]', string))
# ['.', '$', '+', '*', '?']

print(re.findall(r'[+.?*$].', string))
# ['.$', '+*', '?-']

# USANDO INTERVALOS COM META CARACTERES
print(re.findall(r'[$-?]', string))
# ['.', '$', '+', '*', '?', '-']


# NÃO É UM INTERVALO
print(re.findall('[$\-?]', string))
# ['$', '?', '-']

print(re.findall('[-?]', string))
# ['?', '-']

# PRECISA DE ESCAPE DENTRO NO CONJUNTO
# - [ ] 