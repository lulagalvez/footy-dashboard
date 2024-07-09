from dash import html, dcc
import dash_bootstrap_components as dbc


def create_layout(teams):
    team_buttons = [
        dbc.Button(html.Img(src=f'assets/teams/{team.lower().replace(" ", "")}.png', style={'height': '100%', 'width': 'auto'}),
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
                        html.P(
                            "La mejor plataforma para realizar tu análisis futbolero.")
                    ],
                    style={"vertical-alignment": "top", "height": 160}
                ),
                html.Div(
                    team_buttons,
                    style={'margin-left': 15, 'margin-right': 15,
                           'display': 'flex', 'flex-wrap': 'wrap'}
                ),
            ],
            style={'width': '20%', 'margin-left': 35,
                   'margin-right': 35, 'margin-top': 35, 'margin-bottom': 35}
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H1("Select a Team", id='team-name-display',
                                style={'color': 'white', 'margin-bottom': '15px'}),
                    ],
                    style={'width': '100%', 'margin-left': 35,
                           'margin-right': 35, 'margin-top': 35, 'margin-bottom': 35, 'text-align': 'center'}
                ),
                # Gráficos
                html.Div(
                    [
                        html.Div([dcc.Graph(id='graph-1')], className='graph-square',
                                 style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([dcc.Graph(id='graph-2')], className='graph-square',
                                 style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([dcc.Graph(id='graph-3')], className='graph-square',
                                 style={'width': '100%', 'display': 'inline-block'}),
                        html.Div([dcc.Graph(id='graph-4')], className='graph-square',
                                 style={'width': '50%', 'display': 'inline-block'}),
                    ],
                    style={'width': '100%'}
                )
            ],
            style={'overflowY': 'scroll', 'flex': '0 0 56%'}
        ),
        html.Div(
            [
                # Lista de jugadores en la sección de la derecha con barra de desplazamiento
                html.Div([
                    html.Div(id='player-1', className='player-info'),
                    html.Div(id='player-2', className='player-info'),
                    html.Div(id='player-3', className='player-info'),
                    html.Div(id='player-4', className='player-info')
                ],
                    style={'width': '100%', 'height': '100%'})
            ],
            style={'overflowY': 'scroll', 'overflowX': 'hidden', 'padding': '15px',
                   'flex': '0 0 20%', 'background-color': '#333', 'color': '#fff'}
        )
    ], fluid=True, style={'display': 'flex', 'flex-direction': 'row', }, className='dashboard-container')
