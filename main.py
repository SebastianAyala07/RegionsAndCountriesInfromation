import pandas as pd
from requests import request
from restcountries import WildCard
from time import time
import hashlib

url = 'https://restcountries-v1.p.rapidapi.com/all'

headers = {
    'x-rapidapi-key': "8fe403e351msh2659563699216adp13d1b1jsnce039b5dfb46",
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
}

# Dataframe donde se almacenara la informacion completa
dataframe_info_reg_city = pd.DataFrame(
    columns=['Region', 'City Name', 'Language', 'Time']
)

response = request("GET", url, headers=headers)

regiones = []

for country in response.json():
    regiones.append(
        country.get('region')
        if country.get('region')
        else None
    )

serie_regiones = pd.Series(regiones)

serie_regiones = pd.Series(serie_regiones.dropna().unique())

for region in serie_regiones:
    time_start = time()
    country_name, country_language = WildCard.get_one_country_language_by_region(region)
    elapsed_time = time() - time_start
    time_total = "%0.10f seconds" % elapsed_time
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
