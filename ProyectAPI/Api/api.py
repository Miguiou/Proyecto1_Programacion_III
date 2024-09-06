import pandas as pd
from sodapy import Socrata


def get_cliente():
    client = Socrata("www.datos.gov.co", None)

    return client


def datos(departamento, register, client):
    results = client.get("gt2j-8ykr", limit=register, departamento_nom=departamento)
    results_df = pd.DataFrame.from_records(results)

    return results_df


def datos_filtrados(results_df):
    mostrarcol = [
        "ciudad_municipio_nom", 
        "departamento_nom", 
        "edad", 
        "fuente_tipo_contagio",
        "estado", 
        "recuperado"
    ]
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    return results_df[mostrarcol]
