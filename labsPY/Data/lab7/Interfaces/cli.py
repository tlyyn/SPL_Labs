# CLI for user interaction
from Data.lab7.Classes.currency_exchange_service import CurrencyExchangeService
from Data.lab7.Classes.api_provider import APIProvider
from Data.lab7.Classes.display_strategy import ListDisplay, TableDisplay
from Data.lab7.Functions.data_saver import save_to_json, save_to_csv
from Data.lab7.Functions.history_manager import display_history, save_to_history


def main():
    api_provider = APIProvider()
    exchange_service = CurrencyExchangeService(api_provider)

    print("Supported currencies: USD, EUR, UAH, AED, GBP, JPY, CAD, AUD")

    while True:
        choice = input("Choose an action (convert/history/exit): ").strip().lower()
        if choice == "history":
            display_history()
            continue
        elif choice == "exit":
            break
        elif choice == "convert":
            base_currency = input("Enter the base currency (e.g., USD): ").upper()
            target_currency = input("Enter the target currency (e.g., EUR): ").upper()
            amount = float(input("Enter the amount: "))

            result = exchange_service.convert_currency(amount, base_currency, target_currency)
            if result is not None:
                rate = exchange_service.get_exchange_rate(base_currency, target_currency)
                display_choice = input("Choose display format (list/table): ").strip().lower()
                display_strategy = TableDisplay() if display_choice == "table" else ListDisplay()
                display_strategy.display(base_currency, target_currency, rate, amount, result)

                # Save query to history
                save_to_history({
                    "base": base_currency,
                    "target": target_currency,
                    "rate": rate,
                    "amount": amount,
                    "result": result
                })

                # Save result to a file if desired
                save_choice = input("Save result? (json/csv/none): ").strip().lower()
                if save_choice == "json":
                    save_to_json({"base": base_currency, "target": target_currency, "rate": rate, "amount": amount, "result": result})
                elif save_choice == "csv":
                    save_to_csv([base_currency, target_currency, rate, amount, result])
            else:
                print("Conversion failed. Please check the currencies and try again.")
        else:
            print("Invalid choice. Please enter 'convert', 'history', or 'exit'.")