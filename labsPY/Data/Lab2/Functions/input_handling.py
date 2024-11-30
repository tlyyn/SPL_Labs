def get_input():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, ^, √, %): ")
        num2 = None
        if operator != '√':
            num2 = float(input("Enter the second number: "))
        return num1, operator, num2
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_input()

def validate_operator(operator):
    if operator in ['+', '-', '*', '/', '^', '√', '%']:
        return True
    print("Invalid operator. Please enter a valid operator.")
    return False
