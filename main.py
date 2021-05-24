from utilities.rapidapi import RapidApi
from utilities.management_dataframe import ManagementDataframe
from db import InteractionsDatabase, Connection

try:
    serie_regions = RapidApi.get_regions()

    dataframe_info_reg_city = ManagementDataframe.generate_dataframe(serie_regions)

    print(f'\n\n\n{dataframe_info_reg_city}\n\n\n\n')

    time_serie = dataframe_info_reg_city['Time']
    print(f'\nTiempo total: {time_serie.sum()}')
    print(f'Tiempo promedio: {time_serie.mean()}')
    print(f'Tiempo minimo: {time_serie.min()}')
    print(f'Tiempo maximo: {time_serie.max()}')


    dataframe_info_reg_city.to_json('./data/info_execution.json')

    Connection.create_db()

    InteractionsDatabase.save_info_regions(dataframe_info_reg_city)
except Exception as e:
    print(f"Ha ocurrido un error inesperado:\n{e}")
