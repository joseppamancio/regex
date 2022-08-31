import re

string = '<div>Conteudo 01</div><div>Conteudo 02</div>'


# ======= FORMA GULOSA (GREEDY)====== # ------------------->> Pega e Junta Tudo
print(re.findall(r'<div>.+<\/div>', string))
# ['<div>Conteudo 01</div><div>Conteudo 02</div>']

print(re.findall(r'<div>.*<\/div>', string))
# ['<div>Conteudo 01</div><div>Conteudo 02</div>']

print(re.findall(r'<div>.{0,100}<\/div>', string))
# ['<div>Conteudo 01</div><div>Conteudo 02</div>']


# ======= FORMA NÃO GULOSA ====== # ------------------->> Completa, e monta o próximo conjunto
print(re.findall(r'<div>.+?<\/div>', string))
# ['<div>Conteudo 01</div>', '<div>Conteudo 02</div>']

print(re.findall(r'<div>.*?<\/div>', string))
# ['<div>Conteudo 01</div>', '<div>Conteudo 02</div>']

print(re.findall(r'<div>.{0,100}?<\/div>', string))
# ['<div>Conteudo 01</div>', '<div>Conteudo 02</div>']
