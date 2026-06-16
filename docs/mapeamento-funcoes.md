# Mapeamento das Funções

## Tratamento dos Dados - Ficará em outro .ipynb

### `le_ofertas(path: str) -> pd.DataFrame`
Lê arquivos `.xlsx` (ofertas a cada período) e disponibiliza o `df_ofertas` estruturado com colunas:
- `Código`
- `Disciplina`
- `Turma`
- `Docente 1`
- `CH Docente 1`
- `Docente 2`
- `CH Docente 2`
- `Horário`
- `Local`
- `Matriculados`
- `Capacidade`
- `Oferta` (usar o ano de oferta como identificador do arquivo)

### `le_setores(path: str) -> pd.DataFrame`
Lê o arquivo `setores_ctec.xlsx` onde há a definição de setores para as disciplinas (arquivo este que poderá ser alterado conforme necessário e não mudará o funcionamento do dashboard), gerando o `df_setores` com colunas:
- `Código`
- `Disciplina`
- `Setor`

### `grava_dados(df_ofertas, df_setores, path: str) -> None`
Recebe os dfs gerados, convertendo-os para SQL e salvando-os em um banco de dados com a seguinte estrutura:

**Setor**
- `id_setor`: varchar / PK
- `nome_setor`: varchar

**Disciplinas**
- `codigo`: varchar / PK
- `nome_disciplina`: varchar
- `carga_horaria`: int
- `id_setor`: FK

**Professor**
- `id_professor`: varchar / PK
- `nome_professor`: char

**Oferta**
- `id_oferta`: varchar / PK
- `codigo`: FK
- `turma`: int
- `id_professor`: FK
- `ch_professor`: int
- `id_professor2`: FK (null)
- `ch_professor2`: int (null)
- `horario`: varchar
- `local`: char
- `matriculados`: int
- `capacidade`: int

---

## Dashboard (`Dashboard_ofertas.ipynb`)

### Funções Auxiliares

#### `carrega_dados(path: str) -> pd.DataFrame`
Lê o arquivo do banco de dados (`.db`) e reconstrói o `df_bruto` a partir das colunas estritamente necessárias para alimentar o Dashboard.

O cruzamento de informações entre tabelas é feito por colunas em comum, evitando armazenar colunas redundantes. As filtragens convenientes **NÃO** ocorrem aqui — são aplicadas pelos callbacks no momento da interação do usuário. Implementar os cruzamentos diretamente nos callbacks conforme forem surgindo.

#### `identifica_ofertas(df_bruto: pd.DataFrame) -> list`
Recebe o `df_bruto` e identifica os semestres ofertados para alimentar o Range Slider de seleção temporal, retornando a `lista_ofertas`.

#### `seleciona_dados(df_bruto: pd.DataFrame, semestres_selecionados: list) -> pd.DataFrame`
Filtra o `df_bruto` mantendo apenas as linhas cujo semestre esteja dentro do intervalo temporal estabelecido pelo Range Slider. `semestres_selecionados` é um parâmetro proveniente de um callback (interação do usuário com um `dcc`). Retorna `df_filtrado`.

#### `define_demandas(df_filtrado: pd.DataFrame) -> pd.DataFrame`
Classifica a carga horária semanal dos professores em faixas de demanda e calcula a carga horária média por setor respeitando a classificação definida:
- **Baixa:** <= 8h/semana
- **Alta:** > 12h/semana
- **Média:** else

Retorna `df_final`.

#### `gera_opcoes_dropdown_1(df_final: pd.DataFrame, texto_digitado_1: str) -> list`
Filtra os setores disponíveis com base no texto que o usuário está digitando em `barra-pesquisa-1`, retornando as sugestões para o dropdown (`lista_dropdown_1`) em tempo real.

#### `gera_opcoes_dropdown_2(df_final: pd.DataFrame, texto_digitado_2: str, setor_selecionado_1: str) -> list`
Filtra os setores pelo texto digitado em `barra-pesquisa-2`, excluindo o setor já selecionado em `barra-pesquisa-1`. Retorna `lista_dropdown_2`.

