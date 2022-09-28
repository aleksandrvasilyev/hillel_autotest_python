mystring = 'It has survived not only five centuries, but also the leap into electronic typesetting'

res = 0
for word in mystring.split(' '):
    if word[-1] == 'o':
        res += 1

print(res)