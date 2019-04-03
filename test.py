import string

text = '[101, 116, 163, 101]'
text = text.strip(string.punctuation)
text = text.replace(" ", "")
text = text.split(',')
print(type(text))
print(text)

text = list(map(int, text))
print(type(text[0]))
'''





print(text[0])
'''