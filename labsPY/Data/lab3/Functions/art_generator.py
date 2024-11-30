import pyfiglet
import termcolor

def generate_ascii_art(text, font, color, width):
    figlet = pyfiglet.Figlet(font=font)
    art = figlet.renderText(text)
    art_lines = [line[:width] for line in art.split("\n")]
    art = "\n".join(art_lines)
    art = termcolor.colored(art, color)
    return art
