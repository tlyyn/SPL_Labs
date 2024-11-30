class RunnerFacade:
    def __init__(self):
        self.labs = {
            1: "Lab1.main",
            2: "Lab2.main",
            3: "lab3.lab3_main",
            4: "lab4.lab4_main",
            5: "lab5.lab5_main",
            6: "lab6.test_runner",
            7: "lab7.main",
            8: "lab8.lab8_main"
        }

    def run_lab(self, lab_number):
        try:
            if lab_number in self.labs:
                module_path = self.labs[lab_number]
                module = __import__(f"Data.{module_path}", fromlist=[''])
                module.run()  # Викликає стандартну функцію запуску лабораторної
            else:
                print("Неправильний номер лабораторної роботи.")
        except Exception as e:
            print(f"Помилка під час запуску лабораторної: {e}")

    def display_menu(self):
        print("Доступні лабораторні роботи:")
        for number in self.labs.keys():
            print(f"{number} - Lab{number}")
