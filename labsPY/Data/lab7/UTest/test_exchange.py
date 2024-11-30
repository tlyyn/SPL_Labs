import unittest
from Data.lab7.Classes.currency_exchange_service import CurrencyExchangeService
from Data.lab7.Classes.api_provider import APIProvider

class TestCurrencyExchangeService(unittest.TestCase):
    def setUp(self):
        self.api_provider = APIProvider()
        self.service = CurrencyExchangeService(self.api_provider)

    def test_get_exchange_rate(self):
        rate = self.service.get_exchange_rate("USD", "EUR")
        self.assertIsInstance(rate, float)

    def test_convert_currency(self):
        result = self.service.convert_currency(100, "USD", "EUR")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, float)

if __name__ == "__main__":
    unittest.main()
