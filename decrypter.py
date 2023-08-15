from cryptography.fernet import Fernet 

# Ask user for the decryption key file
filekey_path = input("Enter path to file key >> ")

# Read the decryption key
with open(filekey_path, 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

# Ask user for the file to be decrypted
doc_to_decrypt = input("Enter path to file to be decrypted >> ")

# Read the encrypted file
with open(doc_to_decrypt, 'rb') as enc_file:
    encrypted = enc_file.read()

# Decrypt the file
decrypted = fernet.decrypt(encrypted)

# Overwrite the encrypted file with the decrypted file
with open(doc_to_decrypt, 'wb') as dec_file:
    dec_file.write(decrypted)
