import pandas as pd
from time import time
from .restcountries import WildCard

class ManagementDataframe():

    @classmethod
    def generate_dataframe(cls, serie_regions):
        # Dataframe where the complete information will be stored
        dataframe_info_reg_city = pd.DataFrame(
            columns=['Region', 'City Name', 'Language', 'Time']
        )
        for region in serie_regions:
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
        return dataframe_info_reg_city
