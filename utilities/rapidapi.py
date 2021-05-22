from requests import request
import pandas as pd

URL_ALL_COUNTRIES = 'https://restcountries-v1.p.rapidapi.com/all'

HEADERS = {
    'x-rapidapi-key': "8fe403e351msh2659563699216adp13d1b1jsnce039b5dfb46",
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
}

class RapidApi():

    @classmethod
    def get_regions(cls):
        response = request("GET", URL_ALL_COUNTRIES, headers=HEADERS)
        regiones = list()
        for country in response.json():
            regiones.append(
                country.get('region')
                if country.get('region')
                else None
            )
        serie_regiones = pd.Series(regiones)
        return pd.Series(serie_regiones.dropna().unique())