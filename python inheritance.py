class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def disp(self):
        print("polygon is a 2D figure with lines")


class Triangle(Polygon):
    def disp(self):
        print("A triangle is a figure with 3 sides")
        # Method overriding
        Polygon.disp(self)
        # OR
        super().disp()

t = Triangle([1, 2, 3])
t.disp()
