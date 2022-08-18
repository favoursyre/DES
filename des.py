from Crypto.Cipher import DES

print("DATA ENCRYPTION STANDARD \n")

key = "hello123"

def pad(text):
    while len(text) % 8 != 0:
        text += " "
    return text

des = DES.new(key, DES.MODE_ECB)
plainText = "I love you and that's all that matters"
padText = pad(plainText)
cipherText = des.encrypt(padText)
decodedText = des.decrypt(cipherText)

print(cipherText)
print(decodedText)
#print(dir(cry.exceptions.utils))