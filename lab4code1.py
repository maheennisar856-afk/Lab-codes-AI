import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
r = float(input("Enter the radius of the circle: "))
circle = Circle(r)

print("Area of circle:", circle.area())
print("Perimeter of circle:", circle.perimeter())

