import pandas as pd
import plotly.express as px


def prepare_top_scorers_fig(team_name, df):
    team_players = df[df['Current Club'] == team_name]

    top_scorers = team_players.nlargest(8, 'goals_overall')

    fig = px.bar(top_scorers, x='full_name', y='goals_overall',
                 labels={'full_name': 'Nombre jugador',
                         'goals_overall': 'Goles'},
                 color='full_name',
                 color_discrete_sequence=px.colors.qualitative.Plotly)

    fig.update_layout(
        title="Top 8 Goleadores",
        plot_bgcolor='#010103',
        paper_bgcolor='#010103',
        font_color="white",
        xaxis_title='Nombre jugador',
        yaxis_title='Goles',
        xaxis_tickangle=-45,
        uniformtext_minsize=8,
        height=300,
        autosize=True,
        uniformtext_mode='hide',
        xaxis_visible=False,
        yaxis_visible=True,
        bargap=0.2
    )

    return fig
