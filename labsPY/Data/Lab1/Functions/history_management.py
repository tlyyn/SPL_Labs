def store_memory(calculator, value):
    calculator.memory = value
    print(f"Stored {value} in memory.")

def show_memory(calculator):
    print(f"Memory value: {calculator.memory}")
    return calculator.memory

def show_history(calculator):
    if not calculator.history:
        print("No calculations in history.")
    else:
        print("Calculation History:")
        for entry in calculator.history:
            print(entry)
