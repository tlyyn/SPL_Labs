
from .logging_setup import setup_logging
setup_logging(r"/mnt/data/labsPY_extracted/labsPY/Data/Logs/Lab1.log")
from Data.Lab1.Classes.calculator import Calculator
from Data.Lab9.Library.file_manager import FileManager
from Data.Lab9.Library.logger import Logger

def main():
    print("Запуск калькулятора в Lab1...")
    logger = Logger("lab1.log")  # Файл логів для Lab1
    file_manager = FileManager("lab1_history.txt")  # Файл для історії

    calc = Calculator()

    # Основний цикл роботи калькулятора
    calc.run()

    # Збереження історії після завершення
    logger.log("Saving history to file...")
    if calc.history:
        file_manager.write_to_file("\n".join(calc.history))
        logger.log("History saved successfully.")
    else:
        logger.log("No history to save.")

def run():
    main()

if __name__ == "__main__":
    main()
