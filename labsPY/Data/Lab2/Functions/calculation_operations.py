def perform_calculation(num1, operator, num2, decimal_places):
    # Check if inputs are numeric
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        print("Error: Non-numeric input detected.")
        return None

    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2
        elif operator == '√':
            result = num1 ** 0.5
        elif operator == '%':
            result = num1 % num2
        else:
            print("Error: Invalid operator.")
            return None
        return round(result, decimal_places)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
