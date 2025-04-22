import heapq
from collections import deque

# Representação de uma tarefa
class Tarefa:
    def __init__(self, id, quantum, cpus_necessarias, duracao_total):
        self.id = id
        self.quantum = quantum
        self.cpus_necessarias = cpus_necessarias
        self.duracao_restante = duracao_total
        self.duracao_total = duracao_total

    def __lt__(self, other):
        return self.quantum > other.quantum  # maior quantum = maior prioridade

# Inicialização das CPUs
CPUS = [ [] for _ in range(4) ]  # cpu0, cpu1, cpu2, cpu3

# Simulação principal
def simular_escalonador(lista_tarefas):
    tempo = 0
    fila = deque(sorted(lista_tarefas, reverse=True))  # fila com tarefas ordenadas por prioridade

    while fila or any(cpu for cpu in CPUS):
        tarefas_em_execucao = []

        # Libera CPUs após cada quantum
        cpus_livres = [i for i in range(4) if len(CPUS[i]) * 5 == tempo]

        # Verifica quais CPUs estão livres agora
        cpus_ocupadas = set()
        for i, cpu in enumerate(CPUS):
            if len(cpu) * 5 > tempo:
                cpus_ocupadas.add(i)

        cpus_disponiveis = [i for i in range(4) if i not in cpus_ocupadas]

        fila_reativada = deque()

        while fila:
            tarefa = fila.popleft()
            if len(cpus_disponiveis) >= tarefa.cpus_necessarias:
                # Aloca CPUs
                cpus_usadas = cpus_disponiveis[:tarefa.cpus_necessarias]
                for i in cpus_usadas:
                    CPUS[i].append(tarefa.id)
                tempo_execucao = min(tarefa.quantum, tarefa.duracao_restante)
                tarefa.duracao_restante -= tempo_execucao
                tempo += tempo_execucao
                if tarefa.duracao_restante > 0:
                    fila_reativada.append(tarefa)  # volta pra fila se não acabou
            else:
                fila_reativada.append(tarefa)  # não tem CPU suficiente, tenta depois
                break  # se a de maior prioridade não couber, espera

        fila = fila_reativada

    # Exibir resultados
    for i, cpu in enumerate(CPUS):
        print(f"CPU{i}: {cpu}")
    print(f"\nTempo total decorrido: {tempo} segundos")

# 🔧 Exemplo de entrada (pode ser substituído por qualquer LISTA_VM_X)
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
