import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from RunnerFacade import RunnerFacade

if __name__ == "__main__":
    facade = RunnerFacade()
    while True:
        facade.display_menu()
        choice = input("Введіть номер лабораторної роботи для запуску (або 'q' для виходу): ")
        if choice.lower() == 'q':
            print("Завершення роботи.")
            break
        try:
            lab_number = int(choice)
            facade.run_lab(lab_number)
        except ValueError:
            print("Будь ласка, введіть коректний номер.")
