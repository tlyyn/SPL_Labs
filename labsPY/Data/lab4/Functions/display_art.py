def display_ascii_art(art, color):
    color_code = ''
    if color.lower() == 'white':
        color_code = '\u001b[37;1m'
    elif color.lower() == 'black':
        color_code = '\u001b[30m'
    elif color.lower() == 'gray':
        color_code = '\u001b[90m'

    colored_art = f"{color_code}{art}\u001b[0m"
    print(colored_art)
