import re
string = 'Você precisa responder sim, nao ou nao sei!'

print(re.findall(r'sim|nao sei|nao', string))
# ['sim', 'nao', 'nao sei']