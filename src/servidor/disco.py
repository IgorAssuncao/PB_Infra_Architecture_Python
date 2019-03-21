import psutil

def info_disco():
    disco = psutil.disk_usage('.') # variavel para uso importando funcoes da classe disk_usage do modulo psutil
    total = disco.total # tamanho total do disco
    uso = disco.used # Quantitade de disco em uso
    uso_percentual = disco.percent # imprime percentual usado do disco
    livre = disco.free # Quantidade livre em disco

    return [total, uso, uso_percentual, livre]