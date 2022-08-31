import re

# para definir uma classe ou conjunto de caracteres usamos []
string = '1,2,3,4,5,6,a.b c!d?e[f'

print(re.findall('[02468]', string))
# ['2', '4', '6']

string = 'João não vai passear na moto.'
print(re.findall('n[aã]', string))
# ['nã', 'na']