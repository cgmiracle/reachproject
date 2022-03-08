#Decryption of the file

from cryptography.fernet import Fernet

input_file = 'BBC.txt'

encryption_key = 'BBC.txt_filekey.encryption_key.encryption_key'

#Use the key
fernet = Fernet(encryption_key)

#Open the encrypted file
with open(input_file, 'rb') as enc_file:
    encrypted_file = enc_file.read()
    
#Decrypting the file
decrypted_file = fernet.decrypt(encrypted_file)

#Open the file and write the decrypted data
with open(input_file, 'wb') as dec_file:
    dec_file.write(decrypted_file)