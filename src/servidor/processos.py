import os
import time
import psutil

dict_processes = {}

for proc in psutil.process_iter():
    process_as_dict = proc.as_dict(attrs=['pid', 'name'])
    dict_processes[process_as_dict['pid']] = process_as_dict['name']


def infoProcesso(process):
    proc = psutil.Process(process)
    detalhes_processo = []
    try:
        # print("Nome:", proc.name())
        # print("Executável:", proc.exe())
        # print("Tempo de criação:", time.ctime(proc.create_time()))
        # print("Tempo de usuário:", proc.cpu_times().user, "s")
        # print("Tempo de sistema:", proc.cpu_times().system, "s")
        # print("Percentual de uso de CPU:",
            #   proc.cpu_percent(), "%")
        # perc_mem = '{:.2f}'.format(proc.memory_percent())
        # print("Percentual de uso de memória:", perc_mem, "%")
        # mem = '{:.2f}'.format(proc.memory_info().rss/1024/1024)
        # print("Uso de memória:", mem, "MB")
        # print("Número de threads:", proc.num_threads())

        detalhes_processo = [proc.name(),
                             proc.exe(),
                             time.ctime(proc.create_time()),
                             proc.cpu_times().user,
                             proc.cpu_times().system,
                             proc.cpu_percent(),
                             proc.memory_percent(),
                             proc.memory_info(),
                             proc.num_threads()
                             ]
    except:
        pass

    return detalhes_processo


def info_processos():
    processos = {}
    for process in dict_processes:
        processos[process] = infoProcesso(process)

    processos = {pid: detalhes for (
        pid, detalhes) in processos.items() if len(detalhes) > 1}

    return processos
