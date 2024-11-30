class Command:
    def execute(self):
        pass


class DrawCubeCommand(Command):
    def __init__(self, cube):
        self.cube = cube

    def execute(self):
        return self.cube.draw()

