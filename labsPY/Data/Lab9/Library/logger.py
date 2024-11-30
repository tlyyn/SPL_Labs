from datetime import datetime

class Logger:
    def __init__(self, log_file="app.log"):
        self.log_file = log_file

    def log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {level}: {message}\n")

    def log_error(self, message):
        self.log(message, level="ERROR")

    def log_info(self, message):
        self.log(message, level="INFO")
