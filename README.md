# TaskTracker

Sistema simples de gerenciamento de tarefas via linha de comando (CLI), desenvolvido em Python 3
como projeto cumulativo do **Bootcamp II**.

## 📌 Descrição

O TaskTracker ajuda a organizar as tarefas do dia a dia. Pelo terminal, o usuário pode:

- **Cadastrar** uma tarefa com título, descrição, prioridade e data limite;
- **Visualizar** todas as tarefas cadastradas, com resumo de pendentes e concluídas;
- **Concluir** uma tarefa pelo número (identificador);
- **Sair** da aplicação.

O planejamento lógico completo (Fase 1) está em [`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf).

## 🗂️ Estrutura do repositório

```
tasktracker-projeto/
├── README.md                    # Documentação principal da aplicação e instruções de uso
├── .gitignore                   # Regras para ignorar arquivos temporários do Python e ambiente virtual
├── .dockerignore                # Arquivos que não entram na imagem Docker
├── Dockerfile                   # Receita da imagem Docker da aplicação (Fase 3)
├── docker-compose.yml           # Orquestração da execução interativa no terminal (Fase 3)
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico e arquitetural entregue na Fase 1
├── src/
│   └── main.py                  # Código-fonte principal da aplicação TaskTracker
└── tests/
    └── test_tasktracker.py      # Testes automatizados das regras de negócio
```

## 🛠️ Tecnologias

- Python 3
- Git e GitHub
- Docker e Docker Compose

## ✅ Regras de negócio

| Campo | Regra |
|-------|-------|
| Título | Obrigatório. Entradas vazias ou só com espaços são rejeitadas e o sistema pede de novo. |
| Descrição | Livre (pode ficar em branco). |
| Prioridade | Aceita apenas **Alta**, **Média** (ou **Media**) e **Baixa**. Outro valor gera erro e o sistema pede de novo. |
| Data limite | Obrigatória, no formato DD/MM/AAAA e precisa ser uma data que existe (ex.: 31/02 é rejeitado). |
| Identificador | Número gerado automaticamente (1, 2, 3...). |
| Status | Definido automaticamente como **Pendente** no cadastro; vira **Concluída** pela opção 3. |

Se nenhuma tarefa foi cadastrada, a visualização informa que não existem registros.
Opções de menu inválidas não encerram o programa: o sistema avisa e mostra o menu de novo.

## 🐳 Executando com Docker (recomendado)

Pré-requisito: [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e aberto.
Não é preciso instalar o Python: tudo roda dentro do container.

```bash
git clone https://github.com/jjoaquim0/TaskTracker---Bootcamp-2.git
cd TaskTracker---Bootcamp-2
```

**1. Como construir a imagem:**

```bash
docker build -t tasktracker .
```

**2. Como rodar o container em modo isolado:**

```bash
docker run -it --rm tasktracker
```

**3. Como rodar via orquestração (recomendado):**

```bash
docker compose run --rm tasktracker
```

> O `docker compose run` constrói a imagem automaticamente na primeira vez.
> Para forçar uma nova construção depois de alterar o código: `docker compose build`.

### Por que `-it`, `stdin_open` e `tty`?

O TaskTracker é uma aplicação de terminal que usa `input()` para ler as opções do menu.
Por padrão, um container não recebe o que você digita. Por isso:

| Configuração | Onde | Para que serve |
|--------------|------|----------------|
| `-i` / `stdin_open: true` | `docker run` / `docker-compose.yml` | Mantém aberta a entrada de dados (o teclado) |
| `-t` / `tty: true` | `docker run` / `docker-compose.yml` | Aloca um terminal virtual, simulando o console |
| `--rm` | `docker run` / `docker compose run` | Remove o container ao sair, sem deixar lixo |

### O Dockerfile, linha a linha

| Instrução | O que faz |
|-----------|-----------|
| `FROM python:3.11-slim` | Usa uma imagem base leve com Python 3.11 |
| `WORKDIR /app` | Define a pasta de trabalho dentro do container |
| `ENV PYTHONUNBUFFERED=1` | Mostra as mensagens no terminal imediatamente, sem buffer |
| `COPY src/ /app/src/` | Copia o código da aplicação para dentro da imagem |
| `CMD ["python", "src/main.py"]` | Comando que inicia o TaskTracker quando o container sobe |

## ▶️ Execução sem Docker

Pré-requisito: [Python 3](https://www.python.org/downloads/) instalado (não há dependências externas).

```bash
# 1. Clonar o repositório
git clone https://github.com/jjoaquim0/TaskTracker---Bootcamp-2.git
cd TaskTracker---Bootcamp-2

# 2. Executar a aplicação
python3 src/main.py      # no Windows: python src\main.py

# 3. (Opcional) Rodar os testes
python3 -m unittest discover tests
```

### Exemplo de uso

```
========================================
            TASKTRACKER
========================================
1 - Cadastrar nova tarefa
2 - Visualizar tarefas cadastradas
3 - Concluir tarefa
4 - Sair da aplicação
========================================
Escolha uma opção: 1

--- Cadastro de tarefa ---
Título:
Erro: o título é obrigatório e não pode ficar vazio. Tente novamente.
Título: Estudar Git
Descrição (opcional): Revisar commit e push
Prioridade (Alta/Média/Baixa): urgente
Erro: prioridade inválida. Digite apenas Alta, Média ou Baixa.
Prioridade (Alta/Média/Baixa): Alta
Data limite (DD/MM/AAAA): 31/02/2026
Erro: data inválida. Use o formato DD/MM/AAAA (ex.: 20/10/2026).
Data limite (DD/MM/AAAA): 20/10/2026

Tarefa cadastrada com sucesso!
```

## 🗺️ Fases do projeto

| Fase | Entrega | Status |
|------|---------|--------|
| 1 | Planejamento lógico (Google Docs + vídeo) | ✅ Concluída |
| 2 | Repositório Git/GitHub + implementação em Python | ✅ Concluída |
| 3 | Containerização com Docker e Docker Compose | ✅ Concluída |
