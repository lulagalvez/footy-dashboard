from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout(app, teams, fig):
    team_buttons = [
        dbc.Button(html.Img(src=f'assets/teams/{team.lower().replace(" ", "")}.png', style={'height': '80%', 'width': 'auto'}), 
                   id={'type': 'team-button', 'index': team}, className="btn btn-info", style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0)
        for team in teams
    ]

    return dbc.Container([
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
