def get_user_input():
    print("Welcome to ASCII art generator!")
    text = input("Enter the text: ")
    symbols = input("Enter the symbol: ")

    try:
        height = int(input("Enter the height: "))
        width = int(input("Enter the width: "))
    except ValueError:
        print("Invalid input. Using default size (height=5, width=5).")
        height = 5
        width = 5

    alignment = input("Enter the alignment (left, center, right): ")
    if alignment not in ["left", "center", "right"]:
        print("Invalid alignment. Defaulting to left.")
        alignment = "left"

    color = input("Enter the color (white, black, or gray): ")

    return text, symbols, height, width, alignment, color
