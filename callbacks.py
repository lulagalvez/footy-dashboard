from dash import Input, Output, ALL
from graphs.teamprogress_linegraph import prepare_data_and_fig

def register_callbacks(app):
    @app.callback(
        Output('output-1', 'children'),
        Output('output-2', 'children'),
        Output('main-graph', 'figure'),
        Input({'type': 'team-button', 'index': ALL}, 'n_clicks')
    )
    def update_dashboard(n_clicks):
        ctx = dash.callback_context
        if not ctx.triggered:
            return "Output 1: No team selected", "Output 2: No team selected", prepare_data_and_fig()
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            team = eval(button_id)['index']
            return f"Output 1: {team}", f"Output 2: Selected Value: {team}", prepare_data_and_fig(team)
