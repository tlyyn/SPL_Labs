from Data.Lab1.Functions.input_handling import get_input, validate_operator
from Data.Lab1.Functions.calculation_operations import perform_calculation
from Data.Lab1.Functions.history_management import store_memory, show_history
from Data.Lab1.Constants.settings import DECIMAL_PLACES


class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []
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
        # Wrapper method to call perform_calculation and return result
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
                self.history.append(f"{num1} {operator} {num2 if num2 is not None else ''} = {result}")
                store_memory(self, result)

                view_history = input("Would you like to see the calculation history? (yes/no): ").lower()
                if view_history == 'yes':
                    show_history(self)

            another = input("Do you want to perform another calculation? (yes/no): ").lower()
            if another != 'yes':
                show_history(self)
                print("Goodbye!")
                break
