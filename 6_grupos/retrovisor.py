import re
string = '<b>Destaque</b><strong>Forte</strong><div>Conteudo</div>'

print(re.findall('<(\w+)>', string))    # Não inclui '< >'
# ['b', 'strong', 'div']

print(re.findall('(<\w+>)', string))    # Inclui '< >'
# ['<b>', '<strong>', '<div>']

print(re.findall(r'<(\w+)>.*<\/\1>', string))    # Retrovisores, \1 representa o resultado do grupo 1
# ['b', 'strong', 'div']

string2 = 'Lentamente é mente muito lenta.'
result = re.findall(r'(lenta)(mente)', string2, re.I)
print(result)
# [('Lenta', 'mente')]
print(''.join(list(result)[0]))
# Lentamente

result2 = re.findall(r'(lenta)(mente).*\2.*\1', string2, re.I)
print(result2)
# [('Lenta', 'mente')]
