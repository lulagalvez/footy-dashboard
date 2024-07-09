from dash import Input, Output, ALL
from graphs.teamprogress_linegraph import prepare_data_and_fig

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
        Input({'type': 'team-button', 'index': ALL}, 'n_clicks')
    )
    def update_dashboard(n_clicks):
        ctx = dash.callback_context
        if not ctx.triggered:
            return prepare_data_and_fig(), prepare_data_and_fig(), prepare_data_and_fig(), prepare_data_and_fig(), "Player 1", "Player 2", "Player 3", "Player 4"
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            team = eval(button_id)['index']
            # Aquí deberás agregar la lógica para obtener los gráficos y jugadores del equipo seleccionado
            return prepare_data_and_fig(team), prepare_data_and_fig(team), prepare_data_and_fig(team), prepare_data_and_fig(team), f"Player 1 of {team}", f"Player 2 of {team}", f"Player 3 of {team}", f"Player 4 of {team}"
