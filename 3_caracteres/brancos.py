import re

string = ''' 
ca	r
r	o s!
'''

print(re.findall('ca', string))
# ['ca']

print(re.findall('ca\t', string))
# ['ca\t']

print(re.findall('ca\tr', string))
# ['ca\tr']

print(re.findall('ca\tr\n', string))
# ['ca\tr\n']

print(re.findall('ca\tr\nr', string))
# ['ca\tr\nr']

print(re.findall('ca\tr\nr\t', string))
# ['ca\tr\nr\t']

print(re.findall('ca\tr\nr\to', string))
# ['ca\tr\nr\to']


print(re.findall('ca\tr\nr\to\s', string))
# ['ca\tr\nr\to ']

print(re.findall('ca\tr\nr\to\ss', string))
# ['ca\tr\nr\to s']


print(re.findall('ca\tr\nr\to\ss!', string))
# ['ca\tr\nr\to s!']