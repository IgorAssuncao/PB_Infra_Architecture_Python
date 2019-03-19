import sys
import socket
import pickle

host, port = socket.gethostname(), 9991 

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
    resposta = cliente.recv(1024).decode()
    print(resposta)
    print(pickle.loads(reposta))
    msg = input("""Msg: """)
    cliente.send(msg.encode())

cliente.close()
