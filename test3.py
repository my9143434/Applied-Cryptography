import string


item = "([380030, 48699, 190089, 168441, 156216, 158203, 365915, 29462, 250411, 158203, 365915, 29462, 2905, 37248, 158203, 365915, 2905, 201171, 158203, 365915, 285783, 29462, 158203, 365915, 242810, 380030, 158203, 365915, 263908, 263908, 29462, 158203, 365915, 204164, 285783, 158203, 365915, 29462, 230431, 158203, 365915, 263908, 380030, 263908, 274803, 48699], 'pac2', b'_\xc8\xf2\xf9\xc9L\xeat -\xa7\xec\xc6g\x19+\x0exO\xe9\x88L\x02\x08\x8fyu%PJ?\xc4fp\xf2\xdc0g\xb7\x01\xca\xcf\x7fj\xe4I\xdc\xec')"
item = item.strip(string.punctuation)
item = item.split(", 'pac2', ")

encrypted_key = item[0]
ct = item[1]

print('item0:', item[0])
print('item1:', item[1])