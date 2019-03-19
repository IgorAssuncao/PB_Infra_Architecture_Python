import psutil
import cpuinfo
import time


info = cpuinfo.get_cpu_info()

def info_da_cpu():
    cpu_info = cpuinfo.get_cpu_info()
    arch = info['arch'] #arquitetura
    brand = info['brand'] #nome
    bits = info['bits'] #palavra
    cpu_core = psutil.cpu_count() #número de núcleos lógicos (cores) da CPU
    cpu_threads = psutil.cpu_count(logical=False) #nucleos fisicos
    return [arch, brand, bits, cpu_core, cpu_threads]

def freq_da_cpu():
    freq_total = psutil.cpu_freq() #frequencia total
    freq_uso = (psutil.cpu_freq().current)#frequência em uso
    return [freq_total, freq_uso]

def porc_uso_cpu():
    porc_uso = psutil.cpu_percent(interval=1, percpu=True) # porcentagem de uso por núcleo
    return[porc_uso]

def mostra_uso_cpu():
    return [psutil.cpu_percent()]
