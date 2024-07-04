from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import random
import pandas as pd
from graphs.teamprogress_linegraph import prepare_data_and_fig


px.defaults.template = "ggplot2"

external_css = [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

fig = prepare_data_and_fig()

teams = [
    "Arsenal", "Aston Villa", "Brentford", "Brighton", "Burnley",
    "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leeds United",
    "Leicester City", "Liverpool", "Manchester City", "Manchester United",
    "Newcastle United", "Norwich City", "Southampton", "Tottenham Hotspur",
    "Watford", "West Ham United", "Wolverhampton Wanderers"
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
                    html.P(
                        "La mejor plataforma para realizar tu análisis futbolero.")
                ],
                style={
                    "vertical-alignment": "top",
                    "height": 160
                }),
            html.Div(
                [
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/arsenal.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/bournemouth.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/brighton.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/burnley.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70})
                ],
                style={
                    'margin-left': 15,
                    'margin-right': 15,
                    'display': 'flex'
                }),
            html.Div(
                [
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/cardiff.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),

                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/chelsea.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/crystalpalace.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/everton.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70})
                ],
                style={
                    'margin-left': 15,
                    'margin-right': 15,
                    'display': 'flex'
                }),
            html.Div(
                [
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/fulham.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/huddersfield.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/leicester.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/liverpool.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70})
                ],
                style={
                    'margin-left': 15,
                    'margin-right': 15,
                    'display': 'flex'
                }),
            html.Div(
                [
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/manchestercity.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/manchesterunited.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/newcastle.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/southampton.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70})
                ],
                style={
                    'margin-left': 15,
                    'margin-right': 15,
                    'display': 'flex'
                }),
            html.Div(
                [
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/tottenham.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/watford.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/westham.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70}),
                    html.Div(
                        dbc.Button(
                            html.Img(
                                src='assets/teams/wolverhampton.png',
                                style={'height': '80%', 'width': 'auto'}),
                            className="btn btn-info",
                            style={'width': '70px', 'height': '70px', 'padding': '5px'}, n_clicks=0),
                        style={'width': 70})
                ],
                style={
                    'margin-left': 15,
                    'margin-right': 15,
                    'display': 'flex'
                }),

        ],
        style={
            'width': 400,
            'margin-left': 35,
            'margin-top': 35,
            'margin-bottom': 35
        }),
    html.Div(
        [
            html.Div(dcc.Graph(figure=fig), style={'width': 790}),
            html.Div([
                html.H2('Output 1:'),
                html.Div(className='Output'),
                html.H2('Output 2:'),
                html.Div(html.H3("Selected Value"), className='Output')
            ],
                style={'width': 200})
        ],
        style={
            'width': 990,
            'margin-top': 35,
            'margin-right': 35,
            'margin-bottom': 35,
            'display': 'flex'
        })
],
    fluid=True,
    style={'display': 'flex'},
    className='dashboard-container')

if __name__ == '__main__':
    app.run(debug=True)
