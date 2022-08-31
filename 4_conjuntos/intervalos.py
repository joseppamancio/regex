import re

string = '1,2,3,4,5,6,a.b c!d?e[f'

print(re.findall('[a-z]', string))
# ['a', 'b', 'c', 'd', 'e', 'f']

print(re.findall('[b-d]', string))
# ['b', 'c', 'd']

print(re.findall('[2-4]', string))
# ['2', '3', '4']

print(re.findall('[A-Z1-3]', string, re.I))
# ['1', '2', '3', 'a', 'b', 'c', 'd', 'e', 'f']