import pandas as pd

class CSVLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print("Дані успішно завантажені.")
        except Exception as e:
            print(f"Помилка завантаження даних: {e}")
        return self.data
