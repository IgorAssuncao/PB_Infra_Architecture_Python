import os
import sys
import socket

host, port = socket.gethostname(), 9999 

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((host, port))
except Exception as error:
    print(error)
    sys.exit(1)

print(f"""Para sair digite 'fim'""")
msg = input("""Msg: """)
cliente.send(msg.encode())

running = True
while running:
    resposta = cliente.recv(1024)
    print(resposta.decode())
    msg = input("""Msg: """)
    cliente.send(msg.encode())

cliente.close()
