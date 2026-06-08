# Oferta de Disciplinas — Dashboard de Gestão de Professores

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Projeto de **Introdução à Ciência de Dados** — UFAL/CTEC.

Dashboard interativo para visualização e comparação da distribuição de professores por setor no **Centro de Tecnologia (CTEC)** da **Universidade Federal de Alagoas (UFAL)**.

> **Disciplina:** Introdução à Ciência de Dados  
> **Instituição:** UFAL — Campus A.C. Simões

---

## Visão Geral

O CTEC-UFAL não dispõe de uma ferramenta para visualizar a distribuição de carga horária docente entre setores e períodos letivos. Este projeto propõe um dashboard que consolida dados de ofertas e setores, permitindo à gestão:

- Visualizar gargalos na distribuição de carga horária
- Comparar setores lado a lado
- Planejar alocações com base em dados

### Dados de Entrada

| Arquivo | Descrição |
|---|---|
| `ofertas.xlsx` | Disciplinas, docentes e horários por período |
| `setores_ctec.xlsx` | Vínculo disciplina-setor |

### Saída

- Gráfico de carga horária por setor
- Tabela detalhada de professores por disciplina
- Classificação de demanda (baixa, média, alta)
- Modo comparativo entre dois setores

---

## Estrutura do Projeto

```
oferta-disciplinas/
├── Dados/                       # Dados de entrada (.xlsx / .xlsm)
│   ├── setores_ctec.xlsx
│   └── setores_ctec.xlsm
├── docs/                        # Documentação do projeto
│   ├── mapeamento-funcoes.md    # Especificação de funções
│   ├── mapeamento-layout.md     # Especificação do layout
│   └── esboco-dashboard.md      # Descrição visual do dashboard
├── notebooks/                   # Google Colab notebooks (prototipagem)
├── .gitignore                   # Arquivos ignorados pelo Git
├── LICENSE                      # Licença MIT
├── requirements.txt             # Dependências do projeto
└── README.md                    # Este arquivo
```

---

## Documentação

Documentos complementares disponíveis em [`docs/`](docs/):

- [`mapeamento-funcoes.md`](docs/mapeamento-funcoes.md) — Especificação detalhada de todas as funções do sistema (ETL, análise, callbacks)
- [`mapeamento-layout.md`](docs/mapeamento-layout.md) — Estrutura completa do layout com IDs e componentes
- [`esboco-dashboard.md`](docs/esboco-dashboard.md) — Esboço visual e funcionalidades do dashboard

---

## Licença

Este projeto está licenciado sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.
