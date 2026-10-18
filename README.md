# TaskTracker

Sistema simples de gerenciamento de tarefas via linha de comando (CLI), desenvolvido em Python 3
como projeto cumulativo do **Bootcamp II**.

## 📌 Descrição

O TaskTracker ajuda a organizar as tarefas do dia a dia. Pelo terminal, o usuário pode:

- **Cadastrar** uma tarefa com título, descrição, prioridade e data limite;
- **Visualizar** todas as tarefas cadastradas de forma organizada;
- **Sair** da aplicação.

O planejamento lógico completo (Fase 1) está em [`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf).

## 🗂️ Estrutura do repositório

```
tasktracker-projeto/
├── README.md                    # Documentação principal da aplicação e instruções de uso
├── .gitignore                   # Regras para ignorar arquivos temporários do Python e ambiente virtual
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico e arquitetural entregue na Fase 1
└── src/
    └── main.py                  # Código-fonte principal da aplicação TaskTracker
```

## 🛠️ Tecnologias

- Python 3
- Git e GitHub

## ✅ Regras de negócio

| Campo | Regra |
|-------|-------|
| Título | Obrigatório. Entradas vazias ou só com espaços são rejeitadas e o sistema pede de novo. |
| Descrição | Livre (pode ficar em branco). |
| Prioridade | Aceita apenas **Alta**, **Média** (ou **Media**) e **Baixa**. Outro valor gera erro e o sistema pede de novo. |
| Data limite | Texto livre no formato DD/MM/AAAA. |
| Status | Definido automaticamente como **Pendente** no cadastro. |

Se nenhuma tarefa foi cadastrada, a opção de visualização informa que não existem registros.

## ▶️ Instalação e execução

Pré-requisito: [Python 3](https://www.python.org/downloads/) instalado (não há dependências externas).

```bash
# 1. Clonar o repositório
git clone https://github.com/jjoaquim0/TaskTracker---Bootcamp-2.git
cd TaskTracker---Bootcamp-2

# 2. Executar a aplicação
python3 src/main.py      # no Windows: python src\main.py
```

### Exemplo de uso

```
========================================
            TASKTRACKER
========================================
1 - Cadastrar nova tarefa
2 - Visualizar tarefas cadastradas
3 - Sair da aplicação
========================================
Escolha uma opção: 1

--- Cadastro de tarefa ---
Título:
Erro: o título é obrigatório e não pode ficar vazio. Tente novamente.
Título: Estudar Git
Descrição: Revisar commit e push
Prioridade (Alta/Média/Baixa): urgente
Erro: prioridade inválida. Digite apenas Alta, Média ou Baixa.
Prioridade (Alta/Média/Baixa): Alta
Data limite (DD/MM/AAAA): 20/10/2026

Tarefa cadastrada com sucesso!
```

## 🗺️ Fases do projeto

| Fase | Entrega | Status |
|------|---------|--------|
| 1 | Planejamento lógico (Google Docs + vídeo) | ✅ Concluída |
| 2 | Repositório Git/GitHub + implementação em Python | 🚧 Atual |
| 3 | Containerização com Docker, testes e deploy | ⏳ Futura |
