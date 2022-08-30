import re

texto = '1,2,3,4,5,6,a.b c!d?e'

# /,/
regex_vigula = ','
print(texto.split(regex_vigula))
# ['1', '2', '3', '4', '5', '6', 'a.b c!d?e']

print(re.search(regex_vigula, texto).group(0))
# ,

# /,/g
print(re.findall(regex_vigula, texto))
# [',', ',', ',', ',', ',', ',']

# /a/
print(re.fullmatch(r'a', texto))
# None

# /A/
print(re.fullmatch(r'A', texto))
# None

# /a/g
print(re.findall(r'a', texto))
# ['a']

# /a/g
print(re.findall(r'A', texto))
# []

# /A/gi
print(re.findall(r'A', texto, re.I))
# ['a']

# /b c!d/
print(re.findall(r'b c!d', texto, re.I))
# ['a']
