import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_float_value(self):
        return float(self.radius)

    def calculate_diameter(self):
        diameter = self.radius * 2
        return float(diameter)

    def calculate_circumference(self):
        circumference = 2 * math.pi * self.radius
        return float(circumference)

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return float(area)

    def grow(self):
        double_radius = self.radius * 2
        return float(double_radius)

    def get_radius(self):
        return float(self.radius)


if __name__ == "__main__":
    radius_value = input("Enter a radius:")
    c1 = Circle(radius_value)
    float_value = c1.get_float_value()

print(f"Diameter:{Circle.calculate_diameter}")
print(f"Circumference:{Circle.calculate_circumference}")
print(f"Area:{Circle.calculate_area}")
running = True
while running:
    print(f"New Radius:{Circle.grow}")
    print(f"Diameter:{Circle.calculate_diameter}")
    print(f"Circumference:{Circle.calculate_circumference}")
    print(f"Area:{Circle.calculate_area}")
    if input("Grow the circle? (y/n)") == "n":
        running = False
        print("Goodbye!")
        print(f"Circle Radius:{Circle.get_radius}")
