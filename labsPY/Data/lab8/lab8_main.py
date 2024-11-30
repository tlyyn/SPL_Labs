import os
from Data.lab8.Classes.csv_loader import CSVLoader
from Data.lab8.Classes.data_explorer import DataExplorer
from Data.lab8.Classes.data_preprocessor import DataPreprocessor
from Data.lab8.Classes.basic_visualization import BasicVisualization
from Data.lab8.Classes.advanced_visualization import AdvancedVisualization
from Data.lab8.Classes.multi_subplots import MultiSubplots


def main():
    # Визначаємо шлях до CSV-файлу
    file_path = os.path.join(os.path.dirname(__file__), 'Assets', 'data.csv')

    # Завантаження даних
    loader = CSVLoader(file_path)
    data = loader.load_data()

    if data is not None:
        # Дослідження даних
        explorer = DataExplorer(data)
        print("\n" + "=" * 30)
        print("Екстремальні значення по стовпцях:")
        print("-" * 30)
        min_values = explorer.data.min()
        max_values = explorer.data.max()
        print("Мінімальні значення:")
        for column, value in min_values.items():
            print(f"  {column}: {value}")
        print("\nМаксимальні значення:")
        for column, value in max_values.items():
            print(f"  {column}: {value}")
        print("=" * 30 + "\n")

        # Підготовка даних
        preprocessor = DataPreprocessor(data)
        aggregated_data = preprocessor.aggregate_sales_by_month()

        print("Продажі за місяцями:")
        print("-" * 30)
        for month, sales in aggregated_data.items():
            print(f"  {month}: {sales}")
        print("-" * 30 + "\n")

        # Створюємо об'єкти для візуалізації
        basic_viz = BasicVisualization(data)
        adv_viz = AdvancedVisualization(data)
        multi_viz = MultiSubplots(data)

        # Меню вибору візуалізації
        while True:
            print("\nОберіть тип діаграми для відображення:")
            print("1 - Лінійний графік продажів за місяцями")
            print("2 - Діаграма розсіювання продажів та кількості")
            print("3 - Гістограма продажів")
            print("4 - Секторна діаграма продуктів")
            print("5 - Піддіаграми: гістограми продажів та кількості")
            print("6 - Піддіаграми: діаграма розсіювання продажів та кількості")
            print("0 - Вийти")

            choice = input("Введіть номер варіанту: ")

            if choice == "1":
                basic_viz.line_plot("Month", "Sales", "Продажі за місяцями")
            elif choice == "2":
                adv_viz.scatter_plot("Sales", "Quantity", "Діаграма розсіювання: Продажі та Кількість")
            elif choice == "3":
                adv_viz.histogram("Sales", bins=10, title="Гістограма продажів")
            elif choice == "4":
                adv_viz.pie_chart("Product", title="Секторна діаграма продуктів")
            elif choice == "5":
                multi_viz.create_subplots(["Sales", "Quantity"], plot_type='histogram')
            elif choice == "6":
                multi_viz.create_subplots(["Sales", "Quantity"], plot_type='scatter')
            elif choice == "0":
                print("Вихід із програми.")
                break
            else:
                print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()

def run():
    # Викликайте головну функцію запуску вашої лабораторної роботи
    main()  # Якщо головна функція називається main()
