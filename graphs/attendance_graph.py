import pandas as pd
import plotly.express as px

def prepare_attendance_fig():

    # Carga los datos de los partidos desde un archivo CSV, incluyendo fechas y asistencia.
    matches_data = pd.read_csv("./data/england-premier-league-matches-2018-to-2019-stats.csv")
    matches_data['date_GMT'] = pd.to_datetime(matches_data['date_GMT'])

    # Ordena los datos por fecha para asegurar que la línea del tiempo en el gráfico sea correcta.
    matches_data.sort_values(by='date_GMT', inplace=True)

    # Crea un gráfico de línea para visualizar la evolución de la asistencia a los estadios durante la temporada.
    fig = px.line(matches_data, x='date_GMT', y='attendance', title='Evolución de la Asistencia a los Estadios',
                  labels={'date_GMT': 'Fecha', 'attendance': 'Asistencia'})
    fig.update_layout(plot_bgcolor='white', xaxis_title='Fecha', yaxis_title='Asistencia')

    return fig
