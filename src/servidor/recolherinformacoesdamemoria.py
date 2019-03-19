import psutil
import time

m = psutil.virtual_memory()

def memoria():
    m.total = (round(m.total,2))
    m.disponivel = (round(m.available,2))
    m.uso = (round(m.used,2))
    return[m.total, m.disponivel, m.uso]

def percent_memoria():
    d = ((round(m.total,2)) - (round(m.available,2)))/(m.total * 100)
    return [d]
                                 
def mostra_uso_memoria():
    for i in range(0,100):
        print(round(m.used,2))
        time.sleep(1)


def mostra_disponivel_memoria():
    for i in range(0,100):
        print(round(m.available,2))
        time.sleep(1)

print(percent_memoria())
