from Crypto.Cipher import AES
#秘钥,此处需要将字符串转为字节
key = b'abcdefgh'
#加密内容需要长达16位字符，所以进行空格拼接
def pad(text):
    while len(text) % 16 != 0:
        text += b' '
    return text
#加密秘钥需要长达16位字符，所以进行空格拼接
def pad_key(key):
    while len(key) % 16 != 0:
        key += b' '
    return key
#进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
aes = AES.new(pad_key(key), AES.MODE_ECB)
#加密内容,此处需要将字符串转为字节
text = b'woshijiamineirong'
#进行内容拼接16位字符后传入加密类中，结果为字节类型
encrypted_text = aes.encrypt(pad(text))
print(encrypted_text)
