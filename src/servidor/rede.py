import psutil, nmap, subprocess, platform, os


rede = psutil.net_io_counters(pernic= False)

print(psutil.net_if_addrs())




def get_rede():
    def retorna_codigo_ping(hostname):
        """Usa o utilitario ping do sistema operacional para encontrar   o host. ('-c 5') indica, em sistemas linux, que deve mandar 5   pacotes. ('-W 3') indica, em sistemas linux, que deve esperar 3   milisegundos por uma resposta. Esta funcao retorna o codigo de   resposta do ping """

        plataforma = platform.system()
        args = []
        if plataforma == "Windows":
            args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]

        else:
            args = ['ping', '-c', '1', '-W', '1', hostname]

        ret_cod = subprocess.call(args,
                                  stdout=open(os.devnull, 'w'),
                                  stderr=open(os.devnull, 'w'))
        return ret_cod


    def verifica_hosts(base_ip):
        """Verifica todos os host com a base_ip entre 1 e 255 retorna uma lista com todos os host que tiveram resposta 0 (ativo)"""
        print("Mapeando\r")
        host_validos = []
        return_codes = dict()
        for i in range(1, 255):

            return_codes[base_ip + '{0}'.format(i)] = retorna_codigo_ping(base_ip + '{0}'.format(i))
            if i % 20 == 0:
                print(".", end="")
            if return_codes[base_ip + '{0}'.format(i)] == 0:
                host_validos.append(base_ip + '{0}'.format(i))
        print("\nMapping ready...")

        return host_validos

    def obter_hostnames(host_validos):
        nm = nmap.PortScanner
        nm.scan(ip_string)
        for i in host_validos:
            try:
                nm.scan(i)
                print("O IP", host, "possui o nome", nm[i].hostname())

            except Exception as error:
                print(error)


    # Chamadas
    ip_string = input("Entre com o ip alvo: ")
    ip_lista = ip_string.split('.')
    base_ip = ".".join(ip_lista[0:3]) + '.'
    print("O teste será feito na sub rede: ", base_ip)
    print("Os host válidos são: ", verifica_hosts(base_ip))
    host_validos = verifica_hosts(base_ip)
    obter_hostnames(host_validos)


    ###############################




    # as 3 primeiras funcoes tive que fazer uma iteracao a lista de rede, pois a info estava meio jogada
    # separei em 3 funcoes diferentes para caso o usuario solicite apenas uma das informacoes


    def getIp(): #extracao da informacao de ip da maquina
        a = psutil.net_if_addrs()
        net = list()

        # Fiz iteracao a lista de itens que a classe me entregava, filtrando apenas o necessario para essa funcao
        for k, v in a.items():
            ip = v[0].address
            ifnet = ip

            net.append(ifnet)

        return net[1]


    def getMask(): #extracao da mascara

        a = psutil.net_if_addrs()
        net = list()
        for k, v in a.items():
            ip = v[0].netmask
            ifnet = ip

            net.append(ifnet)

        return net[1]

    def getMac(): #extracao do endereco de mac
        a = psutil.net_if_addrs()
        net = list()
        for k, v in a.items():
            ip = v[0].address
            ifnet = ip

            net.append(ifnet)

        return net[3]

    # como pedido fiz duas funcoes para bites e duas para gigas (que ainda nao serao utilizadas, mas estao ok)

    # tive que fazer um resgate das informacoes da rede, essa um pouco mais facil, pois nao precisei fazer iteracao a lista

    def infoBytes():

        print(" ------------------------------ -------------------------------")

        #informacoes enviadas em bytes
        print("Bytes enviados: ", rede.bytes_sent, "B")

        #informacoes recebidas em bytes
        print("Bytes recebidos: ", rede.bytes_recv, "B")

        print(" ------------------------------ -------------------------------")

    def infoPacotesRedes():

        #Pacotes enviados em bytes
        print("Pacotes enviados: ", rede.packets_sent, "B")

        #Pacotes recebidos em bytes
        print("Pacotes recebidos: ", rede.packets_recv, "B")

        print(" ------------------------------ -------------------------------")

    # Capitei a informacao da mesma forma que na funcao acima, porem formatada em GB

    def infoGigasRede():

        print("Bytes enviados: ", round(rede.bytes_sent / (1024 * 1024 * 1024), 2), "GB")

        print("Bytes recebidos: ", round(rede.bytes_recv/ (1024 * 1024 * 1024), 2), "GB")

        print(" ------------------------------ -------------------------------")



    def infoGigasPacotes():

        print("Pacotes enviados: ", round(rede.packets_sent / (1024 * 1024 * 1024), 4), "GB")
        print("Pacotes recebidos: ", round(rede.packets_recv / (1024 * 1024 * 1024), 4), "GB")





    #################### Regiao para testes ##########################

    print("Número de IP: ", getIp())

    print("Número da máscara: ", getMask())

    print("Número de MAC: ", getMac())

    infoBytes()

    infoGigasRede()

    infoPacotesRedes()

    infoGigasPacotes()




get_rede()