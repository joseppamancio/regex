import re

string = '1,2,3,a.b c!d?e[f'

#NÃO DIGITOS
print(re.findall(r'\D', string))
print(re.findall(r'[^\d]', string))
print(re.findall(r'[^0-9]', string))
# [',', ',', ',', 'a', '.', 'b', ' ', 'c', '!', 'd', '?', 'e', '[', 'f']

# Eliminando Pontuações
print(re.findall(r'[^\d!\?\[\s,\.]', string))
# ['a', 'b', 'c', 'd', 'e', 'f']




numeros = '1: !"#$%&\'()*+,-./ 2: :;<=>?@'
# Dois Intervalos Negados
print(re.findall(r'[^!-/:-@\s]', numeros))
# ['1', '2']