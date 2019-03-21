import sys
import socket
import pickle

BYTES = 4096


def tracinhos(cor):
    if cor.lower() == 'azul':
        return '\033[1;34m-\033[0;0m' * 50
    if cor.lower() == 'verde':
        return '\033[1;32m-\033[0;0m' * 50
    if cor.lower() == 'vermelho':
        return '\033[1;31m-\033[0;0m' * 50


def pipe_colorido(cor):
    if cor.lower() == 'azul':
        return '\033[1;34m|\033[0;0m'
    if cor.lower() == 'verde':
        return '\033[1;32m|\033[0;0m'
    if cor.lower() == 'vermelho':
        return '\033[1;31m|\033[0;0m'


def mount_menu():
    print()
    print(tracinhos('azul'))
    print("""\033[1;36mProjeto de Bloco\033[0;32m\nOpcoes:\033[0;0m
          0 - Sair
          1 - Informacoes da CPU
          2 - Informacoes da Memoria
          3 - Informacoes do Disco
          4 - Informacoes de Processos
          5 - Informacoes da Rede
          6 - Informacoes de Diretorios""")
    print(tracinhos('azul'))
    print()


def format_resposta(opcao, resposta):
    if opcao == '0':
        print(tracinhos('vermelho'))
        print(
            f"""{pipe_colorido('vermelho')} Conexao encerrada {pipe_colorido('vermelho')}""")
        print(tracinhos('vermelho'))
    if opcao == '1':
        print(tracinhos('verde'))
        print(f"""{pipe_colorido('verde')} CPU: {pipe_colorido('verde')}
          {pipe_colorido('verde')} Nome: {resposta[0]} {pipe_colorido('verde')}
          {pipe_colorido('verde')} Arquitetura: {resposta[1]} bits {pipe_colorido('verde')}
          {pipe_colorido('verde')} Palavra: {resposta[2]} {pipe_colorido('verde')}
          {pipe_colorido('verde')} Quantidade de nucleos: {resposta[3]} {pipe_colorido('verde')}
          {pipe_colorido('verde')} Quantidade de threads: {resposta[4]} {pipe_colorido('verde')}
          {pipe_colorido('verde')} Frequencia minima: {resposta[5]} MHz {pipe_colorido('verde')}
          {pipe_colorido('verde')} Frequencia maxima: {resposta[6]} MHz {pipe_colorido('verde')}
          {pipe_colorido('verde')} Frequencia atual: {resposta[7]} MHz {pipe_colorido('verde')}
          {pipe_colorido('verde')} Porcentagem de uso: {resposta[8]}% {pipe_colorido('verde')}""")
        for i in range(len(resposta[9])):
            print(
                f"""\t  {pipe_colorido('verde')} Porcentagem de uso nucleo {i + 1}: {resposta[9][i]} % {pipe_colorido('verde')}""")
        print(tracinhos('verde'))
    if opcao == '2':
        print(tracinhos('verde'))
        print(f"""{pipe_colorido('verde')} Memoria: {pipe_colorido('verde')}
           {pipe_colorido('verde')} Memoria total: {resposta[0]/1024/1024/1024:.2f} GB {pipe_colorido('verde')}
           {pipe_colorido('verde')} Memoria disponivel: {resposta[1]/1024/1024/1024:.2f} GB {pipe_colorido('verde')}
           {pipe_colorido('verde')} Memoria em uso: {resposta[2]/1024/1024/1024:.2f} GB {pipe_colorido('verde')}
           {pipe_colorido('verde')} Percentual de Uso: {resposta[3]/1024/1024/1024:.2f} GB {pipe_colorido('verde')}
           {pipe_colorido('verde')} Percentual disponivel: {resposta[4]/1024/1024/1024:.2f} GB {pipe_colorido('verde')}""")
        print(tracinhos('verde'))
    if opcao == '3':
        print(tracinhos('verde'))
        print(f"""{pipe_colorido('verde')} Disco: {pipe_colorido('verde')}
          {pipe_colorido('verde')} Armazenamento total: {resposta[0]/1024/1024/1024:.2f} GB {pipe_colorido('verde')}
          {pipe_colorido('verde')} Armazenamento em uso: {resposta[1]/1024/1024/1024:.2f} GB {pipe_colorido('verde')}
          {pipe_colorido('verde')} Percentual em uso: {resposta[2]/1024/1024/1024:.2f} % {pipe_colorido('verde')}
          {pipe_colorido('verde')} Armazenamento disponivel: {resposta[3]/1024/1024/1024:.2f} GB {pipe_colorido('verde')}""")
        print(tracinhos('verde'))
    if opcao == '4':
        print(tracinhos('verde'))
        print(f"""{pipe_colorido('verde')} Processos: {pipe_colorido('verde')}""")
        print(resposta)
        for key, value in resposta.items():
            print(f"""
                {pipe_colorido('verde')} {key}: {pipe_colorido('verde')}
                {pipe_colorido('verde')} Nome: {resposta[0]} {pipe_colorido('verde')}
                {pipe_colorido('verde')} Executavel: {resposta[1]} {pipe_colorido('verde')}
                {pipe_colorido('verde')} Tempo de criacao: {resposta[2]} {pipe_colorido('verde')}
                {pipe_colorido('verde')} Tempo de usuario: {resposta[3]} s {pipe_colorido('verde')}
                {pipe_colorido('verde')} Tempo de sistema: {resposta[4]} s {pipe_colorido('verde')}
                {pipe_colorido('verde')} Percentual de uso da CPU: {resposta[5]:/2f} % {pipe_colorido('verde')}
                {pipe_colorido('verde')} Percentual de uso da memoria: {resposta[6]:/2f} % {pipe_colorido('verde')}
                {pipe_colorido('verde')} Numero de threads: {resposta[7]} {pipe_colorido('verde')}
            """)
        print(tracinhos('verde'))
    if opcao == '5':
        print(tracinhos('verde'))
        print(f"""{pipe_colorido('verde')} Rede: {pipe_colorido('verde')}""")
        for key, value in resposta.items():
            print(f"""
              {pipe_colorido('verde')} {key}: {pipe_colorido('verde')}
                    {pipe_colorido('verde')} IPv4: {value[0][0]} {pipe_colorido('verde')}
                    {pipe_colorido('verde')} Mascara de rede (IPv4): {value[0][1]} {pipe_colorido('verde')}
                    {pipe_colorido('verde')} IPv6: {value[1][0]} {pipe_colorido('verde')}
                    {pipe_colorido('verde')} Mascara de rede (IPv6): {value[1][1]} {pipe_colorido('verde')}
                    {pipe_colorido('verde')} MAC Address: {value[2]} {pipe_colorido('verde')}""")
        print(tracinhos('verde'))


def imprime_status(bytes, tam):
    kbytes = bytes/1024
    tam_bytes = tam/1024
    texto = """Baixando..."""
    texto += f"""{kbytes} KB"""
    texto += f"""de {tam_bytes} KB"""
    print(texto)


opcoes = [str(i) for i in range(10)]

host, port = socket.gethostname(), 9991

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((host, port))
except Exception as error:
    print(error)
    sys.exit(1)

running = True
while running:
    mount_menu()
    try:
        opcao = input("""Opcao: """)
        if opcao not in opcoes:
            print('Opcao invalida, tente novamente')
            mount_menu()
            opcao = input("""Opcao: """)
        cliente.send(opcao.encode())
        resposta = pickle.loads(cliente.recv(BYTES))
        if resposta:
            format_resposta(opcao, resposta)
        if opcao == '0':
            running = False
    except Exception as error:
        print(error)
        running = False

cliente.close()
