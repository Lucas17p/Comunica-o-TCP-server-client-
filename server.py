import socket

# Configuração do Socket (Camadas 3 e 4 do Modelo OSI)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1' 
PORT = 5000

# O Servidor se vincula à porta (Ele é o "Dono" da porta 5000)
server_socket.bind((HOST, PORT))

# O Servidor fica esperando alguém ligar
server_socket.listen(1)
print(f"[*] SERVIDOR: Aguardando conexões em {HOST}:{PORT}...")

# O Servidor aceita a chamada do cliente
client_socket, client_address = server_socket.accept()
print(f"[*] SERVIDOR: Conexão estabelecida com {client_address}!")

while True:
    dados_recebidos = client_socket.recv(1024)
    if not dados_recebidos:
        break
    
    mensagem = dados_recebidos.decode('utf-8')
    print(f"[Mensagem do Cliente]: {mensagem}")
    
    if mensagem.lower() == 'sair':
        break

client_socket.close()
server_socket.close()
print("[*] SERVIDOR: Conexão encerrada.")