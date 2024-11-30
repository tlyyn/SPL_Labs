import os
import json

HISTORY_FILE = os.path.join("Data", "Lab7", "Assets", "history.json")


def save_to_history(entry):
    """Save a conversion entry to history."""
    # Ensure the Assets directory exists
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

    # Load existing history, add the new entry, and save it back
    history = load_history()
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def load_history():
    """Load the history from the JSON file."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


def display_history():
    """Display the history of conversions in a formatted way."""
    history = load_history()
    if not history:
        print("No history available.")
        return
    print("\nConversion History:")
    for entry in history:
        print(f"{entry['amount']} {entry['base']} to {entry['target']} at rate {entry['rate']}: {entry['result']}")
    print()
