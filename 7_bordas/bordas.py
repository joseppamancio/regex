import re
string = 'Romário era um excelente jogador\n, mas hoje é um político questionador'

print(re.findall(r'r', string, re.I)) # Todos 'R'
# ['R', 'r', 'r', 'r', 'r']

print(re.findall(r'^r', string, re.I)) # O caractere '^' fora de um conjunto e não literal quer dizer COMEÇO de linha/string
# ['R']

print(re.findall(r'r$', string, re.I)) # O caractere '$' fora de um conjunto e não literal quer dizer FINAL de linha/string
# ['r']

print(re.findall(r'^r.*r$', string, re.I)) # Problema do DOTALL '\n' não pode ser resolvido com .*
# []

print(re.findall(r'^r[\s\S]*r$', string, re.I)) # Podemos solucionar com [\s\S]*
# ['Romário era um excelente jogador\n, mas hoje é um político questionador']




