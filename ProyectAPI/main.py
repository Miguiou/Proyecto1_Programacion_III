import Api.api as api
import UI.interface as interfaz


def main():
    departamento, registro = interfaz.ingreso_usuario()
    cliente = api.get_cliente()
    data = api.datos(departamento, registro, cliente)
    filtered_df = api.datos_filtrados(data)
    interfaz.mostrarDatos(filtered_df)
    
main()