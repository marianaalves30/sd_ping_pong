# client.py
import socket                          # Import socket module

s = socket.socket()                    # Create a socket object
host = socket.gethostname()            # Get local machine name
port = 12345                           # Reserve a port for your service.
buffer_size_in_bits = 1024

print("Conectando-se ao servidor")
s.connect((host, port))
print("Conectado")

while True:
    message = input("Digite uma mensagem: ")  + "\n"
    s.sendall(message.encode())
    if message == "SAIR\n":
      break

    print(f"Mensagem enviada")
    print("Esperando resposta")
    bytes_message = s.recv(buffer_size_in_bits)
    if not bytes_message:
      break
    
    string_message = bytes_message.decode().split("\n")[0]

    print(f"Resposta recebida :{string_message}")

s.close()
print("Desconectando.")
