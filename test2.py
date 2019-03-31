import sys

if '-e' in sys.argv:
    print("ff")

    flag_index = sys.argv.index('-e')

    flag_index += 1
    public_key = (sys.argv[flag_index])

    flag_index += 1
    plaintext_filename = (sys.argv[flag_index])

    flag_index += 1
    output_filename = (sys.argv[flag_index])

    print(public_key, plaintext_filename, output_filename)



