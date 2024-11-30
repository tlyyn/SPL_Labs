import sys
from Data.lab5.Classes.cube import Cube
from Data.lab5.Classes.scene import Scene
from Data.lab5.Functions.file_operations import save_ascii_art


class CommandLineInterface:
    def __init__(self):
        self.scene = Scene()

    def run(self):
        print("Welcome to the 3D ASCII Art Generator!")
        while True:
            command = input("Enter a command (create/render/save/scale/translate/exit): ").lower()
            if command == "exit":
                sys.exit(0)
            elif command == "create":
                self.create_cube()
            elif command == "render":
                self.scene.render_scene()
            elif command == "save":
                self.save_to_file()
            elif command == "scale":
                self.scale_cube()
            elif command == "translate":
                self.translate_cube()
            else:
                print("Invalid command. Please try again.")

    def create_cube(self):
        try:
            size = float(input("Enter the size of the cube: "))
            cube = Cube(size)
            self.scene.add_shape(cube)
            print("Cube created.")
        except ValueError:
            print("Invalid input. Please enter a numeric size.")

    def scale_cube(self):
        if not self.scene.shapes:
            print("No shapes to scale. Please create a shape first.")
            return

        try:
            factor = float(input("Enter the scale factor: "))
            for shape in self.scene.shapes:
                shape.scale(factor)
            # Automatically render after scaling
            self.scene.render_scene()
        except ValueError:
            print("Invalid input. Please enter a numeric scale factor.")

    def translate_cube(self):
        if not self.scene.shapes:
            print("No shapes to translate. Please create a shape first.")
            return

        try:
            dx = float(input("Enter the shift in the x-direction: "))
            dy = float(input("Enter the shift in the y-direction: "))
            dz = float(input("Enter the shift in the z-direction: "))
            for shape in self.scene.shapes:
                shape.translate(dx, dy, dz)
            # Automatically render after translation
            self.scene.render_scene()
        except ValueError:
            print("Invalid input. Please enter numeric values for shifts.")
