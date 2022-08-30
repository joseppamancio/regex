# No início
# Um byte == 8 bits == 256 caracteres
# Engloba, Pontuação, A-Z, a-z, 0-9

# Dois bytes == 16 bits = 65500+ caracteres
# Engloba +Simbolos, +Pontuação, A-Z, a-z, 0-9

# Unicode
# Quantidade de bits variável - Expansível
# Suporta mais de 1 milhão de caracteres
# Atualmente tem 100.000 caracteres atribuidos

# https://unicode-table.com


# para usar unicode no terminal usar o seguinte comando 'chcp 65001'
import re
string = 'aʬc௵d'

print(string)
print(re.findall(r'\u02ac|\u0bf5', string, re.UNICODE)) # print apenas pelo terminal
# ['ʬ', '௵']