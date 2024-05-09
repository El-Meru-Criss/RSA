from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket

# Conectar al servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('localhost', 12345))

# Recibir la clave pública del servidor
server_public_key = server.recv(1024)

# Crear un objeto de clave pública RSA
key = RSA.import_key(server_public_key)

# Cifrar el mensaje
cipher = PKCS1_OAEP.new(key)
message = "Hola, servidor!"
encrypted_msg = cipher.encrypt(message.encode())

# Enviar el mensaje cifrado al servidor
server.send(encrypted_msg)
print("Mensaje cifrado enviado al servidor")

# Cerrar la conexión
server.close()
