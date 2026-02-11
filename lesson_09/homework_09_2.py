class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * 3.14 * self.radius**3

class Cube:
    def __init__(self, side_length):
        self.side_length = side_length

    def volume(self):
        return self.side_length**3

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return 3.14 * self.radius**2 * self.height

def calculate_volume(obj):
    return obj.volume()

sphere_1 = Sphere(radius=2)
print(calculate_volume(sphere_1))
cube_1 = Cube(side_length=3)
print(calculate_volume(cube_1))
cylinder_1 = Cylinder(radius=2, height=3)
print(calculate_volume(cylinder_1))