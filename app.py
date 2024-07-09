from dash import Dash, html, dcc, Input, Output, callback_context, ALL
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from graphs.teamprogress_linegraph import prepare_data_and_fig

px.defaults.template = "ggplot2"

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# Prepare initial figure
fig = prepare_data_and_fig()

teams = [
    "Arsenal", "Bournemouth", "Brighton", "Burnley",
    "Cardiff", "Chelsea", "Crystal Palace", "Everton",
    "Fulham", "Huddersfield", "Leicester", "Liverpool",
    "Manchester City", "Manchester United", "Newcastle",
    "Southampton", "Tottenham", "Watford", "West Ham",
    "Wolverhampton"
]

team_buttons = [
    dbc.Button(
        html.Img(src=f'assets/teams/{team.lower().replace(" ", "")}.png', style={'height': '80%', 'width': 'auto'}),
        id={'type': 'team-button', 'index': team}, className="btn btn-info", 
        style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0
    )
    for team in teams
]

app.layout = dbc.Container([
    html.Div(
        [
            html.Div(
                [
                    html.H1([
                        html.Span("¡Bienvenido a"),
                        html.Br(),
                        html.Span("FootyDashboard!")
                    ]),
                    html.P("La mejor plataforma para realizar tu análisis futbolero.")
                ],
                style={"vertical-alignment": "top", "height": 160}
            ),
            html.Div(
                team_buttons,
                style={'margin-left': 15, 'margin-right': 15, 'display': 'flex', 'flex-wrap': 'wrap'}
            ),
        ],
        style={'width': 400, 'margin-left': 35, 'margin-top': 35, 'margin-bottom': 35}
    ),
    html.Div(
        [
            html.Div(dcc.Graph(id='main-graph', figure=fig), style={'width': 790}),
            html.Div([
                html.H2('Output 1:'),
                html.Div(id='output-1', className='Output'),
                html.H2('Output 2:'),
                html.Div(id='output-2', className='Output')
            ], style={'width': 200})
        ],
        style={'width': 990, 'margin-top': 35, 'margin-right': 35, 'margin-bottom': 35, 'display': 'flex'}
    )
], fluid=True, style={'display': 'flex'}, className='dashboard-container')

@app.callback(
    Output('output-1', 'children'),
    Output('output-2', 'children'),
    Output('main-graph', 'figure'),
    Input({'type': 'team-button', 'index': ALL}, 'n_clicks')
)
def update_dashboard(n_clicks):
    ctx = callback_context
    if not ctx.triggered:
        return "Output 1: No team selected", "Output 2: No team selected", fig
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        team = eval(button_id)['index']
        return f"Output 1: {team}", f"Output 2: Selected Value: {team}", prepare_data_and_fig(team)

if __name__ == '__main__':
    app.run_server(debug=True)
