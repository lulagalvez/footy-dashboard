import dash
from dash import html

dash.register_page(__name__, path='/', name="Introducción")

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("Premier League Football Dashboard"),
        "Bienvenidos al Dashboard de Estadísticas de la Premier League. Este dashboard tiene como objetivo proporcionar una visualización interactiva de las estadísticas clave de la liga, incluyendo goles por partido, rendimiento de los jugadores, estadísticas de victorias y derrotas, y comparaciones entre equipos. A través de gráficos y filtros personalizados, los usuarios pueden explorar y analizar los datos de la Premier League de manera intuitiva y detallada.",
        
    ]),
    html.Div(children=[
        html.Br(),
        html.H2("Fuentes de Datos"),
        html.B("League: "), "Contiene información sobre la liga, incluyendo el nombre, temporada, estado, formato, número de clubes, partidos totales, partidos completados, jornada, total de jornadas, progreso, promedio de goles por partido, goles promedio del equipo local y visitante, porcentaje de partidos con ambos equipos anotando, porcentaje de porterías a cero, riesgo de predicción, ventajas del equipo local en ataque y defensa, promedio de córners por partido, promedio de tarjetas por partido y estadísticas de goles y tarjetas en diferentes intervalos de tiempo.",
        html.Br(),
        html.B("Matches: "), "Incluye datos detallados de los partidos como la fecha, asistencia, equipos, árbitro, goles por equipo, goles al medio tiempo, córners, tarjetas, tiros, posesión del balón, y probabilidades de apuestas antes del partido.",
        html.Br(),
        html.B("Players: "), "Proporciona información sobre los jugadores como el nombre completo, edad, cumpleaños, liga, temporada, posición, club actual, minutos jugados, apariciones, goles, asistencias, tarjetas, y varios rankings y métricas de rendimiento.",
        html.Br(),
        html.B("Teams 1: "), "Contiene estadísticas detalladas del equipo incluyendo partidos jugados, victorias, empates, derrotas, goles anotados y concedidos, posición en la liga, posesión promedio, tiros, y varias métricas de rendimiento divididas entre partidos en casa y fuera.",
        html.Br(),
        html.B("Teams 2: "), "Incluye estadísticas adicionales de los equipos como la asistencia promedio, tiempo por gol anotado y concedido, puntos al medio tiempo, córners, tarjetas, y porcentajes de diferentes eventos como goles y córners en diferentes intervalos.",
    ])
], className="bg-light p-4 m-2")