from Crypto.Cipher import AES
# import binascii
import os
import sys
import base64


def pad(text):
    while len(text) % 16 != 0:
        text += '\0'
    return str.encode(text)

'''
def rsa_encrypt(rsa_key, plaintext):
    key, n = rsa_key
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher
'''


def aes_encrypt(rsa_public_key, in_filename, output_filename):
    key = os.urandom(16)
    aes = AES.new(key, AES.MODE_CBC)

    # get message
    text1_file = open(in_filename, "r")
    # it's a string
    lines = text1_file.read()

    encrypted_text = aes.encrypt(pad(lines))
    # aes.encrypt(pad(lines))
    print(encrypted_text)

    '''
    encrypted_key = rsa_encrypt(rsa_public_key, key)
    entire_message = (key, encrypted_key)

    filename = "%s" % output_filename
    FILE = open(filename, "w")
    entire_message = str(entire_message)
    FILE.writelines(entire_message)
    FILE.close()
    

    print("1")
    print(encrypted_text)
    print(entire_message)
    '''


if '-e' in sys.argv:
    flag_index = sys.argv.index('-e')

    flag_index += 1
    public_key = (sys.argv[flag_index])
    flag_index += 1
    plaintext_filename = (sys.argv[flag_index])
    flag_index += 1
    output_filename = (sys.argv[flag_index])

    aes_encrypt(public_key, plaintext_filename, output_filename)
