import re

string = 'ABC [abc] a-c 1234'

print(re.findall('[a-c]', string))
# ['a', 'b', 'c', 'a', 'c']

print(re.findall('a-c', string))
# ['a-c']

# INTERVALO USAM A ORDEM DA TABELA UNICODE
print(re.findall('[A-z]', string))
# ['A', 'B', 'C', '[', 'a', 'b', 'c', ']', 'a', 'c']



# ===== ORDEM DA TABELA UNICODE TEM QUE SER RESPEITADA ===== #

# print(re.findall('[a-Z]', string))
# re.error: bad character range a-Z at position 1

# print(re.findall('[4-1]', string))
# re.error: bad character range 4-1 at position 1