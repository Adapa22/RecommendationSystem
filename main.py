from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
from typing import List
from typing import Union

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def welcome_to():
    html_content = """
    <html>
    <head>
        <style>
            body {
                background-color: black; /* fondo negro */
                text-align: center;
                position: relative;
                margin-bottom: 100px; /* Asegura que los botones no cubran otros contenidos */
            }
            img {
                position: absolute;
                bottom: 0;
                right: 50%;
                transform: translate(-50%);
            }
            .big-img {
                width: 60%;
            }
            .center-img {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
            }
            .btn-container {
                position: fixed;
                bottom: 0;
                width: 100%;
                background-color: #000;
                padding: 20px;
            }
            .btn {
                padding: 10px 18px;
                font-weight: bold;
                font-size: 18px;
                color: white;
                background-color: #1D3052; /* Azul claro */
                border: none;
                border-radius: 5px;
                margin: 10px;
            }
            .btn:hover {
                background-color: #15233B; /* Azul oscuro */
                cursor: pointer;
            }
            .logo-img {
                position: absolute;
                top: 10px;
                right: 10px;
                height: 50px;
            }
            .title {
                font-size: 24px;
                font-weight: bold;
                margin: 0 auto;
                color: white;
                text-align:center;
            }
            footer {
                position: fixed;
                bottom: 0;
                width: 100%;
                background-color: #000000;
                color: white;
                padding: 6px;
                font-size: 10px;
            }
        </style>
    </head>
    <body>
        <div>
            <img class="logo-img" src="https://i.ibb.co/FWsHJcZ/Henry.png" alt="Logo de Google">
        </div>
        ---
        <h1 class="title">¡Bienvenido! </h1>
        ---
        <div style="text-align: center;">
            <img class="big-img center-img" src="https://i.ibb.co/1XMSL1Y/movie.png" alt="Descripción de la imagen">
        </div>
        <div class="btn-container">
            <form>
                <button class="btn" formaction="/docs">Plataformas streaming </button>
            </form>
        </div>
        <footer>
            <p>Consulte su película favorita en la plataforma de su preferencia.</p>
        </footer>            
    </body>
    </html>
    """
    return html_content

# Leer el archivo CSV con la información de las películas
df = pd.read_csv('df_plataformas.csv')

# 1ra funcion : Película con mayor duración
@app.get("/get_max_duration")
def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    global df
    # Verificar si la plataforma es válida
    valid_platforms = ["amazon", "disney", "hulu", "netflix"]
    if platform not in valid_platforms:
        return "Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas."

    # Filtrar según los filtros indicados
    if year:
        df = df[df["release_year"] == year]
    if platform:
        df = df[df["platform"] == platform.lower()]
    if duration_type:
        if duration_type in ["m","mi", "min"]:
            df = df[df["duration_type"] == "min"]
        elif duration_type in ["season", "seasons"]:
            df = df[df["duration_type"] == "season"]

    # Encontrar la película o serie con la duración máxima
    max_duration_idx = df["duration_int"].idxmax()
    max_duration_title = df.loc[max_duration_idx].title

    return max_duration_title 

# 2da funcion : Cantidad de películas por plataforma con un puntaje mayor a XX 
@app.get("/get_score_count/{platform}/{scored}/{year}")
def get_score_count(platform: str, scored: float, year: int)-> Union[int, str]:
    global df
    # Verificar si la plataforma es válida
    valid_platforms = ["amazon", "disney", "hulu", "netflix"]
    if platform not in valid_platforms:
        return "Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas."
    
    # Filtrar las películas de la plataforma y año especificados
    platform_year_movies = df.query(f"platform == '{platform}' and release_year == {year}")
    
    # Seleccionar las películas con una puntuación mayor a 'scored'
    high_score_movies = platform_year_movies.loc[platform_year_movies['scored'] > scored]
    
    # Contar el número de películas que cumplen con los criterios anteriores y retornar el valor
    count_movies = high_score_movies['title'].count()

    # Retornor la cantidad de películas
    return count_movies

# 3da funcion : Cantidad de películas por plataforma 
@app.get("/get_count_platform/{platform}")
def get_count_platform(platform:str)-> Union[int, str]:
    global df
    # Verificar si la plataforma es válida
    valid_platforms = ["amazon", "disney", "hulu", "netflix"]
    if platform not in valid_platforms:
        return "Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas."
    
    # Filtrar las películas de la plataforma especificada
    platform_year_movies = df.query(f"platform == '{platform}'")
    
    # Contar el número de películas que cumple con el criterio anterior
    count_movies = platform_year_movies['platform'].count()

    # Retornor la cantidad de películas
    return count_movies

# 4da funcion : Actor que más se repite según plataforma y año
@app.get("/get_actor/{plataforma}/{year}")
def get_actor10(platform: str, year: int):
    global df
    # Verificar si la plataforma es válida
    valid_platforms = ["amazon", "disney", "hulu", "netflix"]
    if platform not in valid_platforms:
        return "Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas."

    # Filtrar por año y plataforma
    filtered_df = df[(df['platform'] == platform) & (df['release_year'] == year)]

    # Obtener el actor que más se repite en la columna 'cast'
    actors = filtered_df['cast'].str.split(',').explode().str.strip()
    actor_count = actors.value_counts()
    if actor_count.empty:
        return None
    else:
        return actor_count.index[0]