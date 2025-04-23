# Representação de uma tarefa
class Tarefa:
    def __init__(self, id, quantum, cpus_necessarias, duracao_total):
        self.id = id
        self.quantum = quantum
        self.cpus_necessarias = cpus_necessarias
        self.duracao_restante = duracao_total
        self.duracao_total = duracao_total

# Inicialização das CPUs
CPUS = [ [] for _ in range(4) ]  # cpu0, cpu1, cpu2, cpu3

# Função de ordenação personalizada (Bubble Sort)
def ordenar_tarefas(lista_tarefas):
    n = len(lista_tarefas)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Ordena em ordem decrescente de duracao_restante
            if lista_tarefas[j].quantum < lista_tarefas[j + 1].quantum:
                lista_tarefas[j], lista_tarefas[j + 1] = lista_tarefas[j + 1], lista_tarefas[j]
    return lista_tarefas

# Substituindo o deque e sorted por listas e a função de ordenação personalizada
def simular_escalonador(lista_tarefas):
    index_tempo = 0
    fila = ordenar_tarefas(lista_tarefas)  # Ordena a lista de tarefas inicialmente

    while fila or any(cpu for cpu in CPUS):
        # Verifica quais CPUs estão livres agora
        cpus_disponiveis = []
        for cpu in enumerate(CPUS):
            if not cpu[index_tempo]:
                cpus_disponiveis.append(i)

        while fila:
            if len(cpus_disponiveis) >= fila[0].cpus_necessarias:
                tarefa = fila.pop(0)  # Remove o primeiro elemento da lista
                # Aloca CPUs
                cpus_usadas = cpus_disponiveis[:tarefa.cpus_necessarias]
                for i in cpus_usadas:
                    CPUS[i].append(tarefa.id)
                tempo_execucao = min(tarefa.quantum, tarefa.duracao_restante)
                tarefa.duracao_restante -= tempo_execucao
                tempo += tempo_execucao
                if tarefa.duracao_restante > 0:
                    fila.append(tarefa)  # volta pra fila se não acabou
            else:
                break  # se a de maior prioridade não couber, espera

        fila = ordenar_tarefas(fila)  # Reordena a fila reativada
        index_tempo += 1

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
