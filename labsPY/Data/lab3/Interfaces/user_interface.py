from Data.lab3.Functions.input_handling import get_user_input
from Data.lab3.Functions.art_generator import generate_ascii_art
from Data.lab3.Functions.file_operations import save_to_file
from Data.lab3.Functions.preview import preview_art
from Data.lab3.Constants.settings import AVAILABLE_FONTS, AVAILABLE_COLORS


def choose_font():
    print("Available fonts:", ', '.join(AVAILABLE_FONTS))
    chosen_font = input("Choose a font from the list or press enter for default: ").strip().lower()
    return chosen_font if chosen_font in AVAILABLE_FONTS else "slant"


def choose_color():
    print("Available colors:", ', '.join(AVAILABLE_COLORS))
    chosen_color = input("Choose a color from the list or press enter for default: ").strip().lower()
    return chosen_color if chosen_color in AVAILABLE_COLORS else "white"


def run_ascii_art_generator():
    print("Welcome to ASCII Art Generator")

    # Введення користувача
    text = get_user_input()

    # Вибір шрифту і кольору
    font = choose_font()
    color = choose_color()

    # Генерація ASCII арту
    art = generate_ascii_art(text, font, color, 80)

    # Попередній перегляд
    if preview_art(art):
        save_to_file(art)
    else:
        print("Let's try again.")
        run_ascii_art_generator()  # Перезапуск процесу
