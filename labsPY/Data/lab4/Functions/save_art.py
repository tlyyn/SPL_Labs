import os


def save_ascii_art(art, base_name="art"):
    """Зберігає ASCII-арт у новий файл з унікальним іменем в папці SavedArts."""
    # Отримуємо абсолютний шлях до директорії, де знаходиться lab4_main.py
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Переходимо на рівень вище, щоб знайти папку lab4
    lab4_directory = os.path.abspath(os.path.join(script_directory, '..', 'SavedArts'))

    # Переконуємось, що цільова папка існує, і якщо ні, то створюємо її
    os.makedirs(lab4_directory, exist_ok=True)

    # Отримуємо унікальне ім'я файлу
    filename = get_unique_filename(lab4_directory, base_name)

    # Записуємо ASCII-арт у файл
    with open(filename, "w") as file:
        file.write(art)

    print(f"ASCII-арт збережено у файл: {filename}")


def get_unique_filename(directory, base_name="art", extension=".txt"):
    """Генерує унікальне ім'я файлу у вказаній папці."""
    existing_files = os.listdir(directory)
    i = 1

    # Генеруємо ім'я, поки не знайдемо унікальне
    while True:
        filename = f"{base_name}{i}{extension}"
        if filename not in existing_files:
            return os.path.join(directory, filename)
        i += 1
