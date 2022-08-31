import re

string = 'O João recebeu 120 milhões apostando 6 9 21 23 45 46.'


# para definir um quasntificador, us-se {}
print(re.findall(r'\d{1,2}', string)) # um ou até dois dígitos
# ['12', '0', '6', '9', '21', '23', '45', '46']

print(re.findall(r'[0-9]{2}', string)) # apenas números de dois dígitos
# ['12', '21', '23', '45', '46']

print(re.findall(r'\d{1,}', string)) # um ou máximo de números
# ['120', '6', '9', '21', '23', '45', '46']

print(re.findall(r'\w{7}', string)) # palavras com 7 caracteres
# ['recebeu', 'milhões', 'apostan']

print(re.findall(r'[\wõ]{7,}', string)) # palavras com 7 caracteres incluindo õ e ã
# ['recebeu', 'milhões', 'apostando']