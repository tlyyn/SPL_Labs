import json
import os

class SettingsManager:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file

    def load_settings(self):
        if not os.path.exists(self.config_file):
            return {}
        with open(self.config_file, "r") as f:
            return json.load(f)

    def save_settings(self, settings):
        with open(self.config_file, "w") as f:
            json.dump(settings, f, indent=4)
