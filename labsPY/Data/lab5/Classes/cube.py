class Cube:
    def __init__(self, size):
        self.size = size
        self.position = (0, 0, 0)  # Default position at origin

    def draw(self, colored=True):
        # Calculate shifts based on position
        x_shift, y_shift, _ = self.position

        # Adjust the ASCII art by adding spaces for x and y translation
        horizontal_shift = " " * int(x_shift)
        vertical_shift = "\n" * int(y_shift)

        # Cube drawing as ASCII art with translation effect
        t = v = h = int(self.size / 2)
        s, p, b, f, n = " ", "+", "|", "/", "\n"
        l = p + "-" * (t * 4) + p
        S = s * (4 * t)
        k = s * h
        K = b + S + b
        r = vertical_shift + (s * t) + s + l + n
        while t:
            r += (s * t) + f + (S + f + s * (h - t) + b) + n
            t -= 1
        r += l + (k + b) + n + ((K + k + b + n) * (v - 1)) + K + k + p + n
        while v:
            v -= 1
            r += K + (s * v) + f + n
        r += l

        return horizontal_shift + r.replace("\n", "\n" + horizontal_shift)

    def scale(self, factor):
        """Scale the cube by a given factor."""
        self.size *= factor
        print(f"Cube scaled by a factor of {factor}. New size: {self.size}")

    def translate(self, dx, dy, dz):
        """Translate (shift) the cube by (dx, dy, dz)."""
        x, y, z = self.position
        self.position = (x + dx, y + dy, z + dz)
        print(f"Cube translated to new position: {self.position}")
