import json
import csv
import os

def save_to_json(data, filename="exchange_data.json"):
    try:
        # Define the absolute path to the Assets directory
        assets_dir = os.path.abspath(os.path.join("Data", "Lab7", "Assets"))
        # Ensure the Assets directory exists
        os.makedirs(assets_dir, exist_ok=True)

        # Define the full file path
        file_path = os.path.join(assets_dir, filename)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Failed to save JSON file: {e}")

def save_to_csv(data, filename="exchange_data.csv"):
    try:
        # Define the absolute path to the Assets directory
        assets_dir = os.path.abspath(os.path.join("Data", "Lab7", "Assets"))
        # Ensure the Assets directory exists
        os.makedirs(assets_dir, exist_ok=True)

        # Define the full file path
        file_path = os.path.join(assets_dir, filename)
        with open(file_path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Base", "Target", "Rate", "Amount", "Result"])
            writer.writerow(data)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Failed to save CSV file: {e}")
