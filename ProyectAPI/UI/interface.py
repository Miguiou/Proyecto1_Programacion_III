def ingreso_usuario():
    departamento = input("Ingrese el nombre del departamento que desea consultar: ").upper()
    register = int(input("Ingrese el número de registros que desea consultar: "))

    return departamento, register

def mostrarDatos(filtered_df):
    nombrar_df = filtered_df.rename(columns={
        "ciudad_municipio_nom": " Ciudad ",
        "departamento_nom": " Departamento ",
        "edad" : "edad",
        "fuente_tipo_contagio": "Tipo de Contagio",
        "estado": "Estado",
        "recuperado": "Recuperado"})
    print(nombrar_df)