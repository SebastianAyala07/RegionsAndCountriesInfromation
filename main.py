import pandas as pd
from requests import request
from utilities.restcountries import WildCard
from time import time
from utilities.rapidapi import RapidApi

# Dataframe donde se almacenara la informacion completa
dataframe_info_reg_city = pd.DataFrame(
    columns=['Region', 'City Name', 'Language', 'Time']
)

serie_regiones = RapidApi.get_regions()

for region in serie_regiones:
    time_start = time()
    country_name, country_language = WildCard.get_one_country_language_by_region(region)
    time_total = round(time() - time_start, 4)
    dataframe_info_reg_city = dataframe_info_reg_city.append(
        {
            'Region': region,
            'City Name': country_name,
            'Language': country_language,
            'Time': time_total,
        },
        ignore_index=True
    )

print(f'\n\n\n{dataframe_info_reg_city}\n\n\n\n')

time_serie = dataframe_info_reg_city['Time']
print(f'\nTiempo total: {time_serie.sum()}')
print(f'Tiempo promedio: {time_serie.mean()}')
print(f'Tiempo minimo: {time_serie.min()}')
print(f'Tiempo maximo: {time_serie.max()}')


dataframe_info_reg_city.to_json('./data/info_execution.json')

