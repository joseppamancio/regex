import re
texto = 'Casa bonita é casa amarela da esquina com a rua ACASALAR.'

# ==== Global ==== #
match = re.findall(r'casa', texto)
print(match)
# ['casa']

# ==== IgnoreCase ==== #
match = re.findall(r'casa', texto, re.I)
print(match)
# ['Casa', 'casa', 'CASA']

match = re.findall(r'a b', texto)
print(match)
# ['a b']