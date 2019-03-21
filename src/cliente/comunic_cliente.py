import socket, sys, os

# Imprime o status de download
def imprime_status(bytes, tam):
    kbytes = bytes/1024
    tam_bytes = tam/1024
    texto = 'Baixando... '
    texto = texto + '{:<.2f}'.format(kbytes) + ' KB '
    texto = texto + 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
    print(texto)
# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nome_arq = input('Entre com o nome do arquivo: ')

try:
    # Tenta se conectar ao servidor
    s.connect((socket.gethostname(), 9090))
    # Envia o nome do arquivo:
    s.send(nome_arq.encode('ascii'))
    # Recebe o tamanho do arquivo:
    msg = s.recv(12)
    tamanho = int(msg.decode('ascii'))
    # Checa se o arquivo existe no servidor:
    if tamanho >= 0:
        print('baixando arquivo')
        # Gera o arquivo local na pasta download
        arq = open(os.getcwd(), "wb")
        soma = 0
        bytes = s.recv(4096)
        # Escreve o arquivo
        while bytes:
            arq.write(bytes)
            # Impressão do status de download
            soma = soma + len(bytes)
            os.system('cls')
            imprime_status(soma, tamanho)
            bytes = s.recv(4096)
        # Fecha o arquivo
        arq.close()
    else:
        print('Arquivo não encontrado no servidor!')
except Exception as erro:
    
    print(str(erro))
# Fecha o socket
s.close()
input("Pressione qualquer tecla para sair...")