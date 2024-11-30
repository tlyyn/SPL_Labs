class Scene:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def render_scene(self):
        for shape in self.shapes:
            print(shape.draw())
