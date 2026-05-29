import socket

# Configuração do Socket (Camadas 3 e 4 do Modelo OSI)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 5000

# O Cliente TENTA se conectar ao servidor que já deve estar rodando
print(f"[*] CLIENTE: Tentando conectar ao servidor {HOST}:{PORT}...")
client_socket.connect((HOST, PORT))
print("[*] CLIENTE: Conectado com sucesso!")

while True:
    mensagem = input("Digite a mensagem para o servidor (ou 'sair'): ")
    
    # Envia a mensagem convertida em bytes
    client_socket.send(mensagem.encode('utf-8'))
    
    if mensagem.lower() == 'sair':
        break

client_socket.close()
print("[*] CLIENTE: Conexão encerrada.")