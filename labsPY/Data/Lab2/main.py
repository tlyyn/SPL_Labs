
from .logging_setup import setup_logging
setup_logging(r"/mnt/data/labsPY_extracted/labsPY/Data/Logs/Lab2.log")
from Data.Lab2.Classes.calculator import Calculator

def run():
    print("Starting Calculator in Lab 2...")
    calc = Calculator()
    calc.run()
