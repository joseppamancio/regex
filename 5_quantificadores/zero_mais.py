import re

string1 = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOOOO!'
string2 = 'There is a big fog in NYC'

# + -> zero ou mais (um ou nenhum 'o')
print(re.findall(r'fogo*', string1, re.I))
# ['fogo', 'FOGOOOOOO']

print(re.findall(r'fogo*', string2, re.I))
# ['fog']