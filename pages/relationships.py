import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/relationship', name="Relaciones")

####################### DATASET #############################
matches_df = pd.read_csv("./data/england-premier-league-matches-2018-to-2019-stats.csv")

# Convert timestamp to datetime
matches_df['timestamp'] = pd.to_datetime(matches_df['timestamp'])

####################### LINE CHART #############################
def create_line_chart(column1="home_team_goal_count", column2="away_team_goal_count"):
    fig = px.line(matches_df, x='timestamp', y=[column1, column2], labels={'timestamp': 'Date'})
    fig.update_layout(
        title=f"Comparison of {column1} and {column2} Over Time",
        xaxis_title="Date",
        yaxis_title="Values",
        height=600
    )
    return fig

####################### WIDGETS #############################
columns = matches_df.columns

column1 = dcc.Dropdown(id="column1", options=[{"label": col, "value": col} for col in columns if col != 'timestamp'], value="home_team_goal_count", clearable=False)
column2 = dcc.Dropdown(id="column2", options=[{"label": col, "value": col} for col in columns if col != 'timestamp'], value="away_team_goal_count", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.Label("Column 1"), column1,
    html.Label("Column 2"), column2,
    dcc.Graph(id="line_chart")
])

####################### CALLBACKS ###############################
@callback(Output("line_chart", "figure"), [Input("column1", "value"), Input("column2", "value")])
def update_line_chart(column1, column2):
    return create_line_chart(column1, column2)
