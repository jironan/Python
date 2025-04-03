import random
import string

chars = string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

#Encryption

random.shuffle(key)
plain_text = input("Enter your message to encrypt: ")
enc = ""
for letter in plain_text:
    
    encrypted = chars.index(letter)
    enc += key[encrypted]

print(f"Encrypted: {enc}")

#Decryption
encrypted_text = input("Enter you encrypted text: ")
plain_text = ""

for letter in encrypted_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"decrypted: {plain_text}")
