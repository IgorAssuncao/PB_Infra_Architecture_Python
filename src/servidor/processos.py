import subprocess, psutil, time, nmap, os

nome = input("Entre com o nome do processo a ser buscado: ")
pid = subprocess.Popen([nome], shell = True).pid
p = psutil.Process(pid)
process = psutil.Process(os.getpid())
lp = psutil.pids()
lista_pid = []

dict_processes = {}

for proc in psutil.process_iter():
    print(proc)
    process_as_dict = proc.as_dict(attrs = ['pid', 'name'])
    dict_processes[process_as_dict['pid']] = process_as_dict['name']

print(dict_processes)

for i in lp:
    p = psutil.Process(i)
    if p.pid == pid:
        lista_pid.append(str(i))


def infoProcesso():
    if len(lista_pid) > 0:
        print(lista_pid)
        for process in dict_processes:
            proc = psutil.Process(process)
            print(proc)
            print("Nome:", proc.name())
            print("Executável:", process.exe())
            print("Tempo de criação:", time.ctime(proc.create_time()))
            print("Tempo de usuário:", process.cpu_times().user, "s")
            print("Tempo de sistema:", process.cpu_times().system, "s")
            print("Percentual de uso de CPU:", process.cpu_percent(interval=1.0), "%")
            perc_mem = '{:.2f}'.format(process.memory_percent())
            print("Percentual de uso de memória:", perc_mem, "%")
            mem = '{:.2f}'.format(process.memory_info().rss/1024/1024)
            print("Uso de memória:", mem, "MB")
            print("Número de threads:", process.num_threads())
        else:
            print(pid, "Não está sendo executado!")

infoProcesso()