import math

class SimpleLogger:
    def __init__(self):
        self.last_message = None

    def log(self, message):
        self.last_message = message
        print(f"LOG: {self.last_message}")

class Sphere:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")

        if radius <= 0:
            raise ValueError("Radius must be positive")

        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius**3

    def __repr__(self):
        return f"Sphere(radius={self.radius})"


class Cube:
    def __init__(self, side_length):
        self.side_length = side_length

    def volume(self):
        return self.side_length**3

    def __repr__(self):
        return f"Cube(side_length={self.side_length})"

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return 3.14 * self.radius**2 * self.height

    def __repr__(self):
        return f"Cylinder(radius={self.radius}, height={self.height})"

def calculate_volume_and_log(obj, logger=None):
    volume = obj.volume()
    if logger:
        logger.log(f'Object: {obj}, volume is: {volume}')
    return volume

logger = SimpleLogger()

sphere_1 = Sphere(radius=2)
calculate_volume_and_log(sphere_1, logger)
cube_1 = Cube(side_length=3)
calculate_volume_and_log(cube_1, logger)
cylinder_1 = Cylinder(radius=2, height=3)
calculate_volume_and_log(cylinder_1, logger)
