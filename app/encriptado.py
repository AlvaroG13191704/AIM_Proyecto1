from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii
import os

def encrypt_password(password, llave):
    key = llave.encode("utf-8")
    cipher = AES.new(key, AES.MODE_ECB)
    padded_password = pad(password.encode("utf-8"), AES.block_size)
    encrypted_password = cipher.encrypt(padded_password)
    encoded_password = binascii.hexlify(encrypted_password).decode("utf-8")
    return encoded_password

def decrypt_password(encoded_password, llave):
    key = llave.encode("utf-8")
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_password = binascii.unhexlify(encoded_password.encode("utf-8"))
    decrypted_password = cipher.decrypt(encrypted_password)
    unpadded_password = unpad(decrypted_password, AES.block_size)
    return unpadded_password.decode("utf-8")





# # Ejemplo de uso
# password = "Alvaro123"
# llave = "miaproyecto12345"

# # Encriptar la contraseña
# encrypted_password = encrypt_password(password, llave)
# print("Contraseña encriptada:", encrypted_password)

# # Desencriptar la contraseña
# decrypted_password = decrypt_password(encrypted_password, llave)
# print("Contraseña desencriptada:", decrypted_password)


