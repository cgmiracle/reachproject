#Import BBCNews() to get txt file to encrypt
#import article_api_py

#article_api_py.BBCNews()

input_file = "BBC.txt"

#Source of cryptography module:
#https://github.com/pyca/cryptography

#Guide to create encryption tool:
#https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/

#Importing a module that encrypts files 
from cryptography.fernet import Fernet

#Generate a key that will be used to encrpyt the file
encryption_key = Fernet.generate_key()

#Store the generated key in as file
with open(input_file+'_'+'filekey.encryption_key', 'wb') as filekey:
    filekey.write(encryption_key)

    #Encryption of the file

#Open the key
with open(input_file+'_'+'filekey.encryption_key', 'rb') as filekey:
    encryption_key = filekey.read()
    
#Use the generated key
fernet = Fernet(encryption_key)

#opening the orginal file to encrypt
with open(input_file, 'rb') as file:
    original_file = file.read()
    
#Encrypt the file using the key
encryption = fernet.encrypt(original_file)

#Open the file and write the encrypted data
with open(input_file, 'wb') as encrypted_file:
    encrypted_file.write(encryption)