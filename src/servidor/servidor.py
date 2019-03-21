import sys
import datetime
import socket
import pickle

import cpu
import memoria
import disco

def log(opcao, termino=False):
    if opcao == '0':
        if not termino:
            print(f"""[\033[1;32m{datetime.datetime.now().replace(microsecond=0).isoformat(' ')}\033[0;0m] - Encerrando conexao""")
        if termino:
            print(f"""[\033[1;31m{datetime.datetime.now().replace(microsecond=0).isoformat(' ')}\033[0;0m] - Conexao encerrada""")
    if opcao == '1':
        if not termino:
            print(f"""[\033[1;32m{datetime.datetime.now().replace(microsecond=0).isoformat(' ')}\033[0;0m] - Recolhendo informacoes da CPU""")
        if termino:
            print(f"""[\033[1;32m{datetime.datetime.now().replace(microsecond=0).isoformat(' ')}\033[0;0m] - Coleta de informacoes da CPU bem sucedida""")
    if opcao == '2':
        if not termino:
            print(f"""[\033[1;32m{datetime.datetime.now().replace(microsecond=0).isoformat(' ')}\033[0;0m] - Recolhendo informacoes da Memoria""")
        if termino:
            print(f"""[\033[1;32m{datetime.datetime.now().replace(microsecond=0).isoformat(' ')}\033[0;0m] - Coleta de informacoes da Memoria bem sucedida""")

host = socket.gethostname()
port = 9991

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((host, port))
tcp_server.listen()

print(f"""Server de nome {host}, esperando conexao na porta {port}""")
print(f"""Caso receba 'fim' o servidor fechara a conexao""")

socket_client, client_host = tcp_server.accept()
print(f"""Conectado a: {str(client_host)}""")

running = True
while running:
    if not socket_client._closed:
        msg = socket_client.recv(1024).decode()
        if msg == """0""":
            log(msg)
            resposta = 'Conexao encerrada'
            resposta_bytes = pickle.dumps(resposta)
            socket_client.send(resposta_bytes)
            socket_client.close()
            tcp_server.close()
            log(msg, True)
            sys.exit()
        if msg == """1""":
            log(msg)
            resposta = cpu.info_cpu()
            resposta_bytes = pickle.dumps(resposta)
            socket_client.send(resposta_bytes)
            log(msg, True)
        if msg == """2""":
            log(msg)
            resposta = memoria.info_memoria()
            resposta_bytes = pickle.dumps(resposta)
            socket_client.send(resposta_bytes)
            log(msg, True)
        if msg == """3""":
            log(msg)
            resposta = disco.info_disco()
            resposta_bytes = pickle.dumps(resposta)
            socket_client.send(resposta_bytes)
            log(msg, True)
    if socket_client._closed:
        print('Socket closed')
        running = False

tcp_server.close()
