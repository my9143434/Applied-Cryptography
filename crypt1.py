import string

from Crypto.Cipher import AES
import os
import sys


def pad(text):
    while len(text) % 16 != 0:
        text += '\0'
    return str.encode(text)


def rsa_encrypt(rsa_key, aes_key):
    rsa_key = rsa_key.strip(string.punctuation)
    rsa_key = rsa_key.split(",")

    e = int(rsa_key[0])
    n = int(rsa_key[1])

    aes_key = str(aes_key)
    print(aes_key)

    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** e) % n for char in aes_key]
    # Return the array of bytes
    print("cipher type:", type(cipher))
    return cipher


def aes_encrypt(rsa_key, in_filename, output_file_name):
    aes_key = os.urandom(16)
    aes = AES.new(aes_key, AES.MODE_CBC)
    print("aes key length:", len(aes_key))
    print("aes key type: ", type(aes_key))

    string_aeskey = aes_key.decode("utf-8")
    print("string_aeskey: ", string_aeskey)

    # get message
    text1_file = open(in_filename, "r")
    # it's a string
    lines = text1_file.read()

    encrypted_text = aes.encrypt(pad(lines))
    # aes.encrypt(pad(lines))

    encrypted_key = rsa_encrypt(rsa_key, aes_key)
    print("encrypted key type:", type(encrypted_key))
    entire_message = encrypted_key, 'pac2', encrypted_text

    filename = "%s" % output_file_name
    FILE = open(filename, "w")
    entire_message = str(entire_message)
    FILE.writelines(entire_message)
    FILE.close()

    print("Finish Encryption")

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


def rsa_decrypt(rsa_key, encrypted_key):
    rsa_key = rsa_key.strip(string.punctuation)
    rsa_key = rsa_key.split(",")

    d = int(rsa_key[0])
    n = int(rsa_key[1])

    # print(encrypted_key)
    encrypted_key = encrypted_key.strip(string.punctuation)
    encrypted_key = encrypted_key.replace(" ", "")
    encrypted_key = encrypted_key.split(',')
    # print(type(encrypted_key))
    # print(encrypted_key)

    encrypted_key = list(map(int, encrypted_key))

    plain = [chr((char ** d) % n) for char in encrypted_key]

    aes_key = ''.join(plain)

    msg = bytes()  # New empty byte array
    # Append data to the array
    msg.extend(aes_key)
    print("msg type:", type(msg))

    # Return the array of bytes as a string
    return aes_key


def aes_decrypt(rsa_key, cipher_file, output_filename):
    # get message
    cipher_file = open(cipher_file, "r")
    # it's a string
    cipher_lines = cipher_file.read()
    cipher = cipher_lines.split(", 'pac2', ")

    encrypted_key = cipher[0]
    # print(type(encrypted_key))

    encrypted_key = encrypted_key.split('(')
    encrypted_key = encrypted_key[1]
    # print(encrypted_key)

    aes_key = rsa_decrypt(rsa_key, encrypted_key)


''' # aes_key = str.encode(aes_key)
    aes_key = aes_key[2:-1]
    # aes_key = bytes(aes_key, encoding='utf-8')

    print(aes_key)
    aes_key = aes_key.replace("\\", '')

    aes_key = aes_key.encode(encoding="utf-8")

    print(aes_key)
    print(type(aes_key))
    print(len(aes_key))
    # print(aes_key)
    


    ct_content = cipher[1]
    # print(type(ct_content))

    aes = AES.new(aes_key, AES.MODE_CBC)
    decrypted_text = aes.dencrypt(ct_content)
    print("decrypted text:", decrypted_text)
    '''

if '-d' in sys.argv:
    flag_index = sys.argv.index('-d')

    flag_index += 1
    rsa_key_filename = (sys.argv[flag_index])
    # get message
    rsa_key_file = open(rsa_key_filename, "r")
    # it's a string
    rsa_key_lines = rsa_key_file.read()

    flag_index += 1
    cipher_filename = (sys.argv[flag_index])

    flag_index += 1
    output_filename = (sys.argv[flag_index])

    aes_decrypt(rsa_key_lines, cipher_filename, output_filename)
