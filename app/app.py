import os
import dash
from app.dados import carrega_dados
from app.layout import cria_layout
from app.callbacks import registrar_callbacks

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Dados", "dados.db")

app = dash.Dash(__name__)
app.title = "Gestão de Professores — CTEC/UFAL"

df_bruto = carrega_dados(DB_PATH)
app.layout = cria_layout()
registrar_callbacks(app, df_bruto)

if __name__ == "__main__":
    app.run_server(debug=True)
