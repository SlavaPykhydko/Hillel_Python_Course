class Figure:

    def square(self):
        print("Calculating square...")

    def perimeter(self):
        print("Calculating perimeter...")

class Rectangle(Figure):
    def __init__(self, side_a: float, side_b: float):
        self.side_a = side_a
        self.side_b = side_b

    def square(self):
        super().square()
        return self.side_a * self.side_b

    def perimeter(self):
        super().perimeter()
        return 2 * (self.side_a + self.side_b)

class Triangle(Figure):
    def __init__(self, high: float, side: float):
        self.high = high
        self.side = side

    def square(self):
        super().square()
        return (self.high * self.side)/2

    def perimeter(self):
        super().perimeter()
        return 3* self.side

rectangle_1 = Rectangle(side_a=5, side_b=4)
print(rectangle_1.square())
print(rectangle_1.perimeter())

triangle_1 = Triangle(high=5, side=4)
print(triangle_1.square())
print(triangle_1.perimeter())





