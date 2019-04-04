from base64 import b64encode
from os import urandom

random_bytes = urandom(16)
print(random_bytes)
print(type(random_bytes))
print(len(random_bytes))
token = b64encode(random_bytes).decode('utf-8')
print(token)
print(type(token))
