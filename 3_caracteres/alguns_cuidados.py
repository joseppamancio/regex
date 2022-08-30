import re
# cuidado com o tab!

# sem tab configurado na IDE
print(re.findall(r'\s', '	'))
# [' ', ' ', ' ']


# com tab configurado na IDE
print(re.findall(r'\s', '	'))
['\t']


print(re.findall(r'\s', ''))
# []