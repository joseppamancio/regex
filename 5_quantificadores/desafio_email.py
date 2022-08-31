import re

string = '''
Os e-mails dos convidados são:
    - fulano@cod3r.com.br
    - xico@gmail.com
    - joao@empresa.info.br
    - maria_silva@registro.br
    - rafa.sampaio@yahoo.com
'''

print(re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.?[a-zA-Z0-9]+', string))
# ['fulano@cod3r.com.br', 'xico@gmail.com', 'joao@empresa.info.br', 'silva@registro.br', 'sampaio@yahoo.com']

print(re.findall(r'[\w.]+@\w+\.\w+\.?\w{0,2}', string))
# ['fulano@cod3r.com.br', 'xico@gmail.com', 'joao@empresa.info.br', 'maria_silva@registro.br', 'rafa.sampaio@yahoo.com']
