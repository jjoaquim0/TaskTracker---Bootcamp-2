"""TaskTracker - Gerenciador de tarefas via linha de comando (Bootcamp II - Fase 2)."""


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
    titulo = input("Título: ").strip()
    descricao = input("Descrição: ").strip()
    prioridade = input("Prioridade (Alta/Média/Baixa): ").strip()
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
