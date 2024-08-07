import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px


def prepare_data_and_fig(team):

    matches_df = pd.read_csv(
        "./data/england-premier-league-matches-2018-to-2019-stats.csv")
    # Función para calcular puntos basado en los goles de local y visitante.
    def calculate_points(home_goals, away_goals):
        if home_goals > away_goals:
            return 3, 0
        elif home_goals < away_goals:
            return 0, 3
        else:
            return 1, 1


     # Aplica la función para calcular puntos y agregarlos al DataFrame.
    matches_df['home_points'], matches_df['away_points'] = zip(*matches_df.apply(
        lambda row: calculate_points(row['home_team_goal_count'], row['away_team_goal_count']), axis=1))

    # Inicializa un diccionario para seguir la progresión de puntos de cada equipo.
    teams = pd.unique(
        matches_df[['home_team_name', 'away_team_name']].values.ravel('K'))
    team_progress = {team: pd.DataFrame(
        columns=['timestamp', 'points']) for team in teams}

     # Calcular los puntos acumulativos para cada equipo.
    for index, row in matches_df.iterrows():
        home_team = row['home_team_name']
        away_team = row['away_team_name']
        home_points = row['home_points']
        away_points = row['away_points']
        timestamp = row['timestamp']
        
        # Agregar nuevos puntos al registro de cada equipo.
        if team_progress[home_team].empty:
            new_row = pd.DataFrame(
                {'timestamp': [timestamp], 'points': [home_points]})
            team_progress[home_team] = pd.concat(
                [team_progress[home_team], new_row], ignore_index=True)
        else:
            last_points = team_progress[home_team].iloc[-1]['points']
            new_row = pd.DataFrame(
                {'timestamp': [timestamp], 'points': [last_points + home_points]})
            team_progress[home_team] = pd.concat(
                [team_progress[home_team], new_row], ignore_index=True)

        if team_progress[away_team].empty:
            new_row = pd.DataFrame(
                {'timestamp': [timestamp], 'points': [away_points]})
            team_progress[away_team] = pd.concat(
                [team_progress[away_team], new_row], ignore_index=True)
        else:
            last_points = team_progress[away_team].iloc[-1]['points']
            new_row = pd.DataFrame(
                {'timestamp': [timestamp], 'points': [last_points + away_points]})
            team_progress[away_team] = pd.concat(
                [team_progress[away_team], new_row], ignore_index=True)

    #  Combinar los registros de progresión de todos los equipos en un solo DataFrame.
    all_teams_progress = pd.DataFrame()
    for team, progress in team_progress.items():
        progress['team'] = team
        all_teams_progress = pd.concat([all_teams_progress, progress])

     # Convertir la columna 'timestamp' a formato de fecha y hora.
    all_teams_progress['timestamp'] = pd.to_datetime(
        all_teams_progress['timestamp'])

    #  # Definir un mapa de colores para los equipos.
    team_colors = {
        'Manchester City': '#6CABDD',
        'Liverpool': '#D00027',
        'Chelsea': '#034694',
        'Tottenham Hotspur': '#132257',
        'Arsenal': '#EF0107',
        'Manchester United': '#DA291C',
        'Everton': '#003399',
        'Leicester City': '#003090',
        'West Ham United': '#7A263A',
        'Southampton': '#D71920',
        'Wolverhampton Wanderers': '#FDB913',
        'Brighton & Hove Albion': '#0057B8',
        'Newcastle United': '#241F20',
        'Crystal Palace': '#1B458F',
        'Aston Villa': '#95BFE5',
        'Burnley': '#6C1D45',
        'Norwich City': '#00A650',
        'Watford': '#FBEE23',
        'Bournemouth': '#D6001C',
        'Sheffield United': '#EE2737',
        'Leeds United': '#1D428A',
        'Brentford': '#C8102E',
        'Fulham': '#FFFFFF',
        'West Bromwich Albion': '#122F67',
    }

    # Crea un gráfico de líneas con colores  para cada equipo.
    fig = px.line(all_teams_progress, x='timestamp', y='points', color='team',
                  labels={'timestamp': 'Fecha',
                          'points': 'Puntos', 'team': 'Equipo'},
                  title='Progreso de los Equipos en la Temporada')

    # Actualizar el color de las líneas del gráfico según el equipo.
    fig.for_each_trace(lambda trace: trace.update(
        line=dict(color=team_colors.get(trace.name))))

    fig.update_layout(plot_bgcolor='#010103',
                      height=250,              
                      autosize=True,
                      xaxis_visible=False,
                      yaxis_visible=False,
                      showlegend=False,
                      margin=dict(l=0, r=0, t=0, b=0))

    return fig
