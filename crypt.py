import os, random, sys, math

#from Crypto.Cipher import AES


def encrypt(key, filename, input_filename):
    chunksize = 64*1024
    output_filename = "(encrypted)"+filename
    filesize = str(os.path.getsize(filename)).zfill(16)

    for i in range(16):
        IV += chr(random,randint(0, 0xFF))

        encryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(filename, 'rb') as infile:
            with open(outputfile, 'wb') as outfile:
                outfile.write(filesize)
                outfile.write(IV)

                while True:
                    chunk = infile.read(chunksize)

                    if len(chunk) == 0:
                        break
                    elif len(chunk) %16 != 0:
                        chunk += '' *(16 - (len(chunk) % 16))

                    output_filename.write(encryptor.encrypt(chunk))

# encrypting
if '-e' in sys.argv:
    print("ff")

    flag_index = sys.argv.index('-e')
    
    flag_index += 1
    public_key = int(sys.argv[flag_index])
    
    flag_index += 1
    plaintext_filename = int(sys.argv[flag_index])
    
    flag_index += 1
    output_filename = int(sys.argv[flag_index])

    encrypt(public_key, plaintext_filename, output_filename)




# decrypting
if '-d' in sys.argv:
    print("dd")


def decrypt(key, filename):
    chunksize = 64*1024
    outputfile = filename[11:]      #(encrypted) = 11 words

    with open(filename, 'rb') as infile:
        filesize = long(infile.read(16))
        IV = infile.read(16)

        decryptor= AES.new(key, AES.MODE_CBC, IV)

        with open(outputfile, 'wb') as outputfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outputfile.write(decryptor.decrypt(chunk))
            outputfile.truncate(filesize)
