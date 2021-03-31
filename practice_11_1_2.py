import unittest
from practice_11_12 import get_city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city_country = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_city_country_population = get_city_country('santiago', 'chile', 
            5000000)

if __name__ == '__main__':
    unittest.main()