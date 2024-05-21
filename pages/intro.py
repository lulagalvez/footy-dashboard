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
        html.B("League: "), html.Ul([
            html.Li("Nombre"),
            html.Li("Temporada"),
            html.Li("Estado"),
            html.Li("Formato"),
            html.Li("Número de clubes"),
            html.Li("Partidos totales"),
            html.Li("Partidos completados"),
            html.Li("Jornada"),
            html.Li("Total de jornadas"),
            html.Li("Progreso"),
            html.Li("Promedio de goles por partido"),
            html.Li("Goles promedio del equipo local"),
            html.Li("Goles promedio del equipo visitante"),
            html.Li("Porcentaje de partidos con ambos equipos anotando"),
            html.Li("Porcentaje de porterías a cero"),
            html.Li("Riesgo de predicción"),
            html.Li("Ventajas del equipo local en ataque y defensa"),
            html.Li("Promedio de córners por partido"),
            html.Li("Promedio de tarjetas por partido"),
            html.Li("Estadísticas de goles y tarjetas en diferentes intervalos de tiempo")
        ]),
        html.Br(),
        html.B("Matches: "), html.Ul([
            html.Li("Fecha"),
            html.Li("Asistencia"),
            html.Li("Equipos"),
            html.Li("Árbitro"),
            html.Li("Goles por equipo"),
            html.Li("Goles al medio tiempo"),
            html.Li("Córners"),
            html.Li("Tarjetas"),
            html.Li("Tiros"),
            html.Li("Posesión del balón"),
            html.Li("Probabilidades de apuestas antes del partido")
        ]),
        html.Br(),
        html.B("Players: "), html.Ul([
            html.Li("Nombre completo"),
            html.Li("Edad"),
            html.Li("Cumpleaños"),
            html.Li("Liga"),
            html.Li("Temporada"),
            html.Li("Posición"),
            html.Li("Club actual"),
            html.Li("Minutos jugados"),
            html.Li("Apariciones"),
            html.Li("Goles"),
            html.Li("Asistencias"),
            html.Li("Tarjetas"),
            html.Li("Rankings y métricas de rendimiento")
        ]),
        html.Br(),
        html.B("Teams 1: "), html.Ul([
            html.Li("Partidos jugados"),
            html.Li("Victorias"),
            html.Li("Empates"),
            html.Li("Derrotas"),
            html.Li("Goles anotados"),
            html.Li("Goles concedidos"),
            html.Li("Posición en la liga"),
            html.Li("Posesión promedio"),
            html.Li("Tiros"),
            html.Li("Métricas de rendimiento en casa y fuera")
        ]),
        html.Br(),
        html.B("Teams 2: "), html.Ul([
            html.Li("Asistencia promedio"),
            html.Li("Tiempo por gol anotado y concedido"),
            html.Li("Puntos al medio tiempo"),
            html.Li("Córners"),
            html.Li("Tarjetas"),
            html.Li("Porcentajes de eventos en diferentes intervalos")
        ])
    ])
], className="bg-light p-4 m-2")