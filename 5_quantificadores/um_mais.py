import re

string1 = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOOOO!'
string2 = 'There is a big fog in NYC'

# + -> um ou mais (pelo menos um 'o')
print(re.findall(r'fogo+', string1, re.I))
# ['fogo', 'FOGO']

print(re.findall(r'fogo+', string2, re.I))
# []


string3 = 'Os números: 0123456789.'
print(re.findall(r'[0-9]', string3))
print(re.findall(r'\d', string3))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print(re.findall(r'[0-9]+', string3))
print(re.findall(r'\d+', string3))
# ['0123456789']