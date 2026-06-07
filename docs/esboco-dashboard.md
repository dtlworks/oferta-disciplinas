# Esboço do Dashboard

> Conteúdo extraído da apresentação `Esboço dashboard.pptx`

## Visão Geral

O dashboard apresenta uma interface dividida em:

### Painel Lateral (Esquerdo)
- **Seletor de Período:** RangeSlider permitindo selecionar intervalo entre semestres (ex: 2010.1 a 2024.1)
- **Setores de Atuação:** Barra de busca com sugestões em tempo real
- **Modo Comparar:** Radio button para ativar/desativar comparação entre dois setores

### Área Principal
- **Gráfico de Barras:** "Carga Horária dos Setores" — exibe a carga horária média por setor
- **Tabela de Distribuição de Professores:** Lista detalhada com colunas:
  - Professor
  - Setor
  - Disciplina
  - Projetos (PPG, TCC, PROJETO, etc.)
  - CH / Semana
  - Demanda (Alta / Média / Baixa)

### Funcionalidades do Esboço

**Tela 1 — Setor único:**
- Seleciona um setor (ex: Recursos Hídricos)
- Exibe tabela com professores, disciplinas, carga horária e classificação de demanda
- Gráfico de barras mostra carga horária dos setores

**Tela 2 — Modo Comparação:**
- Ativa o modo de comparação via radio button
- Duas tabelas lado a lado (ex: Estruturas vs Recursos Hídricos)
- Cada tabela mostra a distribuição de professores do respectivo setor
- Gráfico de barras atualizado considerando ambos os setores

### Classificação de Demanda
| Faixa | Classificação |
|---|---|
| <= 8h/semana | Baixa |
| > 12h/semana | Alta |
| Demais casos | Média |

### Exemplo de Dados (Mockup)
- **Estruturas:** Eduardo Nobre (22h, Média), Paulo César (16h, Média), Luciana Vieira (16h, Alta)
- **Recursos Hídricos:** Carlos Ruberto (22h, Alta), Christopher (16h, Média), Professor 3 (10h, Média)
