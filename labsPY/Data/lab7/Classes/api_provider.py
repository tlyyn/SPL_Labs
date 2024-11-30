import requests
from Data.lab7.Constants.settings import API_KEY, BASE_URL

class APIProvider:
    SUPPORTED_CURRENCIES = ["USD", "EUR", "UAH", "AED", "GBP", "JPY", "CAD", "AUD"]
    def get_rate(self, base_currency, target_currency):
        if base_currency not in self.SUPPORTED_CURRENCIES or target_currency not in self.SUPPORTED_CURRENCIES:
            print(f"Currency not supported. Supported currencies are: {', '.join(self.SUPPORTED_CURRENCIES)}")
            return None

        response = requests.get(f"{BASE_URL}/{base_currency}", params={"access_key": API_KEY})
        data = response.json()
        return data.get("rates", {}).get(target_currency)
