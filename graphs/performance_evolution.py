import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def prepare_data_and_fig_evolution(team_name):
    # Load the data
    matches_df = pd.read_csv(
        './data/england-premier-league-matches-2018-to-2019-stats.csv')

    # Filter matches where the selected team played either at home or away
    team_matches = matches_df[(matches_df['home_team_name'] == team_name) | (
        matches_df['away_team_name'] == team_name)].copy()

    # Convert date to datetime specifying the exact format
    team_matches['date_GMT'] = pd.to_datetime(
        team_matches['date_GMT'], format='%b %d %Y - %I:%M%p')

    # Calculate points per game
    def calculate_points(row):
        if row['home_team_name'] == team_name:
            if row['home_team_goal_count'] > row['away_team_goal_count']:
                return 3  # win
            elif row['home_team_goal_count'] == row['away_team_goal_count']:
                return 1  # draw
            else:
                return 0  # loss
        else:
            if row['away_team_goal_count'] > row['home_team_goal_count']:
                return 3  # win
            elif row['away_team_goal_count'] == row['home_team_goal_count']:
                return 1  # draw
            else:
                return 0  # loss

    team_matches['points_per_game'] = team_matches.apply(
        calculate_points, axis=1)

    # Set goals scored and conceded depending on whether the team is home or away
    team_matches['goals_scored'] = team_matches.apply(
        lambda x: x['home_team_goal_count'] if x['home_team_name'] == team_name else x['away_team_goal_count'], axis=1)
    team_matches['goals_conceded'] = team_matches.apply(
        lambda x: x['away_team_goal_count'] if x['home_team_name'] == team_name else x['home_team_goal_count'], axis=1)

    # Create subplots
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.1)

    # Add line chart for points per game
    fig.add_trace(
        go.Scatter(x=team_matches['date_GMT'], y=team_matches['points_per_game'],
                   mode='lines+markers', name='Puntos por partido'),
        row=1, col=1
    )

    # Add line chart for goals scored
    fig.add_trace(
        go.Scatter(x=team_matches['date_GMT'], y=team_matches['goals_scored'],
                   mode='lines+markers', name='Goles anotados'),
        row=2, col=1
    )

    # Add line chart for goals conceded
    fig.add_trace(
        go.Scatter(x=team_matches['date_GMT'], y=team_matches['goals_conceded'],
                   mode='lines+markers', name='Goles perdidos'),
        row=2, col=1
    )

    # Update layout to improve viewing
    fig.update_layout(title={
                            'text': "Comparativa de Puntos y Goles",
                            'font': {
                                'color': 'white'
                            },
                            'x': 0.5, 
                            'xanchor': 'center',
                            'yanchor': 'top'
                        },
                      plot_bgcolor='#010103',
                      paper_bgcolor='#010103',
                      height=300,
                      autosize=True,
                      xaxis_visible=False,
                      yaxis_visible=False,
                      showlegend=True,
                      margin=dict(l=20, r=20, t=50, b=20),
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
