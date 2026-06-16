# Mapeamento do Layout

## Estrutura do Layout Geral

```python
app.layout = html.Div(
    id = 'container-geral',
    children = [

        # Coluna Esquerda
        html.Div(
            id = 'painel-lateral',
            children = [
                cria_cabecalho(),      # id = 'cabecalho' — H1, H2, logo
                cria_painel_lateral(), # dropdown, slider, radio
            ]
        ),

        # Coluna Direita
        html.Div(
            id = 'conteudo-principal',
            children = [

                # Superior
                html.Div(
                    id = 'div-superior',
                    children = [
                        html.Div(id = 'titulo-data'),         # título + data (callback)
                        html.Div(
                            id = 'grafico',
                            children = [cria_container_grafico()]  # dcc.Graph
                        ),
                    ]
                ),

                # Inferior
                html.Div(
                    id = 'div-inferior',
                    children = [
                        html.Div(
                            id = 'bloco-tabela',
                            children = [
                                html.Div(id = 'tabela-professores-1'),  # tabela fixa
                            ]
                        ),
                        html.Div(
                            id = 'bloco-comparacao',
                            style = {'display': 'none'},       # oculto por padrão
                            children = [
                                html.Div(id = 'tabela-professores-2'),  # depende do modo comparar
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ]
)
```

---

## Funções de Layout

### `cria_cabecalho() -> html.Div`
Renderiza cabeçalho estático do Dashboard.

**Componentes internos:**
- `html.H1` — título principal
- `html.H2` — subtítulo
- `html.Img` — logo (CTEC)

Retorna `html.Div`, container estático com título, subtítulo e logo.

---

### `cria_painel_lateral() -> html.Div`
Renderiza o painel lateral global, sempre visível do lado esquerdo do Dashboard independentemente do modo de comparação.

**Componentes internos e IDs:**

| Componente | ID | Descrição |
|---|---|---|
| `dcc.Dropdown` / `dcc.Input` | `barra-pesquisa-1` | Busca de setores |
| `dcc.Dropdown` / `dcc.Input` | `barra-pesquisa-2` | Oculta por padrão (`display: none`), ativada pelo callback de `radio-modo-comparar` |
| `dcc.RangeSlider` | `range-slider` | Seleção dos períodos (ex: 2026.1, 2026.2) |
| `dcc.RadioItems` | `radio-modo-comparar` | Ativar/desativar modo de comparação |

Retorna `html.Div`, container com os controles de filtragem global.

---

### `cria_container_grafico() -> html.Div`
Renderiza o espaço reservado para o gráfico de barras.

**Componentes internos e IDs:**

| Componente | ID | Descrição |
|---|---|---|
| `dcc.Graph` | `grafico` | Recebe a figura gerada por `cria_grafico()` via Output do callback `atualizar_grafico` |

Retorna `html.Div`, container centralizado com o componente `dcc.Graph`.

---

### `cria_container_tabelas() -> html.Div`
Renderiza a área de exibição das tabelas de professores, composta por dois blocos: a tabela principal (sempre visível) e o container de comparação (visibilidade controlada por callback).

**Componentes internos e IDs:**

| Componente | ID | Descrição |
|---|---|---|
| `html.Div` | `tabela-professores-1` | Tabela principal, sempre visível. Alimentada pelo callback `atualizar_tabela_1` via `cria_tabela_professores()` |
| `html.Div` | `container-comparacao` | Container dinâmico controlado pelo callback `exibir_segunda_tabela()`. Agrupa os componentes que aparecem/desaparecem no modo de comparação |
| `dcc.Dropdown` | `barra-pesquisa-2` | Barra de busca do segundo setor. Opções atualizadas pelo callback `atualizar_opcoes_dropdown_2` |
| `html.Div` | `tabela-professores-2` | Tabela de comparação. Alimentada pelo callback `atualizar_tabela_2` via `cria_tabela_professores()` |

Retorna `html.Div`, container com `tabela-professores-1` e `container-comparacao`.
