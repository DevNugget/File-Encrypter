from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Ask user to save the key to a file
print("Saving key to file.")
print("Use key to encrypt and decrypt files.")
file_name = input("Enter filename >> ")

# Write the generated key to file specified by user
with open(file_name + ".key", "wb") as filekey:
    filekey.write(key)

print("NOTE: Do not share the file key unless trusted!")
