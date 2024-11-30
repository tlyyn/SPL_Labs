import os

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_file(self, data, mode='w'):
        with open(self.file_path, mode) as f:
            f.write(data)

    def read_from_file(self):
        if not os.path.exists(self.file_path):
            return None
        with open(self.file_path, 'r') as f:
            return f.read()

    def file_exists(self):
        return os.path.exists(self.file_path)
