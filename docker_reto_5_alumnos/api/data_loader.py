import pandas as pd

def cargar_excel():
    df = pd.read_excel("C:/Users/pablo/Desktop/retos/Reto-5-azul-claro/docker_reto_5_alumnos/datos/datos.xlsx")
    return df.to_dict(orient="records")

