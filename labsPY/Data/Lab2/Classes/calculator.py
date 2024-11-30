from Data.Lab2.Functions.input_handling import get_input, validate_operator
from Data.Lab2.Functions.calculation_operations import perform_calculation
from Data.Lab9.Library.history_manager import HistoryManager
from Data.Lab2.Constants.settings import DECIMAL_PLACES

class Calculator:
    def __init__(self):
        self.memory = 0
        self.history_manager = HistoryManager()  # Історія через HistoryManager
        self.decimal_places = DECIMAL_PLACES  # Default decimal places

    def set_decimal_places(self):
        try:
            decimals = int(input("Enter the number of decimal places to display (0-10): "))
            if 0 <= decimals <= 10:
                self.decimal_places = decimals
                print(f"Decimal places set to {self.decimal_places}.")
            else:
                print("Please enter a valid number between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def calculate(self, num1, operator, num2):
        # Виклик perform_calculation і повернення результату
        return perform_calculation(num1, operator, num2, self.decimal_places)

    def run(self):
        while True:
            change_settings = input("Would you like to change calculator settings? (yes/no): ").lower()
            if change_settings == 'yes':
                self.set_decimal_places()

            num1, operator, num2 = get_input()
            if not validate_operator(operator):
                continue

            result = self.calculate(num1, operator, num2)
            if result is not None:
                print(f"Result: {result}")
                entry = f"{num1} {operator} {num2 if num2 is not None else ''} = {result}"
                self.history_manager.add_entry(entry)  # Додати до історії

                view_history = input("Would you like to see the calculation history? (yes/no): ").lower()
                if view_history == 'yes':
                    self.show_history()

            another = input("Do you want to perform another calculation? (yes/no): ").lower()
            if another != 'yes':
                self.show_history()
                print("Goodbye!")
                break

    def show_history(self):
        history = self.history_manager.get_history()
        if not history:
            print("No calculations in history.")
        else:
            print("Calculation History:")
            for entry in history:
                print(entry)
