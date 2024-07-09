import pandas as pd
import plotly.express as px


def prepare_possession_goals_fig(team_name):
    matches_df = pd.read_csv(
        './data/england-premier-league-matches-2018-to-2019-stats.csv')
    # Filtra los partidos en los que participó el equipo 
    team_matches = matches_df[(matches_df['home_team_name'] == team_name) | (
        matches_df['away_team_name'] == team_name)].copy()

    # Convierte la columna de fechas a formato datetime.
    team_matches['date_GMT'] = pd.to_datetime(
        team_matches['date_GMT'], format='%b %d %Y - %I:%M%p')
    
    # Calcula los goles anotados por el equipo en cada partido.
    team_matches['goals_scored'] = team_matches.apply(
        lambda x: x['home_team_goal_count'] if x['home_team_name'] == team_name else x['away_team_goal_count'],
        axis=1
    )

    team_matches['average_possession'] = team_matches.apply(
        lambda x: x['home_team_possession'] if x['home_team_name'] == team_name else x['away_team_possession'],
        axis=1
    )

    # Create the scatter plot
    fig = px.scatter(
        team_matches,
        x='average_possession',
        y='goals_scored',
        labels={
            'average_possession': 'Posesión del balón (%)', 'goals_scored': 'Goles anotados'},
        trendline='ols'  # Add OLS trendline
    )

    fig.update_layout(plot_bgcolor='#010103',
                      paper_bgcolor='#010103',
                      font_color="white",
                      height=300,
                      autosize=True)

    return fig
