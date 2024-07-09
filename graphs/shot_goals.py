import pandas as pd
import plotly.express as px


def prepare_shots_goals_fig(team_name):
    matches_df = pd.read_csv(
        './data/england-premier-league-matches-2018-to-2019-stats.csv')

    team_matches = matches_df[(matches_df['home_team_name'] == team_name) | (
        matches_df['away_team_name'] == team_name)].copy()

    team_matches['date_GMT'] = pd.to_datetime(
        team_matches['date_GMT'], format='%b %d %Y - %I:%M%p')

    team_matches['goals_scored'] = team_matches.apply(
        lambda x: x['home_team_goal_count'] if x['home_team_name'] == team_name else x['away_team_goal_count'],
        axis=1
    )

    team_matches['shots'] = team_matches.apply(
        lambda x: x['home_team_shots'] if x['home_team_name'] == team_name else x['away_team_shots'],
        axis=1
    )

    fig = px.scatter(
        team_matches,
        x='date_GMT',
        y='goals_scored',
        size='shots',
        color='goals_scored',
        labels={'date_GMT': 'Fecha',
                'goals_scored': 'Goles', 'shots': 'Disparos'},
        size_max=28
    )

    fig.update_layout(plot_bgcolor='#010103',
                      paper_bgcolor='#010103',
                      font_color="white",
                      xaxis_title="",
                      yaxis_title="",
                      title="Goles anotados (Tamaño de burbuja representa la cantidad de disparos)",
                      height=300,
                      autosize=True)

    return fig
