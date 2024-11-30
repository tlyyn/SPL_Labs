from Data.lab3.Interfaces.user_interface import run_ascii_art_generator
from Data.Lab9.Library.history_manager import HistoryManager
from Data.Lab9.Library.file_manager import FileManager


def main():
    print("Запуск ASCII-арт генератора (Lab3)...")
    history_manager = HistoryManager()
    file_manager = FileManager("lab3_ascii_history.txt")

    while True:
        # Генерація ASCII-арту
        ascii_art = run_ascii_art_generator()

        # Додати результат до історії
        history_manager.add_entry(ascii_art)

        # Запит користувача на збереження
        save_to_file = input("Would you like to save this ASCII art to a file? (yes/no): ").lower()
        if save_to_file == 'yes':
            file_manager.write_to_file(ascii_art)
            print("ASCII art saved successfully!")

        # Запит користувача на перегляд історії
        view_history = input("Would you like to see the ASCII art history? (yes/no): ").lower()
        if view_history == 'yes':
            show_ascii_history(history_manager)

        # Перевірити, чи продовжувати роботу
        another = input("Would you like to create another ASCII art? (yes/no): ").lower()
        if another != 'yes':
            print("Goodbye!")
            break


def show_ascii_history(history_manager):
    history = history_manager.get_history()
    if not history:
        print("No ASCII art history available.")
    else:
        print("ASCII Art History:")
        for index, art in enumerate(history, start=1):
            print(f"\n--- Art #{index} ---")
            print(art)


# Точка входу для Runner
def run():
    main()


if __name__ == "__main__":
    main()
