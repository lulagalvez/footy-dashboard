import pandas as pd
import plotly.express as px


def prepare_top_scorers_fig(team_name, df):
    # Filtra los jugadores del equipo especificado.
    team_players = df[df['Current Club'] == team_name]
     # Selecciona los 8 jugadores con mayor número de goles.
    top_scorers = team_players.nlargest(8, 'goals_overall')

     # Crea un gráfico de barras de los máximos goleadores usando Plotly Express.
    fig = px.bar(top_scorers, x='full_name', y='goals_overall',
                 labels={'full_name': 'Nombre jugador',
                         'goals_overall': 'Goles'},
                 color='full_name',
                 color_discrete_sequence=px.colors.qualitative.Plotly)

    fig.update_layout(
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
        yaxis_visible=False,
        bargap=0.2
    )

    return fig
