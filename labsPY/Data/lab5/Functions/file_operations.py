import os


def save_ascii_art(art_list, folder=None):
    # Перевірка, чи задана папка для збереження
    if folder is None:
        # Використовуємо шлях до папки `Assets` всередині `lab5`
        folder = os.path.join(os.path.dirname(__file__), "..", "Assets")

    # Створюємо папку, якщо вона не існує
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Рахуємо існуючі файли art*.txt у папці, щоб визначити ім'я нового файлу
    existing_files = [f for f in os.listdir(folder) if f.startswith("art") and f.endswith(".txt")]
    next_index = len(existing_files) + 1
    file_path = os.path.join(folder, f"art{next_index}.txt")

    # Перетворюємо список art_list у один рядок, об'єднуючи елементи через новий рядок
    full_art = "\n\n".join(art_list)

    # Записуємо ASCII-арт у файл
    try:
        with open(file_path, "w") as file:
            file.write(full_art)
        return file_path  # Повертаємо ім'я файлу, якщо збереження успішне
    except Exception as e:
        print(f"Помилка при збереженні ASCII-арту: {e}")
        return None
