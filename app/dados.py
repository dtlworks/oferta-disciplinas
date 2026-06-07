import pandas as pd
from sqlalchemy import create_engine


def le_ofertas(path: str) -> pd.DataFrame:
    """
    Le arquivos .xlsx (ofertas a cada período) e disponibiliza o df_ofertas
    estruturado com colunas: Código, Disciplina, Turma, Docente 1,
    CH Docente 1, Docente 2, CH Docente 2, Horário, Local, Matriculados,
    Capacidade, Oferta (usar o ano de oferta como identificador do arquivo).
    """
    df = pd.read_excel(path)
    return df


def le_setores(path: str) -> pd.DataFrame:
    """
    Le o arquivo setores_ctec.xlsx onde há a definição de setores para as
    disciplinas, gerando o df_setores com colunas: Código, Disciplina, Setor.
    """
    df = pd.read_excel(path)
    return df


def grava_dados(df_ofertas: pd.DataFrame, df_setores: pd.DataFrame, path: str) -> None:
    """
    Recebe os DataFrames gerados, convertendo-os para SQL e salvando-os
    em um banco de dados SQLite.
    """
    engine = create_engine(f"sqlite:///{path}")
    df_ofertas.to_sql("ofertas", engine, if_exists="replace", index=False)
    df_setores.to_sql("setores", engine, if_exists="replace", index=False)
    engine.dispose()


def carrega_dados(path: str) -> pd.DataFrame:
    """
    Le o arquivo do banco de dados (.db) e reconstrói tudo em um único
    df_bruto — já realizando as filtragens convenientes — que será utilizado
    para a alimentação do Dashboard.
    """
    engine = create_engine(f"sqlite:///{path}")
    df_ofertas = pd.read_sql("SELECT * FROM ofertas", engine)
    df_setores = pd.read_sql("SELECT * FROM setores", engine)
    engine.dispose()
    df_bruto = df_ofertas.merge(df_setores, on=["Código", "Disciplina"], how="left")
    return df_bruto
