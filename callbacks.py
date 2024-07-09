from dash import Input, Output, ALL
import dash
from graphs.teamprogress_linegraph import prepare_data_and_fig
from graphs.performance_evolution import prepare_data_and_fig_evolution
from graphs.possession_goal_relation import prepare_possession_goals_fig


def register_callbacks(app):
    @app.callback(
        Output('graph-1', 'figure'),
        Output('graph-2', 'figure'),
        Output('graph-3', 'figure'),
        Output('graph-4', 'figure'),
        Output('player-1', 'children'),
        Output('player-2', 'children'),
        Output('player-3', 'children'),
        Output('player-4', 'children'),
        Output('team-name-display', 'children'),
        Input({'type': 'team-button', 'index': ALL}, 'n_clicks')
    )
    def update_dashboard(n_clicks):
        ctx = dash.callback_context
        if not ctx.triggered:
            default_team = 'Arsenal'  # or any default team
            return (
                prepare_data_and_fig_evolution(default_team),
                prepare_possession_goals_fig(default_team),
                prepare_data_and_fig(default_team),
                prepare_data_and_fig(default_team),
                "Player 1", "Player 2", "Player 3", "Player 4",
                default_team  # Display default team name
            )
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            team = eval(button_id)['index']
            return (
                prepare_data_and_fig_evolution(team),
                prepare_possession_goals_fig(team),
                prepare_data_and_fig(team),
                prepare_data_and_fig(team),
                f"Player 1 of {team}", f"Player 2 of {team}", f"Player 3 of {team}", f"Player 4 of {team}",
                team  # Update the display with the selected team name
            )
