# . é um coringa, válido para uma posição

import re

string = '1,2,3,4,5,6,7,8,9,0'

print(re.findall('1.2', string)) # ponto significa qualquer coisa no meio
# ['1,2']

print(re.findall('1..2', string))
# []

print(re.findall('1..,', string))
# ['1,2,']

notas = '8.3,7.1,8.8,10.0'
print(re.findall('8..', notas))
# ['8.3', '8.8']

print(re.findall(r'.\..', notas))
# ['8.3', '7.1', '8.8', '0.0']