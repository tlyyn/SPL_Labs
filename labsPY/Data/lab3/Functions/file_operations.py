import os

def save_to_file(art, directory="Assets", base_name="art"):
    """Зберігає ASCII-арт у новий файл з унікальним іменем в папці Arts."""
    # Переконуємось, що папка існує, і якщо ні, то створюємо її
    os.makedirs(directory, exist_ok=True)
    filename = get_unique_filename(directory, base_name)
    with open(filename, "w") as file:
        file.write(art)
    print(f"ASCII-арт збережено у файл: {filename}")

def get_unique_filename(directory, base_name="art", extension=".txt"):
    """Генерує унікальне ім'я файлу у вказаній папці."""
    existing_files = os.listdir(directory)
    i = 1
    while True:
        filename = f"{base_name}{i}{extension}"
        if filename not in existing_files:
            return os.path.join(directory, filename)
        i += 1
