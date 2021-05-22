from requests import request
from encrypt import CustomEncrypting
import random

URL_COUNTRIES_BY_REGION = 'https://restcountries.eu/rest/v2/region/{}'

class WildCard():

    @classmethod
    def get_one_country_language_by_region(cls, region):
        response = request("GET", URL_COUNTRIES_BY_REGION.format(region))
        response = response.json()
        index = random.randint(0, (len(response) - 1))
        country_selected = response[index]
        name_country = country_selected.get('name')
        language = (country_selected.get('languages'))[0]
        # print(language)
        language_encrypt = CustomEncrypting.sha1_hexdigest(language.get('name'))
        return (name_country, language_encrypt)
