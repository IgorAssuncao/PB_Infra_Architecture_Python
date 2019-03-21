import psutil
import nmap
import subprocess
import platform
import os

rede = psutil.net_io_counters(pernic=False)


def info_rede():
    network_interfaces = psutil.net_if_addrs()
    info_network_interfaces = {}

    for key, value in network_interfaces.items():
        ipv4 = [value[0].address,
                value[0].netmask]

        ipv6 = [value[1].address,
                value[1].netmask]

        mac_address = value[2].address

        info_network_interfaces[key] = [ipv4, ipv6, mac_address]

    return info_network_interfaces


# def get_rede():
#     def retorna_codigo_ping(hostname):
#         """Usa o utilitario ping do sistema operacional para encontrar o host. ('-c 5') indica, em sistemas linux, que deve mandar 5   pacotes. ('-W 3') indica, em sistemas linux, que deve esperar 3   milisegundos por uma resposta. Esta funcao retorna o codigo de   resposta do ping """

#         plataforma = platform.system()
#         args = []
#         if plataforma == "Windows":
#             args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]

#         else:
#             args = ['ping', '-c', '1', '-W', '1', hostname]

#         ret_cod = subprocess.call(args,
#                                   stdout=open(os.devnull, 'w'),
#                                   stderr=open(os.devnull, 'w'))
#         return ret_cod


#     def verifica_hosts(base_ip):
#         """Verifica todos os host com a base_ip entre 1 e 255 retorna uma lista com todos os host que tiveram resposta 0 (ativo)"""
#         print("Mapeando\r")
#         host_validos = []
#         return_codes = dict()
#         for i in range(1, 255):

#             return_codes[base_ip + '{0}'.format(i)] = retorna_codigo_ping(base_ip + '{0}'.format(i))
#             if i % 20 == 0:
#                 print(".", end="")
#             if return_codes[base_ip + '{0}'.format(i)] == 0:
#                 host_validos.append(base_ip + '{0}'.format(i))
#         print("\nMapping ready...")

#         return host_validos

#     def obter_hostnames(host_validos):
#         nm = nmap.PortScanner
#         nm.scan(ip_string)
#         for host in host_validos:
#             try:
#                 nm.scan(host)
#                 print("O IP", host, "possui o nome", nm[host].hostname())

#             except Exception as error:
#                 print(error)


#     # Chamadas
#     ip_string = input("Entre com o ip alvo: ")
#     ip_lista = ip_string.split('.')
#     base_ip = ".".join(ip_lista[0:3]) + '.'
#     print("O teste será feito na sub rede: ", base_ip)
#     print("Os host válidos são: ", verifica_hosts(base_ip))
#     host_validos = verifica_hosts(base_ip)
#     obter_hostnames(host_validos)


#     ###############################


#     # as 3 primeiras funcoes tive que fazer uma iteracao a lista de rede, pois a info estava meio jogada
#     # separei em 3 funcoes diferentes para caso o usuario solicite apenas uma das informacoes


#     #################### Regiao para testes ##########################

#     print("Número de IP: ", getIp())

#     print("Número da máscara: ", getMask())

#     print("Número de MAC: ", getMac())


# get_rede()
