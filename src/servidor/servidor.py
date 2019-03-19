import socket
import pickle

import recolherinformacoesdacpu
# import recolherinformacoesdamemoria

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
    try:
        msg = socket_client.recv(1024).decode()
        print(msg)
        if msg == """fim""":
            print("""Shutting down connection""")
            socket_client.close()
            running = False
        if msg == """0""":
            resposta = [recolherinformacoesdacpu.info_da_cpu(),
                   recolherinformacoesdacpu.freq_da_cpu(),
                   recolherinformacoesdacpu.mostra_uso_cpu(),
                   recolherinformacoesdacpu.porc_uso_cpu()
                   ]
            aux = str(resposta).encode()
            pickle.dumps(aux)
        #if msg == """1""":



        # resposta = f"""{host}: {msg}""".encode()
        socket_client.send(resposta)
    except Exception as exc:
        socket_client(exc) 

tcp_server.close()
