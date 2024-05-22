import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/player-distribution', name="Distribución de Jugadores")

####################### DATASET #############################
players_df = pd.read_csv("data/england-premier-league-players-2018-to-2019-stats.csv")

####################### DISTRIBUTION CHART #############################
def create_distribution_chart(column="role"):
    fig = px.histogram(players_df, x=column)
    fig.update_layout(
        title=f"Distribution of {column.capitalize()}",
        xaxis_title=column.capitalize(),
        yaxis_title="Count",
        height=600
    )
    return fig

####################### WIDGETS #############################
options = ["position", "Current Club", "nationality"]

column_dropdown = dcc.Dropdown(
    id="column_dropdown", 
    options=[{"label": col.capitalize(), "value": col} for col in options], 
    value="role", 
    clearable=False
)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.Label("Select Column"), column_dropdown,
    dcc.Graph(id="distribution_chart")
])

####################### CALLBACKS ###############################
@callback(Output("distribution_chart", "figure"), [Input("column_dropdown", "value")])
def update_distribution_chart(column):
    return create_distribution_chart(column)
