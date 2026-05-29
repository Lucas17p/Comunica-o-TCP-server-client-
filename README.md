# 🌐 Comunicação TCP Server-Client (Modelo OSI)

Este é um projeto prático desenvolvido em Python para demonstrar o funcionamento das camadas do **Modelo OSI** através de uma arquitetura Cliente-Servidor utilizando sockets TCP. 

O objetivo principal é sair da teoria dos livros e visualizar como os dados são estruturados, endereçados e transmitidos através de uma rede de computadores.

---

## 🛠️ Como o Modelo OSI é aplicado neste projeto?

Embora o sistema operacional gerencie as camadas inferiores, o código foi estruturado para representar o fluxo conceitual do modelo:

* **Camada 7 (Aplicação):** Interface de linha de comando (CLI) onde o usuário interage, digita as mensagens no `client.py` e visualiza o recebimento no `server.py`.
* **Camada 4 (Transporte):** Utilização do protocolo **TCP** (`socket.SOCK_STREAM`) para garantir a entrega confiável e ordenada das mensagens, gerenciando portas de comunicação (Porta padrão: `5000`).
* **Camada 3 (Rede):** Endereçamento e roteamento IP utilizando o protocolo IPv4 (`socket.AF_INET`) apontando para a interface de loopback local (`127.0.0.1`).
* **Camadas 2 e 1 (Enlace e Física):** Abstraídas pelo Sistema Operacional através da placa de rede virtual (*Loopback Adapter*) e processamento direto em memória.

---

## 🚀 Como Executar o Projeto

Certifique-se de ter o Python instalado na sua máquina.

1. **Inicie o Servidor:**
   Abra um terminal (CMD/PowerShell) na pasta do projeto e execute:
   ```bash
   python server.py
O servidor ficará em modo de escuta aguardando conexões.

Inicie o Cliente:
Abra um segundo terminal na mesma pasta e execute:

Bash
python client.py
Envie mensagens:
Digite qualquer mensagem no terminal do cliente e veja ela ser entregue em tempo real no terminal do servidor. Digite sair para encerrar.

📈 Próximos Passos (Roadmap)
[ ] Camada 6 (Apresentação): Implementar criptografia em Base64 ou Cifra de César para os dados não viajarem em texto puro.

[ ] Camada 5 (Sessão): Adicionar gerenciamento de múltiplos clientes simultâneos usando multithreading e controle de timeout de conexão.

💡 Projeto desenvolvido para fins de estudo sobre Redes de Computadores e Sistemas Distribuídos.