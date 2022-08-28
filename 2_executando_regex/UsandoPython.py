import re

texto = '0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f'

# ====== O primeiro elemento dentro daquele intervalo ====== #
pattern = re.compile(r'9')
match = re.search(pattern, texto)
print("Posicoes: %s, %s; Valor: %s." % (match.start(), match.end(), match.group(0)))
# Posicoes: 18, 19; Valor: 9.


# ====== Verificando se conjunto existem naquele intervalo ===== #
valores = re.findall(r'[a-f]', texto)
print('Valores: ', valores)
# Valores:  ['a', 'b', 'c', 'd', 'e', 'f']


# ====== Subistituindo o regex ===== #
subs = re.sub(r'[a-f]', 'OK', texto)
print(subs)
# 0,1,2,3,4,5,6,7,8,9,OK,OK,OK,OK,OK,OK
