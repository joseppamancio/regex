import re

string = 'Bom\ndia'
print(re.findall(r'.', string, re.I)) # Não conseguiu resolver o \n
# ['B', 'o', 'm', 'd', 'i', 'a']

string = 'Bom\tdia'
print(re.findall(r'.', string, re.I))
# ['B', 'o', 'm', '\t', 'd', 'i', 'a']

string = 'Bom\ndia' 
print(re.findall(r'...', string, re.I)) # Não conseguiu resolver o \n
# ['Bom', 'dia']

string = 'Bom\ndia'
print(re.findall(r'....', string, re.I)) # Não conseguiu resolver o \n
# []

string = 'Bom\ndia' 
print(re.findall(r'....', string, re.S)) # Conseguiu resolver o \n com a Flag S
# ['Bom\n']
