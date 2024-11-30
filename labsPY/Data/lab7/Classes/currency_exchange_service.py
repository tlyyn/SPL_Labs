# CurrencyExchangeService (Facade)
class CurrencyExchangeService:
    def __init__(self, api_provider):
        self.api_provider = api_provider

    def get_exchange_rate(self, base_currency, target_currency):
        rate = self.api_provider.get_rate(base_currency, target_currency)
        return rate

    def convert_currency(self, amount, base_currency, target_currency):
        rate = self.get_exchange_rate(base_currency, target_currency)
        return amount * rate if rate else None
