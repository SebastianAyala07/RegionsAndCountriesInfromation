import unittest
from utilities.management_dataframe import ManagementDataframe
import pandas as pd
from utilities.restcountries import WildCard
from utilities.rapidapi import RapidApi

class TestRestCountries(unittest.TestCase):

    def setUp(self):
        self.regions = [
            'Americas',
            'Asia',
            'Europe',
            'Oceania',
            'Africa',
            'Polar',
        ]
        super().setUp()

    def test_correct_request_country(self):
        for region in self.regions:
            country, language = WildCard.get_one_country_language_by_region(region)
            self.assertIsNotNone(country)
            self.assertIsNotNone(language)


class TestRapidApi(unittest.TestCase):

    def test_request_get_regions(self):
        regions = RapidApi.get_regions()
        self.assertTrue(regions.count() == 6)


class TestManagementDataFrame(unittest.TestCase):

    def setUp(self):
        self.regions = pd.Series([
            'Americas',
            'Asia',
            'Europe',
            'Oceania',
            'Africa',
            'Polar',
        ])
        super().setUp()

    def test_generate_dataframe(self):
        df = ManagementDataframe.generate_dataframe(self.regions)
        self.assertTrue(type(df) == pd.core.frame.DataFrame)
        self.assertTrue(df.shape[0] == 6)
        self.assertTrue(df.shape[1] == 4)


if __name__ == '__main__':
    unittest.main()