import string

from Crypto.Cipher import AES
# import binascii
import os
import sys


def pad(text):
    while len(text) % 16 != 0:
        text += '\0'
    return str.encode(text)


def rsa_encrypt(rsa_key, aes_key):
    print("here is rsa_encrypt")
    print(rsa_key)
    # print("rsa key: ", type(rsa_key))

    rsa_key = rsa_key.strip(string.punctuation)
    # print(rsa_key)
    rsa_key = rsa_key.split(",")
    # print(type(rsa_key))
    # print(rsa_key[0])
    e = int(rsa_key[0])
    n = int(rsa_key[1])
    # print(e*n)

    aes_key = str(aes_key)
    # print(aes_key)

    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** e) % n for char in aes_key]
    # Return the array of bytes
    return cipher


def aes_encrypt(rsa_key, in_filename, output_file_name):
    key = os.urandom(16)
    aes = AES.new(key, AES.MODE_CBC)

    # get message
    text1_file = open(in_filename, "r")
    # it's a string
    lines = text1_file.read()

    encrypted_text = aes.encrypt(pad(lines))
    # aes.encrypt(pad(lines))
    # print(encrypted_text)

    encrypted_key = rsa_encrypt(rsa_key, key)
    entire_message = (encrypted_key, encrypted_text)

    filename = "%s" % output_file_name
    FILE = open(filename, "w")
    entire_message = str(entire_message)
    FILE.writelines(entire_message)
    FILE.close()

    # print(encrypted_text)
    # print(entire_message)


if '-e' in sys.argv:
    flag_index = sys.argv.index('-e')

    flag_index += 1
    rsa_key_filename = (sys.argv[flag_index])
    # get message
    rsa_key_file = open(rsa_key_filename, "r")
    # it's a string
    rsa_key_lines = rsa_key_file.read()

    flag_index += 1
    plaintext_filename = (sys.argv[flag_index])
    flag_index += 1
    output_filename = (sys.argv[flag_index])

    aes_encrypt(rsa_key_lines, plaintext_filename, output_filename)
