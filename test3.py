import os


def rsa_encrypt(rsa_key, aes_key):
    key, n = rsa_key
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher

rsa_key =
key = os.urandom(16)
rsa_encrypt(rsa_key,key)