import plotly.express as px
import pandas as pd


def cria_grafico(df_final: pd.DataFrame, setores_selecionados: list = None) -> dict:
    """
    Gera o gráfico de barras com a carga horária média por setor.
    Retorna dict (formato figure) para o componente dcc.Graph.
    """
    df_agg = df_final.groupby("Setor", as_index=False)["CH Docente 1"].mean()
    df_agg = df_agg.rename(columns={"CH Docente 1": "Carga Horária Média"})

    if setores_selecionados and len(setores_selecionados) > 0:
        df_agg = df_agg[df_agg["Setor"].isin(setores_selecionados)]

    fig = px.bar(
        df_agg,
        x="Setor",
        y="Carga Horária Média",
        title="Carga Horária dos Setores",
        labels={"Carga Horária Média": "CH (h/semana)"},
        color="Carga Horária Média",
        color_continuous_scale="Blues",
    )

    fig.update_layout(
        xaxis_title="Setor",
        yaxis_title="Carga Horária Média (h/semana)",
        paper_bgcolor="white",
        plot_bgcolor="rgba(0,0,0,0.02)",
    )

    return fig
