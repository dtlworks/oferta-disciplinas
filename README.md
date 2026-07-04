# Oferta de Disciplinas — Dashboard de Gestão de Professores

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Projeto de **Introdução à Ciência de Dados** — UFAL/CTEC.

Dashboard interativo para visualização e comparação da distribuição de professores por setor no **Centro de Tecnologia (CTEC)** da **Universidade Federal de Alagoas (UFAL)**.

> **Disciplina:** Introdução à Ciência de Dados  
> **Instituição:** UFAL — Campus A.C. Simões

---

## Motivação

O CTEC-UFAL não dispõe de uma ferramenta para visualizar a distribuição de carga horária docente entre setores e períodos letivos. Este projeto propõe um dashboard que consolida dados de ofertas e setores, permitindo à gestão:

- Visualizar gargalos na distribuição de carga horária
- Comparar setores lado a lado
- Planejar alocações com base em dados

---

## Tecnologias

- **Python** — processamento e análise de dados
- **Pandas** — manipulação dos dados tabulares
- **SQLite / SQLModel** — persistência e consultas
- **Dash** — aplicação web interativa
- **Plotly** — visualização de dados

---

## Estrutura do Projeto

```
oferta-disciplinas/
├── notebooks/               # Notebooks Jupyter (ETL + Dashboard)
│   ├── Tratamento_dos_dados.ipynb
│   └── Dashboard_oferta.ipynb
├── dados/
│   ├── entrada/             # Dados de entrada (.xlsx / .xlsm)
│   │   ├── setores_ctec.xlsm
│   │   └── oferta_AAAA.S.xlsx
│   ├── banco/               # Banco SQLite gerado pelo Notebook 1
│   │   └── ofertas.db
│   └── exemplos/            # Exemplos de uso (opcional)
├── docs/                    # Documentação do projeto
│   ├── mapeamento-funcoes.md
│   ├── mapeamento-layout.md
│   └── esboco-dashboard.md
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── requirements.txt
└── README.md
```

---

## Fluxo de Execução

```
Planilhas de oferta (.xlsx)
         |
         v
Notebook 1 — Tratamento dos dados (ETL)
         |
         v
    SQLite (ofertas.db)
         |
         v
Notebook 2 — Dashboard (Dash/Plotly)
         |
         v
   Dashboard interativo
```

---

## Como Executar

### 1. Pré-requisitos

- Python 3.10+
- Gerenciador de pacotes `pip`

### 2. Criar ambiente virtual (recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

> **Nota:** Os notebooks usam caminhos relativos à raiz do projeto (`dados/entrada/`, `dados/banco/`). Execute os notebooks com o diretório de trabalho na raiz do projeto — é o comportamento padrão ao abrir a pasta `oferta-disciplinas` no Jupyter ou VS Code.

### 4. Executar o Notebook 1 (ETL)

Abra e execute `notebooks/Tratamento_dos_dados.ipynb`:

- Jupyter Notebook: `jupyter notebook notebooks/Tratamento_dos_dados.ipynb`
- VS Code: abra o arquivo e execute célula por célula

Este notebook lê os arquivos de `dados/entrada/`, processa os dados e persiste o resultado em `dados/banco/ofertas.db`.

### 5. Executar o Notebook 2 (Dashboard)

Abra e execute `notebooks/Dashboard_oferta.ipynb`:

Ao executar a última célula, o servidor Dash será iniciado em `http://localhost:8050`.

---

## Estrutura dos Arquivos de Entrada

### Arquivo fixo

`setores_ctec.xlsm` — mapeamento de disciplinas para setores. Deve permanecer inalterado.

### Arquivos de oferta

Seguem obrigatoriamente o padrão:

```
oferta_AAAA.S.xlsx
```

Onde `AAAA` é o ano e `S` é o período (1 ou 2).

Exemplos:

```
oferta_2024.1.xlsx
oferta_2024.2.xlsx
oferta_2025.1.xlsx
```

---

## Resultado Esperado

> Screenshots do dashboard — *em breve*

---

## Documentação

Documentos complementares disponíveis em [`docs/`](docs/):

- [`mapeamento-funcoes.md`](docs/mapeamento-funcoes.md) — Especificação detalhada de todas as funções do sistema (ETL, análise, callbacks)
- [`mapeamento-layout.md`](docs/mapeamento-layout.md) — Estrutura completa do layout com IDs e componentes
- [`esboco-dashboard.md`](docs/esboco-dashboard.md) — Esboço visual e funcionalidades do dashboard

---

## Autor

Projeto desenvolvido como trabalho da disciplina de Introdução à Ciência de Dados — UFAL/CTEC.

---

## Licença

Este projeto está licenciado sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.
