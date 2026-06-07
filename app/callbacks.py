from dash import Output, Input, State, callback
from app.auxiliares import (
    seleciona_dados,
    define_demandas,
    gera_opcoes_dropdown_1,
    gera_opcoes_dropdown_2,
)
from app.graficos import cria_grafico
from app.tabelas import cria_tabela_professores


def registrar_callbacks(app, df_bruto):
    @app.callback(
        Output("grafico", "figure"),
        Output("tabela-professores-1", "children"),
        Input("barra-pesquisa-1", "value"),
        Input("range-slider", "value"),
    )
    def atualizar_tabela_1(pesquisa_setor_1, range_tempo):
        if not pesquisa_setor_1:
            return cria_grafico(df_bruto), "Selecione um setor para visualizar os dados."

        df_filtrado = seleciona_dados(df_bruto, range_tempo)
        df_final = define_demandas(df_filtrado)

        figura = cria_grafico(df_final, [pesquisa_setor_1])
        tabela = cria_tabela_professores(df_final, [pesquisa_setor_1])
        return figura, tabela

    @app.callback(
        Output("barra-pesquisa-1", "options"),
        Input("barra-pesquisa-1", "search_value"),
    )
    def atualizar_opcoes_dropdown_1(valor_digitado):
        return gera_opcoes_dropdown_1(df_bruto, valor_digitado or "")

    @app.callback(
        Output("container-comparacao", "style"),
        Input("radio-modo-comparar", "value"),
    )
    def exibir_segunda_tabela(botao_comparar):
        if botao_comparar == "ativado":
            return {
                "flex": "1",
                "padding": "20px",
                "background": "white",
                "margin": "0 8px 16px 8px",
                "border-radius": "8px",
                "box-shadow": "0 1px 3px rgba(0,0,0,0.12)",
            }
        return {"display": "none"}

    @app.callback(
        Output("barra-pesquisa-2", "options"),
        Input("barra-pesquisa-2", "search_value"),
        State("barra-pesquisa-1", "value"),
    )
    def atualizar_opcoes_dropdown_2(valor_digitado, setor_selecionado_1):
        return gera_opcoes_dropdown_2(
            df_bruto, valor_digitado or "", setor_selecionado_1
        )

    @app.callback(
        Output("tabela-professores-2", "children"),
        Input("barra-pesquisa-2", "value"),
        Input("range-slider", "value"),
        prevent_initial_call=True,
    )
    def atualizar_tabela_2(pesquisa_setor_2, range_tempo):
        if not pesquisa_setor_2:
            return "Selecione um setor para comparar."

        df_filtrado = seleciona_dados(df_bruto, range_tempo)
        df_final = define_demandas(df_filtrado)
        tabela = cria_tabela_professores(df_final, [pesquisa_setor_2])
        return tabela
