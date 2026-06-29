from testingpractice import city_country
import unittest

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        test_value = city_country('santiago','chile')
        self.assertEqual(test_value,'Santiago, Chile')

    def test_city_country_population(self):
        value_to_test = city_country('santiago','chile',5000000)
        self.assertEqual(value_to_test, 'Santiago, Chile - 5000000')

unittest.main()
