import dash_html_components as html
import dash_core_components as dcc


def cria_cabecalho() -> html.Div:
    """
    Renderiza o cabeçalho estático do Dashboard com título, subtítulo e logo.
    """
    return html.Div(
        children=[
            html.H1(
                "Gestão de Professores",
                style={
                    "margin": "0",
                    "font-size": "28px",
                    "color": "#003366",
                },
            ),
            html.H2(
                "Centro de Tecnologia — UFAL",
                style={
                    "margin": "4px 0 0 0",
                    "font-size": "16px",
                    "color": "#666",
                    "font-weight": "normal",
                },
            ),
        ],
        style={
            "padding": "20px 30px",
            "background": "white",
            "border-bottom": "2px solid #003366",
            "display": "flex",
            "align-items": "center",
            "gap": "16px",
        },
    )


def cria_painel_lateral() -> html.Div:
    """
    Renderiza o painel lateral global com controles de filtragem.
    """
    return html.Div(
        children=[
            html.Label("Setores de Atuação", style={"font-weight": "bold"}),
            dcc.Dropdown(
                id="barra-pesquisa-1",
                placeholder="Digite o nome do setor...",
                style={"margin-bottom": "16px"},
            ),
            html.Label("Período", style={"font-weight": "bold"}),
            dcc.RangeSlider(
                id="range-slider",
                min=2010,
                max=2026,
                step=0.5,
                marks={
                    2010: "2010.1",
                    2020: "2020.1",
                    2026: "2026.1",
                },
                value=[2010, 2026],
                tooltip={"placement": "bottom", "always_visible": True},
                style={"margin-bottom": "16px"},
            ),
            html.Label("Modo de Comparação", style={"font-weight": "bold"}),
            dcc.RadioItems(
                id="radio-modo-comparar",
                options=[
                    {"label": " Desativado", "value": "desativado"},
                    {"label": " Ativado", "value": "ativado"},
                ],
                value="desativado",
                labelStyle={"display": "block", "margin": "4px 0"},
            ),
        ],
        style={
            "width": "280px",
            "padding": "20px",
            "background": "#f5f5f5",
            "border-right": "1px solid #ddd",
            "height": "100vh",
            "overflow-y": "auto",
        },
    )


def cria_container_grafico() -> html.Div:
    """
    Renderiza o espaço reservado para o gráfico de barras.
    """
    return html.Div(
        children=[
            dcc.Graph(id="grafico"),
        ],
        style={
            "flex": "1",
            "padding": "20px",
            "background": "white",
            "margin": "16px",
            "border-radius": "8px",
            "box-shadow": "0 1px 3px rgba(0,0,0,0.12)",
        },
    )


def cria_container_tabelas() -> html.Div:
    """
    Renderiza a área de exibição das tabelas de professores.
    """
    return html.Div(
        children=[
            html.Div(
                id="tabela-professores-1",
                style={
                    "flex": "1",
                    "padding": "20px",
                    "background": "white",
                    "margin": "0 8px 16px 8px",
                    "border-radius": "8px",
                    "box-shadow": "0 1px 3px rgba(0,0,0,0.12)",
                    "overflow-x": "auto",
                },
            ),
            html.Div(
                id="container-comparacao",
                children=[
                    html.H3(
                        "Comparação",
                        style={
                            "margin": "0 0 12px 0",
                            "color": "#003366",
                        },
                    ),
                    dcc.Dropdown(
                        id="barra-pesquisa-2",
                        placeholder="Selecione outro setor...",
                        style={"margin-bottom": "12px"},
                    ),
                    html.Div(
                        id="tabela-professores-2",
                        style={"overflow-x": "auto"},
                    ),
                ],
                style={
                    "flex": "1",
                    "padding": "20px",
                    "background": "white",
                    "margin": "0 8px 16px 8px",
                    "border-radius": "8px",
                    "box-shadow": "0 1px 3px rgba(0,0,0,0.12)",
                    "display": "none",
                },
            ),
        ],
        style={
            "display": "flex",
            "padding": "0 16px",
        },
    )


def cria_layout():
    """
    Monta o layout completo do dashboard.
    """
    return html.Div(
        children=[
            cria_cabecalho(),
            html.Div(
                children=[
                    cria_painel_lateral(),
                    html.Div(
                        children=[
                            cria_container_grafico(),
                            cria_container_tabelas(),
                        ],
                        style={
                            "flex": "1",
                            "display": "flex",
                            "flex-direction": "column",
                        },
                    ),
                ],
                style={"display": "flex"},
            ),
        ],
        style={"font-family": "Arial, sans-serif"},
    )
