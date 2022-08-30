import re
string = 'lista de arquivos mp3: jazz.mp3,rock.mp3,podcast.mp3,blues.mp3'
print(re.findall(r'\.mp3', string))
# ['.mp3', '.mp3', '.mp3', '.mp3']

print(re.findall(r'\w+\.mp3', string))
# ['jazz.mp3', 'rock.mp3', 'podcast.mp3', 'blues.mp3']