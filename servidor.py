from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket

# Crear un par de claves RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Iniciar el servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("Servidor escuchando en el puerto 12345")

# Aceptar conexiones de clientes
client_socket, client_address = server.accept()
print(f"Conexión establecida desde {client_address}")

# Enviar la clave pública al cliente
client_socket.send(public_key)

# Recibir el mensaje cifrado del cliente
encrypted_msg = client_socket.recv(1024)

# Imprimir el mensaje encriptado
print("Mensaje encriptado:", encrypted_msg)

# Crear un objeto de cifrado
cipher = PKCS1_OAEP.new(key)

# Descifrar el mensaje
decrypted_msg = cipher.decrypt(encrypted_msg)
print("Mensaje descifrado:", decrypted_msg.decode())

# Cerrar la conexión
client_socket.close()
server.close()