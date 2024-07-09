from dash import Input, Output, ALL, html
import dash
from graphs.teamprogress_linegraph import prepare_data_and_fig
from graphs.performance_evolution import prepare_data_and_fig_evolution
from graphs.possession_goal_relation import prepare_possession_goals_fig
from graphs.shot_goals import prepare_shots_goals_fig
from graphs.top_scorers import prepare_top_scorers_fig


def register_callbacks(app, df):
    @app.callback(
        Output('graph-1', 'figure'),
        Output('graph-2', 'figure'),
        Output('graph-3', 'figure'),
        Output('graph-4', 'figure'),
        Output('players-list', 'children'),
        Output('team-name-display', 'children'),
        Input({'type': 'team-button', 'index': ALL}, 'n_clicks')
    )
    def update_dashboard(n_clicks):
        ctx = dash.callback_context
        team = 'Arsenal'

        if not ctx.triggered:
            players_content = create_player_list(team, df)
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            team = eval(button_id)['index']
            players_content = create_player_list(team, df)

        return (
            prepare_data_and_fig_evolution(team),
            prepare_possession_goals_fig(team),
            prepare_shots_goals_fig(team),
            prepare_top_scorers_fig(team, df),
            players_content,
            team  # Display selected team name
        )


def create_player_list(team_name, df):
    filtered_players = df[df['Current Club'] == team_name]
    return [html.Div([
        html.H4(player['full_name']),
        html.P(f"Edad: {player['age']}"),
        html.P(f"Posicion: {player['position']}"),
        html.P(f"Minutos jugados: {player['minutes_played_overall']}")
    ], className='player-info', style={'margin': '10px', 'padding': '10px', 'border': '1px solid #ccc', 'border-radius': '5px', 'text-align': 'center'})
        for index, player in filtered_players.iterrows()]
