from Data.lab4.Assets.ascii_alphabet import Alphabet
from Data.lab4.Functions.display_art import display_ascii_art
from Data.lab4.Functions.save_art import save_ascii_art
from Data.lab4.Functions.input_handler import get_user_input

class ASCIIArt:
    def __init__(self):
        self.text = ""
        self.symbols = ""
        self.height = 0
        self.width = 0
        self.alignment = "left"
        self.color = ""

    def generate_art(self):
        # Генерація ASCII-арту
        art_lines = []
        symbol_index = 0

        for i in range(max(self.height, len(Alphabet["A"]))):
            art_line = ""
            for char in self.text.upper():
                if char in Alphabet:
                    line = Alphabet[char][i % len(Alphabet[char])]
                    new_line = ""
                    for ch in line:
                        if ch == "#":
                            new_line += self.symbols[symbol_index % len(self.symbols)]
                            symbol_index += 1
                        else:
                            new_line += ch
                    art_line += new_line
                else:
                    art_line += " " * self.width

            if self.alignment == "center":
                art_line = art_line.center(
                    max(self.width, len(Alphabet["A"])) * len(self.text)
                )
            elif self.alignment == "right":
                art_line = art_line.rjust(
                    max(self.width, len(Alphabet["A"])) * len(self.text)
                )

            art_lines.append(art_line)
        return "\n".join(art_lines)

    def display_art(self):
        # Використання функції для відображення ASCII-арту
        display_ascii_art(self.generate_art(), self.color)

    def save_art(self):
        # Використання функції для збереження ASCII-арту в файл
        save_ascii_art(self.generate_art())

    def preview_art(self):
        # Попередній перегляд ASCII-арту
        print("Preview:")
        self.display_art()

    def user_input(self):
        # Отримання введення користувача
        self.text, self.symbols, self.height, self.width, self.alignment, self.color = get_user_input()

    def run_art(self):
        # Основний запуск генератора ASCII-арту
        self.user_input()
        self.display_art()
        if input("Do you want to save the art? (yes/no): ").lower() == "yes":
            self.save_art()
        self.preview_art()
