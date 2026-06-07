# Oferta de Disciplinas — Dashboard de Gestão de Professores

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Dash](https://img.shields.io/badge/Dash-2.0%2B-00897B)](https://dash.plotly.com)

Dashboard interativo para visualização e comparação da distribuição de professores por setor no **Centro de Tecnologia (CTEC)** da **Universidade Federal de Alagoas (UFAL)**, desenvolvido com Dash e Python.

> **Disciplina:** Introdução à Ciência de Dados  
> **Instituição:** UFAL — Campus A.C. Simões  
> **Tecnologias:** Python, Dash, Plotly, Pandas, SQLAlchemy

---

## Sumário

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Como Executar](#como-executar)
- [Como Usar](#como-usar)
- [Tecnologias](#tecnologias)
- [Documentação](#documentação)
- [Licença](#licença)

---

## Visão Geral

O CTEC-UFAL não dispõe de uma ferramenta para visualizar a distribuição de carga horária docente entre setores e períodos letivos. Este dashboard consolida dados de ofertas de disciplinas e setores, permitindo à gestão:

- **Visualizar gargalos** na distribuição de carga horária
- **Comparar setores** lado a lado
- **Planejar alocações** com base em dados

### Dados de Entrada

O sistema consolida dados de duas planilhas:
1. **ofertas.xlsx** — disciplinas, docentes, horários por período
2. **setores_ctec.xlsx** — vínculo disciplina-setor

### Saída

- Gráfico de carga horária por setor
- Tabela detalhada de professores por disciplina
- Classificação de demanda (baixa, média, alta)
- Modo comparativo entre dois setores

---

## Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| **Filtro Temporal** | RangeSlider para selecionar intervalo de semestres |
| **Busca de Setores** | Barra de pesquisa com sugestões em tempo real |
| **Gráfico de Barras** | Carga horária média por setor com Plotly |
| **Tabela de Professores** | Distribuição detalhada de professores por disciplina |
| **Classificação de Demanda** | Baixa (<=8h), Média, Alta (>12h) |
| **Modo de Comparação** | Comparação lado a lado entre dois setores |

---

## Estrutura do Projeto

```
oferta-disciplinas/
├── app/                        # Aplicação Dash
│   ├── app.py                  # Inicialização e execução do app
│   ├── dados.py                # Leitura, tratamento e carga dos dados
│   ├── auxiliares.py           # Funções auxiliares de análise
│   ├── layout.py               # Componentes de layout do dashboard
│   ├── graficos.py             # Geração de gráficos (Plotly)
│   ├── tabelas.py              # Geração de tabelas HTML
│   └── callbacks.py            # Callbacks de interatividade
├── notebooks/                  # Jupyter notebooks para prototipagem
│   ├── Tratamento_dos_dados.ipynb
│   └── Dashboard_ofertas.ipynb
├── Dados/                      # Dados de entrada (.xlsx)
│   ├── setores_ctec.xlsx
│   └── setores_ctec.xlsm
├── docs/                       # Documentação do projeto
│   ├── mapeamento-funcoes.md   # Especificação de funções
│   ├── mapeamento-layout.md    # Especificação do layout
│   └── esboco-dashboard.md     # Descrição visual do dashboard
├── .gitignore                  # Arquivos ignorados pelo Git
├── LICENSE                     # Licença MIT
├── requirements.txt            # Dependências do projeto
└── README.md                   # Este arquivo
```

---

## Pré-requisitos

- **Python 3.10+** instalado
- **pip** (gerenciador de pacotes Python)

## Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/oferta-disciplinas.git
cd oferta-disciplinas
```

2. **Crie e ative um ambiente virtual (recomendado):**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute o dashboard:**

```bash
python app/app.py
```

5. **Acesse no navegador:** [http://localhost:8050](http://localhost:8050)

---

## Como Usar

### 1. Selecionar Período
Use o RangeSlider no painel lateral para definir o intervalo de semestres desejado.

### 2. Buscar Setor
Digite o nome de um setor na barra de pesquisa. Sugestões aparecerão em tempo real.

### 3. Visualizar Dados
- O **gráfico de barras** mostra a carga horária média dos setores
- A **tabela principal** exibe a distribuição de professores do setor selecionado

### 4. Comparar Setores
Ative o **Modo de Comparação** via radio button. Uma segunda barra de pesquisa aparecerá para selecionar outro setor. As duas tabelas serão exibidas lado a lado.

---

## Tecnologias

| Tecnologia | Versão | Função |
|---|---|---|
| [Python](https://python.org) | 3.10+ | Linguagem principal |
| [Dash](https://dash.plotly.com) | 2.0+ | Framework web para dashboard |
| [Plotly](https://plotly.com/python) | 5.0+ | Gráficos interativos |
| [Pandas](https://pandas.pydata.org) | 1.5+ | Manipulação de dados |
| [SQLAlchemy](https://sqlalchemy.org) | 2.0+ | ORM e persistência SQLite |
| [openpyxl](https://openpyxl.readthedocs.io) | 3.0+ | Leitura de arquivos .xlsx |

---

## Documentação

Documentos complementares disponíveis em [`docs/`](docs/):

- [`mapeamento-funcoes.md`](docs/mapeamento-funcoes.md) — Especificação detalhada de todas as funções do sistema (ETL, análise, callbacks)
- [`mapeamento-layout.md`](docs/mapeamento-layout.md) — Estrutura completa do layout com IDs e componentes
- [`esboco-dashboard.md`](docs/esboco-dashboard.md) — Esboço visual e funcionalidades do dashboard

---

## Licença

Este projeto está licenciado sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.
