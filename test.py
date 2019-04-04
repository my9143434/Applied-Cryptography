
'''test2 = b"l\x99IKLZ\x10`'\x88\xe6\xef&`=N"
# test1 = bytes(test2, encoding='utf-8')
#print(test1)
#print(type(test1))
print(len(test2))

'''
# import os

# b = os.urandom(16)
# print(type(b))
# print(b)

c = "?ZE.\x84>\xb6\xf2\xd2#x\xc9\x8d\x8e\xa8\xd6"

b = str(c)
print(type(b))
c = bytes(b, encoding='utf-8')

print(type(c))
print(len(c))
print(c)
'''
b = b[2:-1]


print(b)

test3 = "example"
test3 = test3.encode(encoding="gb2312")
print(type(test3))
print(test3)
'''