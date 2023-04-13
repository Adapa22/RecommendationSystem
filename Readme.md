<h1 align=center> PROYECTO INDIVIDUAL Nº1 </h1>
<h1 align=center>Machine Learning Operations (MLOps)</h1>

Estudiante: Ada Parhuana 

<a href="https://imgbb.com/"><img src="https://i.ibb.co/1XMSL1Y/movie.png" alt="space" width="1000" height="450"></a>

# **Contenido:** 
<li><a href="#INTRODUCCIÓN">INTRODUCCIÓN</a></li>
<li><a href="#OBJETIVO">OBJETIVO</a></li>
<li><a href="#ETL">ETL</a></li>
<li><a href="#EDA">EDA </a></li>
<li><a href="#API">API</a></li>
<li><a href="#SISTEMA DE RECOMENDACIÓN">SISTEMA DE RECOMENDACIÓN</a></li>


## INTRODUCCIÓN
Como parte de la etapa de labs de Data Science en Henry se nos asignó en el rol de MLOps Engineer crear un modelo de ML de Sistema de Recomendación de servicios de plataformas streaming de películas y series. 

Para este proyecto se nos facilitó los datasets sin procesar de las plataformas: Amazon Prime Video, Disney Plus, Hulu y Netflix; y ratings.


## OBJETIVO
Recolectar y tratar los datos para crear un modelo de ML de sistema de recomendación de plataformas streaming. 


## ETL

El proceso de ETL consistió en tratar los datos contenidos en los datasets de 4 cvs de plataformas y  8 csv de ratings. 

Los querimientos para el tratamiento fueron los siguientes:

+	Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

+	Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”).

+	De haber fechas, deberán tener el formato AAAA-mm-dd
+	Los campos de texto deberán estar en minúsculas, sin excepciones
+	El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas).


## EDA

EL proceso de EDA consistió en utilizar técnicas y herramientas 
para analizar y explorar los datos con el objetivo de obtener información útil para la realizar nuestro modelo de ML de Sistema de Recomendación.

## API

Para el desarrollo de la API se utilizó el framework FastAPI. Para lo cual se dispuso de los datos ya tratados en el proceso de ETL.

Se realizaron 4 funciones en python para la realizar las consultas asignadas. Siendo estas las siguientes:

1.	Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration (year, platform, duration_type)).

2.	Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count (platform, scored, year)).

3.	Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform (platform)).

4.	Actor que más se repite según plataforma y año. (La función debe llamarse get_actor (platform, year)).

Link de la API (Se necesita estar registrado en https://render.com) : [Ir a la API](https://ada-rsystem.onrender.com/)

## SISTEMA DE RECOMENDACIÓN

El Sistema de Recomendación consistió en sugerir películas o series a usuarios, donde dado un id de usuario y una película, nos diga si la recomienda o no para dicho usuario.Con este proposito se seleccionó el algoritmo de SVD (Singular Value Decomposition) para entrenar el modelo.

Puedes entrar al sistema de recomendación de películas desde el siguiente [link](https://huggingface.co/spaces/adaap/Streaming)

## STATUS
En progreso


