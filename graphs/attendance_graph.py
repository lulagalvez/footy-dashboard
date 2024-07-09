import pandas as pd
import plotly.express as px

def prepare_attendance_fig():
    # Cargar los datos de asistencia
    matches_data = pd.read_csv("./data/england-premier-league-matches-2018-to-2019-stats.csv")
    matches_data['date_GMT'] = pd.to_datetime(matches_data['date_GMT'])
    matches_data.sort_values(by='date_GMT', inplace=True)

    # Crear el gráfico
    fig = px.line(matches_data, x='date_GMT', y='attendance', title='Evolución de la Asistencia a los Estadios',
                  labels={'date_GMT': 'Fecha', 'attendance': 'Asistencia'})
    fig.update_layout(plot_bgcolor='white', xaxis_title='Fecha', yaxis_title='Asistencia')

    return fig
