import re
from typing import MappingView
tele_num = '1234567890'

m = re.match(pattern='\d\d\d\d\d\d\d\d\d\d', string = tele_num)
print(type(m))
print(MappingView)
print(bool(m))

if m:
    print('match')
else:
    print('no match')

print(m.start())
print(m.end())
print(m.span())
print(m.group())

tele_num_spaces = '123 456 7890'
m = re.match(pattern='\d{10}', string = tele_num_spaces)
print(m)

if m:
    print('match')
else:
    print('no match')

p = '\d{3}\s?\d{3}\s?\d{4}'
n = re.match(pattern=p, string = tele_num_spaces)
print(n)

q = re.complie('\d{10}')
s = '1234567890'
m = p.match(s)
print(m)