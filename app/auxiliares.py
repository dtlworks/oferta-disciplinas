import pandas as pd


def identifica_ofertas(df_bruto: pd.DataFrame) -> list:
    """
    Recebe o df_bruto e identifica os semestres ofertados para alimentar
    o Range Slider de seleção temporal, retornando a lista_ofertas.
    """
    ofertas = sorted(df_bruto["Oferta"].unique())
    return ofertas


def seleciona_dados(
    df_bruto: pd.DataFrame, semestres_selecionados: list
) -> pd.DataFrame:
    """
    Filtra o df_bruto mantendo apenas as linhas cujo semestre esteja
    dentro do intervalo temporal estabelecido pelo Range Slider.
    """
    df_filtrado = df_bruto[
        df_bruto["Oferta"].between(semestres_selecionados[0], semestres_selecionados[1])
    ]
    return df_filtrado


def define_demandas(df_filtrado: pd.DataFrame) -> pd.DataFrame:
    """
    Classifica a carga horária semanal dos professores em faixas de demanda
    e calcula a carga horária média por setor:
      - baixa: <= 8h/semana
      - alta: > 12h/semana
      - média: else
    """
    df = df_filtrado.copy()

    def classificar(ch):
        if ch <= 8:
            return "Baixa"
        elif ch > 12:
            return "Alta"
        return "Média"

    df["Demanda"] = df["CH Docente 1"].apply(classificar)
    return df


def gera_opcoes_dropdown_1(
    df_final: pd.DataFrame, texto_digitado_1: str
) -> list:
    """
    Filtra os setores disponíveis com base no texto digitado em
    barra-pesquisa-1, retornando sugestões para o dropdown.
    """
    setores = df_final["Setor"].dropna().unique()
    if not texto_digitado_1:
        return [{"label": s, "value": s} for s in sorted(setores)]
    texto = texto_digitado_1.lower()
    filtrados = [s for s in setores if texto in s.lower()]
    return [{"label": s, "value": s} for s in sorted(filtrados)]


def gera_opcoes_dropdown_2(
    df_final: pd.DataFrame, texto_digitado_2: str, setor_selecionado_1: str
) -> list:
    """
    Filtra os setores disponíveis com base no texto digitado em
    barra-pesquisa-2, excluindo o setor já selecionado na primeira barra.
    """
    setores = df_final["Setor"].dropna().unique()
    setores = [s for s in setores if s != setor_selecionado_1]
    if not texto_digitado_2:
        return [{"label": s, "value": s} for s in sorted(setores)]
    texto = texto_digitado_2.lower()
    filtrados = [s for s in setores if texto in s.lower()]
    return [{"label": s, "value": s} for s in sorted(filtrados)]
