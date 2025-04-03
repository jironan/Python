import random
import string 


chars = string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars )
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

# ENCRYPTION

plain_text = input ("Enter a message to encrypt: ")
cipher_text = ""

for  letter in plain_text:
     index = chars.index(letter)
     cipher_text += key[index]
print(f"ORiginal message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# ENCRYPTION

cipher_text = input ("Enter a message to decrypt: ")
plain_text = ""

for  letter in cipher_text:
     index = key.index(letter)
     plain_text += chars[index]
print(f"ORiginal message: {cipher_text}")
print(f"Encrypted message: {plain_text}")
