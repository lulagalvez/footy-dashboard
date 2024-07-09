import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def prepare_data_and_fig_evolution(team_name):
    # Load the data
    matches_df = pd.read_csv(
        './data/england-premier-league-matches-2018-to-2019-stats.csv')

    # Filtra los partidos en los que el equipo seleccionado jugó como local o visitante.
    team_matches = matches_df[(matches_df['home_team_name'] == team_name) | (
        matches_df['away_team_name'] == team_name)].copy()

    # Convierte la columna de fecha a formato datetime
    team_matches['date_GMT'] = pd.to_datetime(
        team_matches['date_GMT'], format='%b %d %Y - %I:%M%p')

    #  Calcula los puntos obtenidos en cada partido.
    def calculate_points(row):
        if row['home_team_name'] == team_name:
            if row['home_team_goal_count'] > row['away_team_goal_count']:
                return 3  # victoria
            elif row['home_team_goal_count'] == row['away_team_goal_count']:
                return 1  # empate
            else:
                return 0  # derrota
        else:
            if row['away_team_goal_count'] > row['home_team_goal_count']:
                return 3  # victoria
            elif row['away_team_goal_count'] == row['home_team_goal_count']:
                return 1  # empate
            else:
                return 0  # derrota
            
     # Aplicar la función de cálculo de puntos a cada fila.
    team_matches['points_per_game'] = team_matches.apply(
        calculate_points, axis=1)

     # Calcular goles anotados y recibidos dependiendo si el equipo juega local o fuera.
    team_matches['goals_scored'] = team_matches.apply(
        lambda x: x['home_team_goal_count'] if x['home_team_name'] == team_name else x['away_team_goal_count'], axis=1)
    team_matches['goals_conceded'] = team_matches.apply(
        lambda x: x['away_team_goal_count'] if x['home_team_name'] == team_name else x['home_team_goal_count'], axis=1)

    # rear un layout de subplots: 2 filas, 1 columna, ejes X compartidos.
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.1)

    # Agrega un gráfico de líneas para los puntos por partido en la primera fila.
    fig.add_trace(
        go.Scatter(x=team_matches['date_GMT'], y=team_matches['points_per_game'],
                   mode='lines+markers', name='Puntos por partido'),
        row=1, col=1
    )

    # Agrega un gráfico de líneas para los goles anotados en la segunda fila.
    fig.add_trace(
        go.Scatter(x=team_matches['date_GMT'], y=team_matches['goals_scored'],
                   mode='lines+markers', name='Goles anotados'),
        row=2, col=1
    )

    # Agregar un gráfico de líneas para los goles concedidos en la segunda fila.
    fig.add_trace(
        go.Scatter(x=team_matches['date_GMT'], y=team_matches['goals_conceded'],
                   mode='lines+markers', name='Goles perdidos'),
        row=2, col=1
    )

     # Actualiza el diseño general
    fig.update_layout(plot_bgcolor='#010103',
                      paper_bgcolor='#010103',
                      height=300,
                      autosize=True,
                      xaxis_visible=False,
                      yaxis_visible=False,
                      showlegend=True,
                      margin=dict(l=20, r=20, t=20, b=20),
                      legend=dict(
                          orientation="h",
                          x=0.5,
                          y=-0.1,
                          xanchor='center',
                          yanchor='top',
                          font=dict(
                              color='white'
                          )
                      ))

    fig.update_xaxes(title_text="", showticklabels=False, row=2, col=1)
    fig.update_yaxes(title_text="", showticklabels=False, row=2, col=1)

    return fig
