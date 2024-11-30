class HistoryManager:
    def __init__(self):
        self.history = []

    def add_entry(self, entry):
        self.history.append(entry)

    def clear_history(self):
        self.history.clear()

    def get_history(self):
        return self.history
