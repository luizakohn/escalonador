import csv

# Representação de uma tarefa
class Tarefa:
    def __init__(self, id, quantum, cpus_necessarias, duracao_total):
        self.id = id
        self.quantum = quantum
        self.cpus_necessarias = cpus_necessarias
        self.duracao_restante = duracao_total
        self.duracao_total = duracao_total

CPUS = [ [] for _ in range(4) ]  # cpu0, cpu1, cpu2, cpu3

def ordenar_tarefas(lista_tarefas):
    n = len(lista_tarefas)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Ordena em ordem decrescente de quantum
            if lista_tarefas[j].quantum < lista_tarefas[j + 1].quantum:
                lista_tarefas[j], lista_tarefas[j + 1] = lista_tarefas[j + 1], lista_tarefas[j]
    return lista_tarefas


def simular_escalonador(lista_tarefas):
    fila = ordenar_tarefas(lista_tarefas)
    
    index_tempo = 0
    while fila:

        # Verifica quais CPUs estão livres agora
        cpus_disponiveis = []
        for i, cpu in enumerate(CPUS):
            if index_tempo >= len(cpu) or not cpu[index_tempo]:
                cpus_disponiveis.append(i)

        lista_tarefas_refeita = []
        lista_tarefas_volta_fila = []
        for i in range(len(fila)):
            if len(cpus_disponiveis) < fila[i].cpus_necessarias: 
                lista_tarefas_refeita.append(fila[i])
                continue
            tarefa = fila[i]
            tempo_execucao = min(tarefa.quantum, tarefa.duracao_restante)
            for _ in range(tarefa.cpus_necessarias):
                cpu_em_uso = cpus_disponiveis.pop(0)
                for _ in range(tempo_execucao // 5):
                    CPUS[cpu_em_uso].append(tarefa.id)
            tarefa.duracao_restante -= tempo_execucao
            if tarefa.duracao_restante > 0:
                lista_tarefas_volta_fila.append(tarefa)
        lista_tarefas_refeita.extend(lista_tarefas_volta_fila)  
        fila = ordenar_tarefas(lista_tarefas_refeita) 
        index_tempo += 1

    # Exibir resultados
    with open('resultado_escalonador.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["CPU;Tarefas"])
        for i, cpu in enumerate(CPUS):
            writer.writerow([f'CPU{i};', '; '.join(map(str, cpu))])

    max_length = max(len(cpu) for cpu in CPUS)
    print(f"Tempo decorrido: {max_length * 5} segundos")

LISTA_VM_1 = [
    Tarefa("T1", 15, 1, 30),
    Tarefa("T2", 20, 2, 60),
    Tarefa("T3", 15, 4, 40),
    Tarefa("T4", 10, 1, 20),
    Tarefa("T5", 10, 2, 30),
    Tarefa("T6", 20, 4, 50),
    Tarefa("T7", 15, 2, 40),
    Tarefa("T8", 10, 1, 60),
    Tarefa("T9", 20, 2, 40),
    Tarefa("T10", 15, 1, 20)
]

simular_escalonador(LISTA_VM_1)