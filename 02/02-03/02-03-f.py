import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

data = pd.read_csv("offres-emploi-2021-2022.csv", usecols=["date_publication","total"])

# Créer une figure Plotly pour l'utiliser dans dcc.Graph()
fig = px.line(data, x= "date_publication", y = "total",title="Nombre des offres d'emploi entre 2021 et 2022"
              )


app = dash.Dash(__name__)

app.title = "Nombre des offres d'emploi entre 2021 et 2022"

app.layout = html.Div(
    id = "app_container",
    children=[
        html.H1("Nombre des offres d'emploi entre 2021 et 2022"),
        html.P("Résultats après traitement"),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)