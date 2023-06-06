from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import os

def encrypt_password(password,llave):
    key = llave.encode("utf-8")
    cipher = AES.new(key, AES.MODE_ECB)
    padded_password = pad(password.encode("utf-8"), AES.block_size)
    encrypted_password = cipher.encrypt(padded_password)
    encoded_password = b64encode(encrypted_password).decode("utf-8")
    return encoded_password

def decrypt_password(encoded_password,llave):
    key = llave.encode("utf-8")
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_password = b64decode(encoded_password.encode("utf-8"))
    decrypted_password = cipher.decrypt(encrypted_password)
    unpadded_password = unpad(decrypted_password, AES.block_size)
    return unpadded_password.decode("utf-8")




# # Ejemplo de uso
# password = "Alvaro123"

# # Encriptar la contraseña
# encrypted_password = encrypt_password(password)
# print("Contraseña encriptada:", encrypted_password)

# # Desencriptar la contraseña
# decrypted_password = decrypt_password(encrypted_password)
# print("Contraseña desencriptada:", decrypted_password)


