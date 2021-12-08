# server.py
#!/usr/bin/python3.10                       # Server.py file

import socket                               # Import module

s = socket.socket()                         # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 12345                                # Reserve a port for your service.

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))                        # Liga a porta

number_of_connections = 1
buffer_size_in_bits = 1024
cli_connection = None

def chat(cli_connection:socket.socket):
     while True:
            print("Esperando mensagem")
            bytes_message = cli_connection.recv(buffer_size_in_bits)

            if not bytes_message:
                break
            string_message = bytes_message.decode()
            string_message = string_message.split("\n")[0]

            if string_message == "SAIR":
                break
    

            print(f"Mensagem recebida: {string_message}")
            response = input("Digite resposta: ") +"\n"
            cli_connection.sendall(response.encode())
            print("Resposta enviada.")
     
     cli_connection.close()
     print("Conexão encerrada.")
 
# Esperando pela conexão do cliente
s.listen(number_of_connections)
try:
    while True:
        cli_connection: socket.socket
        addr: (str, int)
        # Conectando ao cliente.
        print(f"Esperando conexão")
        cli_connection, addr = s.accept()
        print("Conectado")
        chat(cli_connection)

except KeyboardInterrupt as errorKeyboard:
    print(f"\nclosing server")
    s.close()
    if cli_connection:
        cli_connection.close()
    exit(0)
    
