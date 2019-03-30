from Crypto.Cipher import AES
import os

key = os.urandom(16)


def pad(text):
    while len(text) % 16 != 0:
        text += b' '
    return text


def pad_key(key):
    while len(key) % 16 != 0:
        key += b' '
    return key


aes = AES.new(pad_key(key), AES.MODE_ECB)

text = b'woshijiamineirong'

encrypted_text = aes.encrypt(pad(text))
print(encrypted_text)
