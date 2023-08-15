from cryptography.fernet import Fernet

# Ask user for the encryption key
filekey_path = input("Enter path to file key >> ")

# Read the encryption key
with open(filekey_path, "rb") as filekey:
    key = filekey.read()

fernet = Fernet(key)

# Ask user for the file to be encrypted
doc_to_encrypt = input("Enter path to document to be encrypted >> ")

# Read original file
with open(doc_to_encrypt, "rb") as file:
    original = file.read()

# Encrypt the file
encrypted = fernet.encrypt(original)

# Overwrite the original file with the encrypted file
with open(doc_to_encrypt, "wb") as encrypted_file:
    encrypted_file.write(encrypted)

print("File encrypted!")
    
