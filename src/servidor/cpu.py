import psutil
import cpuinfo
import time

def info_cpu():
    cpu_info = cpuinfo.get_cpu_info()
    print(cpu_info)
    arch = cpu_info['arch'] #arquitetura
    brand = cpu_info['brand'] #nome
    bits = cpu_info['bits'] #palavra
    cpu_core = psutil.cpu_count() #número de núcleos lógicos (cores) da CPU
    cpu_threads = psutil.cpu_count(logical=False) #nucleos fisicos
    freq_min = psutil.cpu_freq().min #frequencia mininma
    freq_max = psutil.cpu_freq().max #frequencia maxima
    freq_uso = psutil.cpu_freq().current #frequência em uso
    porc_uso = psutil.cpu_percent()
    porc_uso_core = psutil.cpu_percent(interval=1, percpu=True) # porcentagem de uso por núcleo
    return [brand, arch, bits, cpu_core, cpu_threads, freq_min, freq_max, freq_uso, porc_uso, porc_uso_core]

print(info_cpu())
