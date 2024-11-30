
from .logging_setup import setup_logging
setup_logging(r"/mnt/data/labsPY_extracted/labsPY/Data/Logs/lab7.log")
# Data/Lab7/main.py
from Data.lab7.Interfaces.cli import main

if __name__ == "__main__":
    main()

def run():
    # Викликайте головну функцію запуску вашої лабораторної роботи
    main()  # Якщо головна функція називається main()
