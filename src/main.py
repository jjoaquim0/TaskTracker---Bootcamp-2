"""TaskTracker - Gerenciador de tarefas via linha de comando (Bootcamp II - Fase 2)."""

# Prioridades aceitas: o que o usuário digita (em minúsculas) -> como fica salvo
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


def ler_titulo():
    """Pede o título até que seja informado um valor não vazio."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode ficar vazio. Tente novamente.")


def ler_prioridade():
    """Pede a prioridade até que seja Alta, Média (ou Media) ou Baixa."""
    while True:
        prioridade = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
        if prioridade in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[prioridade]
        print("Erro: prioridade inválida. Digite apenas Alta, Média ou Baixa.")


def exibir_menu():
    """Mostra as opções do menu principal."""
    print("\n" + "=" * 40)
    print("            TASKTRACKER")
    print("=" * 40)
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicação")
    print("=" * 40)


def cadastrar_tarefa(tarefas):
    """Pede os dados da tarefa ao usuário e salva na lista."""
    print("\n--- Cadastro de tarefa ---")
    titulo = ler_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    """Mostra todas as tarefas cadastradas."""
    print("\n--- Tarefas cadastradas ---")
    for tarefa in tarefas:
        print(tarefa)


def main():
    """Loop principal: mostra o menu até o usuário escolher sair."""
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("\nObrigado por usar o TaskTracker. Até logo!")
            break
        else:
            print("\nOpção inválida! Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
