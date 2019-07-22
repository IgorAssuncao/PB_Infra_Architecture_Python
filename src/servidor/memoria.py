import psutil

def info_memoria():
    m = psutil.virtual_memory()
    total = m.total
    disponivel = m.available
    uso = m.used
    percentual_uso = (total - disponivel) / total * 10
    percentual_disponivel = (total - uso) / total * 10
    return [total, disponivel, uso, percentual_uso, percentual_disponivel]