mystring = 'It has survived not onlyО fiveО centuries, but also the leap into electronic typesetting'

res = 0
for word in mystring.split(' '):
    if word[-1] in ['o', 'O', 'о', 'О']:
        res += 1

print(res)