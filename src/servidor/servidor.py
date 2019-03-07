import os
import socket
import time

host = socket.gethostname()
porta = 9999

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((host, porta))
tcp_server.listen()

print(f'Server de nome {host}, esperando conexao na porta {porta}')
print(f'Caso receba \'fim\' o servidor fechara a conexao')

socket_client, addr = tcp_server.accept()
print(f'Conectado a: {str(addr)}')

running = True
while running:
  msg = socket_client.recv(1024)
  print(msg.decode())
  if msg.decode() == 'fim':
    print('Shutting down connection')
    socket_client.close()
    running = False
  
  resposta = f"""{host}: {msg}""".encode()
  socket_client.send(resposta)
  # time.sleep(1)

tcp_server.close()