#### `cria_tabela_professores(df_final: pd.DataFrame, setor_selecionado: list) -> dash.html.Table`
Filtra os dados para o setor selecionado e apresenta a distribuição de professores para as disciplinas do setor. Retorna a tabela pronta para ser inserida no layout, servindo como base de comparação e uso do dashboard.

#### `cria_grafico(df_final: pd.DataFrame, setores_selecionados: list) -> dict`
Gera o gráfico de barras com a carga horária média por setor. Está vinculada ao callback `atualizar_tabela_1`, que é quem a chama e injeta a sua saída no Output `"grafico"`. Retorna dict (formato figure) para o componente `grafico`.

---

### Callbacks

#### `atualizar_grafico(pesquisa_setor_1: str, range_tempo: list) -> dict`
- **Inputs:** `barra-pesquisa-1` (value), `range-slider` (value)
- **Output:** `grafico` (figure)

Monitora a `barra-pesquisa-1` e o Range Slider; atualiza o gráfico de barras. Internamente chama:
1. `seleciona_dados()` — aplicar filtro temporal
2. `define_demandas()`
3. `cria_grafico()` — gerar figura

Retorna dict (figure) para o componente `grafico`.

#### `atualizar_tabela_1(pesquisa_setor_1: str, range_tempo: list) -> dash.html.Table`
- **Inputs:** `barra-pesquisa-1` (value), `range-slider` (value)
- **Output:** `tabela-professores-1` (children)

Monitora a `barra-pesquisa-1` e o Range Slider; atualiza a tabela 1. Internamente chama:
1. `seleciona_dados()` — aplicar filtro temporal
2. `define_demandas()`
3. `cria_tabela_professores()` — montar tabela 1

Retorna `dash.html.Table` para `tabela-professores-1`.

#### `atualizar_opcoes_dropdown_1(valor_digitado: str) -> list`
- **Input:** `barra-pesquisa-1` (search_value)
- **Output:** `barra-pesquisa-1` (options)

Monitora o texto digitado na `barra-pesquisa-1` e atualiza suas sugestões em tempo real. Internamente chama `gera_opcoes_dropdown_1()`. Retorna a lista de sugestões filtradas.

#### `exibir_segunda_tabela(botao_comparar: str) -> dict`
- **Input:** `radio-modo-comparar` (value)
- **Output:** `container-comparacao` (style)

Mostra ou esconde o container da segunda tabela (e da segunda barra de pesquisa) com base no radio button de modo de comparação. Retorna um dicionário com propriedade CSS (mostrar se ativo; senão, não mostrar).

#### `atualizar_opcoes_dropdown_2(valor_digitado: str, setor_selecionado_1: str) -> list`
- **Input:** `barra-pesquisa-2` (search_value)
- **State:** `barra-pesquisa-1` (value)
- **Output:** `barra-pesquisa-2` (options)

Monitora o texto digitado em `barra-pesquisa-2` e atualiza suas sugestões em tempo real, excluindo o setor já confirmado em `barra-pesquisa-1`. Usa `State` pois o setor 1 é apenas consultado, não deve disparar esse callback sozinho. Internamente chama `gera_opcoes_dropdown_2()`.

#### `atualizar_tabela_2(pesquisa_setor_2: str, range_tempo: list) -> dash.html.Table`
- **Inputs:** `barra-pesquisa-2` (value), `range-slider` (value)
- **Output:** `tabela-professores-2` (children)
- `prevent_initial_call = True`

Monitora a barra de pesquisa do setor 2 e o Range Slider; atualiza a tabela 2 de comparação quando o modo de comparação está ativo. Internamente chama:
1. `seleciona_dados()` — aplicar filtro temporal
2. `cria_tabela_professores()` — montar tabela 2

Retorna a tabela 2 atualizada.
