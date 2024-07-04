import dash
from dash import html, dcc

# Assuming you've registered this page appropriately in your Dash app configuration
dash.register_page(__name__, path='/teams', name="Teams Overview")

# List of Premier League teams
teams = [
    "Arsenal", "Aston Villa", "Brentford", "Brighton", "Burnley",
    "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leeds United",
    "Leicester City", "Liverpool", "Manchester City", "Manchester United",
    "Newcastle United", "Norwich City", "Southampton", "Tottenham Hotspur",
    "Watford", "West Ham United", "Wolverhampton Wanderers"
]

####################### PAGE LAYOUT #############################
layout = html.Div([
    html.Div([
        html.H2("Premier League Teams", className="text-center"),
        html.P("Click on a team to view detailed statistics and information.", className="text-center"),
    ], className="mb-3"),
    html.Div([
        dcc.Link(html.Button(team, className="btn btn-primary square-button"), href=f"/team/{team.lower().replace(' ', '_')}")
        for team in teams
    ], className="btn-grid"),
    html.Div([
        html.Div(style={'display': 'none'})  # Ensuring CSS is applied correctly
    ])
], className="container bg-light p-4", style={
    'gridTemplateColumns': 'repeat(auto-fill, minmax(100px, 1fr))',
    'gap': '10px'
})

# Custom CSS applied directly in the layout
layout.children.append(html.Style("""
    .square-button {
        width: 100px;  # Set width
        height: 100px;  # Set height to make it square
        padding: 10px;
        margin: 5px;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        white-space: normal;
    }
    .btn-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));  # Adjust number of columns based on space
        gap: 10px;
    }
"""))

# Update this path according to your app structure if needed
if __name__ == '__main__':
    app.run_server(debug=True)
