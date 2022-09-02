import re

string = 'O José Simão é muito engraçado... hehehehehehe'

print(re.findall(r'he', string))
# ['he', 'he', 'he', 'he', 'he', 'he']


print(re.search(r'(he){3}', string).group())
# hehehe

print(re.findall(r'(he){3}', string))
# ['he', 'he']



string2 = 'http://www.site.info www.escola.ninja.br google.com.ag'
tuples = re.findall(r'(http:\/\/)?(www\.)?([\w\.-]+)(\w{2,})?', string2)
print(''.join(list(tuples[0])))
print(''.join(list(tuples[1])))
print(''.join(list(tuples[2])))

# http://www.site.info
# www.escola.ninja.br
# google.com.ag
