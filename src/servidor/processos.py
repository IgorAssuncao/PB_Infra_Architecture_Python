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
        detalhes_processo = [proc.name(),
                             proc.exe(),
                             time.ctime(proc.create_time()),
                             proc.cpu_times().user,
                             proc.cpu_times().system,
                             proc.cpu_percent(),
                             proc.memory_percent(),
                             proc.memory_info()
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
