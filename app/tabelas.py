import pandas as pd
import dash_html_components as html


def cria_tabela_professores(
    df_final: pd.DataFrame, setor_selecionado: list
) -> html.Table:
    """
    Filtra os dados para o setor selecionado e apresenta a distribuição
    de professores para as disciplinas do setor.
    """
    if not setor_selecionado:
        return html.Div("Selecione um setor para visualizar os dados.")

    df_setor = df_final[df_final["Setor"].isin(setor_selecionado)]

    if df_setor.empty:
        return html.Div("Nenhum dado encontrado para o setor selecionado.")

    colunas_exibir = [
        "Docente 1",
        "Setor",
        "Disciplina",
        "CH Docente 1",
        "Demanda",
    ]
    colunas_disponiveis = [c for c in colunas_exibir if c in df_setor.columns]

    cabecalho = html.Thead(
        html.Tr(
            [
                html.Th(
                    col,
                    style={
                        "padding": "8px 12px",
                        "background": "#003366",
                        "color": "white",
                        "text-align": "left",
                    },
                )
                for col in colunas_disponiveis
            ]
        )
    )

    linhas = []
    for _, row in df_setor.iterrows():
        cor_demanda = {
            "Alta": "#ff4d4d",
            "Média": "#ffa64d",
            "Baixa": "#4dab4d",
        }
        demanda = row.get("Demanda", "")
        cor = cor_demanda.get(demanda, "inherit")

        linhas.append(
            html.Tr(
                [
                    html.Td(
                        row.get(col, ""),
                        style={
                            "padding": "6px 12px",
                            "border-bottom": "1px solid #ddd",
                        },
                    )
                    for col in colunas_disponiveis
                ]
                + [
                    html.Td(
                        demanda,
                        style={
                            "padding": "6px 12px",
                            "border-bottom": "1px solid #ddd",
                            "color": cor,
                            "font-weight": "bold",
                        },
                    )
                ],
                style={
                    "background": "#f9f9f9" if linhas.index([]) % 2 == 0 else "white"
                },
            )
        )
        _ = linhas.pop()

    corpo = html.Tbody(linhas)

    return html.Table(
        [cabecalho, corpo],
        style={
            "width": "100%",
            "border-collapse": "collapse",
            "font-family": "Arial, sans-serif",
            "font-size": "14px",
        },
    )
