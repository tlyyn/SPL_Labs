class DataExplorer:
    def __init__(self, data):
        self.data = data

    def get_extreme_values(self):
        try:
            print("Екстремальні значення по стовпцях:")
            min_values = self.data.min()
            max_values = self.data.max()
            print("Мінімальні значення:\n", min_values)
            print("Максимальні значення:\n", max_values)
        except Exception as e:
            print(f"Помилка при визначенні екстремальних значень: {e}")
