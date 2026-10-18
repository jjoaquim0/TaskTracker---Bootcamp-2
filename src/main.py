"""TaskTracker - Gerenciador de tarefas via linha de comando (Bootcamp II - Fase 2)."""

from datetime import datetime

# Prioridades aceitas: o que o usuário digita (em minúsculas) -> como fica salvo
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}

STATUS_PENDENTE = "Pendente"
STATUS_CONCLUIDA = "Concluída"


# ---------------------------------------------------------------------------
# Regras de validação
# ---------------------------------------------------------------------------

def titulo_valido(titulo):
    """O título é obrigatório e não pode conter apenas espaços."""
    return bool(titulo.strip())


def normalizar_prioridade(prioridade):
    """Retorna Alta, Média ou Baixa; ou None se a prioridade for inválida."""
    return PRIORIDADES_VALIDAS.get(prioridade.strip().lower())


def data_valida(data):
    """A data deve estar no formato DD/MM/AAAA e existir no calendário."""
    try:
        datetime.strptime(data.strip(), "%d/%m/%Y")
        return True
    except ValueError:
        return False


# ---------------------------------------------------------------------------
# Leitura de dados com repetição até a entrada ser válida
# ---------------------------------------------------------------------------

def ler_titulo():
    """Pede o título até que seja informado um valor não vazio."""
    while True:
        titulo = input("Título: ").strip()
        if titulo_valido(titulo):
            return titulo
        print("Erro: o título é obrigatório e não pode ficar vazio. Tente novamente.")


def ler_prioridade():
    """Pede a prioridade até que seja Alta, Média (ou Media) ou Baixa."""
    while True:
        prioridade = normalizar_prioridade(input("Prioridade (Alta/Média/Baixa): "))
        if prioridade:
            return prioridade
        print("Erro: prioridade inválida. Digite apenas Alta, Média ou Baixa.")


def ler_data_limite():
    """Pede a data limite até que seja uma data válida no formato DD/MM/AAAA."""
    while True:
        data = input("Data limite (DD/MM/AAAA): ").strip()
        if data_valida(data):
            return data
        print("Erro: data inválida. Use o formato DD/MM/AAAA (ex.: 20/10/2026).")


# ---------------------------------------------------------------------------
# Operações do sistema
# ---------------------------------------------------------------------------

def criar_tarefa(identificador, titulo, descricao, prioridade, data_limite):
    """Monta o dicionário da tarefa com status inicial Pendente."""
    return {
        "id": identificador,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": STATUS_PENDENTE,
    }


def cadastrar_tarefa(tarefas, proximo_id):
    """Pede os dados da tarefa, salva na lista e retorna o próximo identificador."""
    print("\n--- Cadastro de tarefa ---")
    titulo = ler_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = ler_prioridade()
    data_limite = ler_data_limite()

    tarefas.append(criar_tarefa(proximo_id, titulo, descricao, prioridade, data_limite))
    print("\nTarefa cadastrada com sucesso!")
    return proximo_id + 1


def contar_por_status(tarefas):
    """Retorna a quantidade de tarefas pendentes e concluídas."""
    pendentes = sum(1 for tarefa in tarefas if tarefa["status"] == STATUS_PENDENTE)
    return pendentes, len(tarefas) - pendentes


def visualizar_tarefas(tarefas):
    """Mostra todas as tarefas cadastradas e o resumo por status."""
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for tarefa in tarefas:
        print(f"\nTarefa #{tarefa['id']}")
        print(f"  Título.......: {tarefa['titulo']}")
        print(f"  Descrição....: {tarefa['descricao'] or 'Sem descrição'}")
        print(f"  Prioridade...: {tarefa['prioridade']}")
        print(f"  Data limite..: {tarefa['data_limite']}")
        print(f"  Status.......: {tarefa['status']}")
        print("-" * 40)

    pendentes, concluidas = contar_por_status(tarefas)
    print(f"Total: {len(tarefas)} | Pendentes: {pendentes} | Concluídas: {concluidas}")


def buscar_tarefa(tarefas, identificador):
    """Procura uma tarefa pelo identificador; retorna None se não existir."""
    for tarefa in tarefas:
        if tarefa["id"] == identificador:
            return tarefa
    return None


def concluir_tarefa(tarefas):
    """Marca uma tarefa pendente como concluída a partir do identificador."""
    print("\n--- Concluir tarefa ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    visualizar_tarefas(tarefas)
    entrada = input("\nInforme o número da tarefa a concluir: ").strip()
    if not entrada.isdigit():
        print("Erro: informe um número válido.")
        return

    tarefa = buscar_tarefa(tarefas, int(entrada))
    if tarefa is None:
        print("Erro: tarefa não encontrada.")
    elif tarefa["status"] == STATUS_CONCLUIDA:
        print("Esta tarefa já está concluída. Nenhuma alteração foi necessária.")
    else:
        tarefa["status"] = STATUS_CONCLUIDA
        print("Tarefa concluída com sucesso!")


# ---------------------------------------------------------------------------
# Menu principal
# ---------------------------------------------------------------------------

def exibir_menu():
    """Mostra as opções do menu principal."""
    print("\n" + "=" * 40)
    print("            TASKTRACKER")
    print("=" * 40)
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Concluir tarefa")
    print("4 - Sair da aplicação")
    print("=" * 40)


def main():
    """Loop principal: mostra o menu até o usuário escolher sair."""
    tarefas = []
    proximo_id = 1

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            proximo_id = cadastrar_tarefa(tarefas, proximo_id)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            print("\nObrigado por usar o TaskTracker. Até logo!")
            break
        else:
            print("\nOpção inválida! Digite 1, 2, 3 ou 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nAplicação encerrada pelo usuário. Até logo!")
