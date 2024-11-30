
class DisplayStrategy:
    def display(self, base_currency, target_currency, rate, amount, result):
        pass

class ListDisplay(DisplayStrategy):
    def display(self, base_currency, target_currency, rate, amount, result):
        print(f"{amount} {base_currency} = {result:.2f} {target_currency} at rate {rate}")

class TableDisplay(DisplayStrategy):
    def display(self, base_currency, target_currency, rate, amount, result):
        print(f"{'Base':<10}{'Target':<10}{'Rate':<10}{'Result':<10}")
        print(f"{base_currency:<10}{target_currency:<10}{rate:<10.2f}{result:<10.2f}")
