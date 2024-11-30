from Data.lab3.Constants.settings import DEFAULT_FONT, DEFAULT_COLOR

def set_art_size(self):
    while True:
        try:
            width_input = input("Введіть ширину ASCII-арту (натисніть Enter для стандартної 80): ")
            if width_input:
                self.width = int(width_input)  # Встановлюємо ширину користувача
            else:
                self.width = 80  # Якщо користувач не ввів значення, встановлюємо 80 за замовчуванням

            height_input = input("Введіть висоту (натисніть Enter для пропуску): ")
            if height_input:
                self.height = int(height_input)

            break  # Вихід з циклу, якщо введені значення коректні
        except ValueError:
            print("Невірний ввід. Введіть числове значення або натисніть Enter для значення за замовчуванням.")

