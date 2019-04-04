import os


aes_key = os.urandom(16)
print(type(aes_key))
print(aes_key)

filename = "temp"

FILE = open(filename, "wb")
FILE.writelines(aes_key)
FILE.close()

read_aes_key = open(filename, "rb")
rsa_key = read_aes_key.read()

print(type(rsa_key))


'''

str1 = b'\xe7z\x99\xc3d\xe9\x8f\xa8T\x04\x8f7\x1e\x1bW\xe6'
print(type(str1))

filename = "temp"

FILE = open(filename, "wb")
FILE.writelines(str1)
FILE.close()

read_aes_key = open(filename, "r")
rsa_key = read_aes_key.read()

print(type(rsa_key))
'''