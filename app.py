from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from layout import create_layout
from callbacks import register_callbacks
import pandas as pd

# Configuración de Plotly
px.defaults.template = "ggplot2"

# Crear la aplicación Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# Equipos de la Premier League
teams = [
    "Arsenal", "AFC Bournemouth", "Brighton & Hove Albion", "Burnley",
    "Cardiff City", "Chelsea", "Crystal Palace", "Everton",
    "Fulham", "Huddersfield Town", "Leicester City", "Liverpool",
    "Manchester City", "Manchester United", "Newcastle United",
    "Southampton", "Tottenham Hotspur", "Watford", "West Ham United",
    "Wolverhampton Wanderers"
]

player_df = pd.read_csv(
    './data/england-premier-league-players-2018-to-2019-stats.csv')

# Registrar los callbacks
register_callbacks(app, player_df)

# Asignar el layout
app.layout = html.Div([
    # Imagen de fondo
    html.Div(style={
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'width': '100%',
        'height': '100%',
        'background-image': 'url("/assets/Santiago_Bernabeu_Stadium_-_panoramio.jpg")',
        'background-size': 'cover',
        'background-repeat': 'no-repeat',
        'background-position': 'center',
        'opacity': 0.5,
        'z-index': -1  # Asegura que esté detrás de todo el contenido
    }),
    # Contenido principal
    html.Div([
        create_layout(teams),
        html.Div(id='hidden-div', style={'display': 'none'})
    ], style={'position': 'relative', 'z-index': 1})
], style={'position': 'relative'})


# Añadir estilos CSS adicionales para asegurar la distribución adecuada
app.clientside_callback(
    """
    function(stylesheet) {
        let style = document.createElement('style');
        style.innerHTML = `
            .graph-square {
                width: 48%;
                height: 48%;
                padding: 10px;
                box-sizing: border-box;
            }
            .player-info {
                padding: 15px;
                border: 1px solid #ddd;
                margin-bottom: 10px;
                background-color: #444;
                color: #fff;
                border-radius: 5px;
            }
            .player-info:hover {
                background-color: #555;
            }
        `;
        document.head.appendChild(style);
        return stylesheet;
    }
    """,
    Output('hidden-div', 'children'),
    Input('hidden-div', 'children')
)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
