from dash import html, dcc
import dash_bootstrap_components as dbc


def create_layout(teams):
    # Generamos botones para cada equipo utilizando imágenes de los equipos
    # Cada botón se identifica por un ID único que refleja el equipo correspondiente
    team_buttons = [
        dbc.Button(html.Img(src=f'assets/teams/{team.lower().replace(" ", "")}.png', style={'height': '100%', 'width': 'auto'}),
                   id={'type': 'team-button', 'index': team}, className="btn btn-info", style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0)
        for team in teams
    ]
     # Estructuración del contenedor principal que incluye tres secciones principales
    return dbc.Container([
        # Sección superior: Bienvenida y selección de equipos
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
        # Sección superior: Bienvenida y selección de equipos
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
                # Gráficos de datos de equipos y jugadores
                html.Div(
                    [
                        html.Div([dcc.Graph(id='graph-1')], className='graph-square',
                                 style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([dcc.Graph(id='graph-2')], className='graph-square',
                                 style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([dcc.Graph(id='graph-3')], className='graph-square',
                                 style={'width': '100%', 'display': 'inline-block'}),
                        html.Div([dcc.Graph(id='graph-4')], className='graph-square',
                                 style={'width': '100%', 'display': 'inline-block'}),
                    ],
                    style={'width': '100%'}
                )
            ],
            style={'overflowY': 'scroll', 'flex': '0 0 56%'}
        ),
        # Sección derecha: Listado de jugadores
        html.Div(
            [
                
                html.Div(id='players-list', style={
                    'overflowY': 'scroll',
                    'height': '100%',
                    'padding': '15px',
                    'background-color': '#333',
                    'color': '#fff'
                })
            ],
            style={'padding': '15px','flex': '0 0 20%', 'background-color': '#333', 'color': '#fff'}
        )
    ], fluid=True, style={'display': 'flex', 'flex-direction': 'row', }, className='dashboard-container')
